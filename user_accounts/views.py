from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from user_accounts.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from quote.models import Quote, QuoteFiles, Upload
from django.http import HttpResponseNotFound

#####################################################
import logging
import boto3
from botocore.exceptions import ClientError
import requests    # To install: pip install requests
################################################



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

    # The response contains the presigned URL
    return response
    #############################################################################



def index(request):
    #Return the index.html file
     return render(request, 'index.html')


def logout(request):
    #Logout
    auth.logout(request)
    messages.add_message(request, messages.INFO, 'logout')
    return render(request, 'index.html')


@login_required(login_url='/login/')
def user_account(request):

    if request.user.is_superuser: 
        orders = Quote.objects.all().filter(purchased = True, status= "SUBMITTED")
    else: 
        current_user = request.user
        user = current_user.username
        orders = Quote.objects.all().filter(purchased = True, submitted_by = user)

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

                list_of_files_n_urls.append(list_of_files)
            orderList.append(list_of_files_n_urls)

            list_of_orderLists.append(orderList)
       
    context = { "orders": list_of_orderLists }
       
    return render(request, 'user_account.html', context = context)


  
 
def user_login(request):
    #Return a log in page
    if request.method == "POST":
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "login success")
                return HttpResponseRedirect(request.GET['next'])
            else:
                loginForm.add_error(None, "Your username or password is incorrect")
                

    else:
       loginForm = LoginForm()
    return render(request, 'login.html', {"loginForm": loginForm})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(request.GET['next'])
        else:
            form.add_error(None, "Your username or password is incorrect")
         
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})  



