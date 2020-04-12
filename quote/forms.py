from django import forms
from quote.models import Document

categories  =[("1", "Academic"), ("2", "General")]
class QuoteManualForm(forms.Form):

    categoriess = forms.ChoiceField(choices = categories, label="")
    word_count = forms.DecimalField()

class QuoteUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )