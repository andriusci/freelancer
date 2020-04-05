from django import forms

class LoginForm(forms.Form):
#Defines user login form containing two fields, namely username (email address) and password.
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)