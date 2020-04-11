from django import forms


categories  =[("1", "Academic"), ("2", "General")]
class QuoteForm(forms.Form):

    categoriess = forms.ChoiceField(choices = categories, label="")
    word_count = forms.DecimalField()