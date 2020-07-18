from django import forms


class ChatForm(forms.Form):
    #Form to be used send Email to freelancer
    message = forms.CharField(widget=forms.Textarea(attrs = {'class' : "chat_text"}), label="")
    quote_ref = forms.IntegerField(widget=forms.HiddenInput())
    file_name = forms.CharField(widget=forms.HiddenInput())
    