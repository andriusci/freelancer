from django import forms
from quote.models import Upload

categories  =[("Academic", "Academic"), ("General", "General")]


class QuoteUploadForm(forms.Form):
         # categories = forms.ChoiceField(widget=forms.Select(attrs={'class' : 'form-input'}), choices = categories, label="",)
         # number = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-input', 'placeholder': 'Number of words'}), label="")
         # document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class' : 'form-input'}))
          description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-input', 'placeholder': 'Description'}), label="")


class OpenDocument(forms.Form):

    quote_ref = forms.IntegerField(widget=forms.HiddenInput())