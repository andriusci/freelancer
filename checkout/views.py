from django.shortcuts import render
import stripe
import os

stripe.api_key = os.getenv('STRIPE_SECRET')
#stripe.api_key = "sk_test_gaXrNd3ptwCYLK5NIGUU3ssU00wD4sYZob"

def checkout(request):
    if request.method == 'POST':
        str_of_refs = request.POST.get('str_of_refs')
        total = request.POST.get('total')
        #convert total amount from currency format (€x.xx) to string (xxx) suitable for stripe.
        total2 = ""
        for elem in total:
            if elem != ".":
                total2 = total2 + elem
        
        context = {"str_of_refs":str_of_refs, "total" : total, "total2": total2}
        return render(request, 'checkout.html',context = context)

def payment(request):
       if request.method == 'POST':
        total = request.POST.get('total2')
        str_of_refs = request.POST.get('str_of_refs')
      
        charge = stripe.Charge.create(
            amount=total,
            currency='eur',
            description=str_of_refs,
            source=request.POST['stripeToken']
        )
        current_user = request.user
        user = current_user.username
     #   orders = Quote.objects.all().filter(submitted_by=user)
        context = {"token" : total}
        return render(request, 'checkout_success.html', context = context)