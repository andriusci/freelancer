from django import forms
from quote.models import Upload

categories  =[("Academic", "Academic"), ("General", "General")]
class QuoteManualForm(forms.Form):

    categories = forms.ChoiceField(choices = categories, label="")
    word_count = forms.DecimalField(min_value=1)

class QuoteUploadForm(forms.Form):
          categories = forms.ChoiceField(choices = categories, label="")
          document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
             