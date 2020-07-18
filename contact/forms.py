from django import forms

class ContactForm(forms.Form):
    #Form to be used to contact the freelancer
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'myfieldclass'}))
    email_body = forms.CharField(widget=forms.Textarea(attrs={'class' : 'myfieldclass', 'rows':9}))