from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from user_accounts.forms import LoginForm
from user_accounts.forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from quote.models import Quote, QuoteFiles, Upload
from django.http import HttpResponseNotFound
from quote.forms import  UploadFileForm


#-------------------------------------------------------------------------------------------------#
# creates a presigned url to be passed to user_account page
# as shown at https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
import logging
import boto3
from botocore.exceptions import ClientError
import requests 

def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains presigned URL
    return response
#-----------------------------------------------------------------------------------#



def logout(request):
    #Logs user out and returns index page
    auth.logout(request)
    messages.add_message(request, messages.INFO, 'logout')
    return render(request, 'index.html')


@login_required(login_url='/login/')
def user_account(request):
    # Create the list of orders containing all relevant information.
    # Pass the list of orders to the user account template.
    # Return user account page.

    # the data structure produced by the code bellow 
    # explaned at Documentation >> Data Structure >> User Accounts.
    uploadForm = UploadFileForm
    if request.user.is_superuser: 
        orders = Quote.objects.all().filter(purchased = True, status= "Pending")#if user is freelancer get pending orders only.
    else: 
        current_user = request.user
        user = current_user.username
        orders = Quote.objects.all().filter(purchased = True, submitted_by = user)# if user is not freelaner get orders purchased by the user.

    # creates the list_of_orderLists that contains all the relevant order information.
    # the logic is explained in the documentation. please refer to the Features > Account page section
    list_of_orderLists = []
    for eachOrder in orders:
            orderList = []
            orderList.append(eachOrder.id)
            orderList.append(eachOrder.title)
            orderList.append(eachOrder.status)

            list_of_files_n_urls = []
            
            files = QuoteFiles.objects.all().filter(quote_ref=eachOrder.id)
            for eachFile in files:
                list_of_files = []
                list_of_files.append(eachFile.file_name)

                url_str = "media/documents/" + str(eachOrder.id) + "_" + eachFile.file_name
                url = create_presigned_url('freelancer2020', url_str)
                list_of_files.append(url)
                
                list_of_files.append(eachFile.status)

                list_of_files_n_urls.append(list_of_files)
            orderList.append(list_of_files_n_urls)

            list_of_orderLists.append(orderList)
    # pass the list_of_orderList to the user_account & return user account page.
    context = { "list_of_orderLists": list_of_orderLists, "count" : len(orders), "uploadForm" : uploadForm }
    return render(request, 'user_account.html', context = context)


  
 
def user_login(request):
     #Logs user in or returns a log-in page.
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "login success")
                try:
                  return HttpResponseRedirect(request.GET['next'])
                except:
                  return redirect(reverse('user_account'))#if the destination is not defined return user account page
            else:
                loginForm.add_error(None, "Your username or password is incorrect")
                return render(request, 'login.html', {"loginForm": loginForm, "user": user})
    else:
       if request.user.is_authenticated:
          return redirect(reverse('user_account'))
       else:
          loginForm = LoginForm()
          return render(request, 'login.html', {"loginForm": loginForm})


def signup(request):
    #Creates new user
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "signup success")
            try:
                  return HttpResponseRedirect(request.GET['next'])
            except:
                  return render(request, 'user_account.html')#if the destination is not defined return user account page
        else:
            form.add_error(None, "Your username or password is incorrect")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})  



