from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'myfieldclass'}))





class ReuploadForm(forms.Form):
    name = forms.IntegerField(widget=forms.HiddenInput())

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='O')
    email = forms.EmailField(max_length=254, help_text='Email address.')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )