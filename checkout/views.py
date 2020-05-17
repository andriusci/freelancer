from django.shortcuts import render
import stripe
import os

stripe.api_key = os.getenv('STRIPE_SECRET')
#stripe.api_key = "sk_test_gaXrNd3ptwCYLK5NIGUU3ssU00wD4sYZob"
def checkout(request):
    
     if request.method == 'POST':
        
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'checkout_success.html')
     else:
        return render(request, 'checkout.html')