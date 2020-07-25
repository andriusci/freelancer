from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# done with help frpm tutorial https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html 

class LoginForm(forms.Form):
    #Form to be used to log users in
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-input'}))


 
class SignUpForm(UserCreationForm):
    #Form to be used to create new users
    username = forms.CharField(max_length=320, required=True)
    email = forms.EmailField(max_length=254,)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
      
        