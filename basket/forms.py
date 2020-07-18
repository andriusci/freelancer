from  django import forms



class AddToBasketForm(forms.Form):
    #Form to be used add items to the basket 
    quote_ref = forms.IntegerField(widget=forms.HiddenInput())

    
 
