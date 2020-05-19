from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from user_accounts.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from quote.models import Quote


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
    #Return user_account.html file
    current_user = request.user
    user = current_user.username
    orders = Quote.objects.all().filter(submitted_by=user, purchased = True)
    context = {  "orders": orders,   
                 #"add_to_basket_form": AddToBasketForm(initial=initial)
                   }
      
    return render(request, 'user_account.html', context=context)



def user_login(request):
    #Return a log in page
    if request.method == "POST":
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            messages.success(request, "login success")

            if user:
                auth.login(user=user, request=request)
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
         #   return redirect(reverse('user_account'))
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})  



