from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'myfieldclass'}))





class ReuploadForm(forms.Form):
    name = forms.IntegerField(widget=forms.HiddenInput())