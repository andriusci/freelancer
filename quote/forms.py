from django import forms
from quote.models import Upload

categories  =[("Academic", "Academic"), ("General", "General")]


class QuoteUploadForm(forms.Form):
          categories = forms.ChoiceField(choices = categories, label="")
          document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
          description = forms.CharField()