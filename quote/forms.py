from django import forms
from quote.models import Upload

categories  =[("Academic", "Academic"), ("General", "General")]


class QuoteUploadForm(forms.Form):
        #form used in addition to inline html quote form
          description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-input', 'placeholder': 'Description'}), label="")


class UploadFileForm(forms.Form):
    #form used to upload files
    files = forms.FileField(label="", widget = forms.FileInput(attrs = {'onchange' : "customUpload();"}))

