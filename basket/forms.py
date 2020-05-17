from  django import forms



class AddToBasketForm(forms.Form):

    quote_ref = forms.IntegerField()

    #widget=forms.HiddenInput())

