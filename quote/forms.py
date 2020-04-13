from django import forms
from quote.models import Document

categories  =[("1", "Academic"), ("2", "General")]
class QuoteManualForm(forms.Form):

    categoriess = forms.ChoiceField(choices = categories, label="")
    word_count = forms.DecimalField()

class QuoteUploadForm(forms.Form):
          document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))