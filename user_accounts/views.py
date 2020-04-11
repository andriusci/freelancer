from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from user_accounts.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
    #Return the index.html file
     return render(request, 'index.html')


def logout(request):
    #Logout
    auth.logout(request)
    return redirect(reverse('login'))


def user_account(request):
    #Return user_account.html file
     return render(request, 'user_account.html')

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
                return redirect(reverse ('user_account'))
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
            return redirect(reverse('user_account'))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})