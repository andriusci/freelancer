from  django import forms



class AddToBasketForm(forms.Form):

    user = forms.CharField(max_length=100)
    quote_ref = forms.IntegerField()

    #widget=forms.HiddenInput())

