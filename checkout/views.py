from django.shortcuts import render
from basket.models import AddToBasket
import stripe
from quote.models import Quote
import os
from django.http import HttpResponse
stripe.api_key = os.getenv('STRIPE_SECRET')


def checkout(request):
    # returns the checkout page with the relevant information such as the amount to be paid#
    # and the list of quote references (so after the paiment is made satus of the quote could be changed )
    if request.method == 'POST':
        str_of_refs = request.POST.get('str_of_refs')
        total = request.POST.get('total')
        #convert total amount from currency format (€x.xx) to string (xxx) suitable for Stripe.
        total2 = ""
        for elem in total:
            if elem != ".":
                total2 = total2 + elem
        
        context = {"str_of_refs":str_of_refs, "total" : total, "total2": total2}
        return render(request, 'checkout.html',context = context)
    else:
        html = "<html><body> The page you are trying to access does not exist.</body></html>" 
        return HttpResponse(html)
   
def payment(request):
       if request.method == 'POST':
        current_user = request.user
        user = current_user.username
        total = request.POST.get('total2')
        str_of_refs = request.POST.get('str_of_refs')
        str_of_refs = str_of_refs.replace(" ", "")
        str_of_refs = str_of_refs + "," 
        charge = stripe.Charge.create(
            amount=total,
            currency='eur',
            description=str_of_refs,
            source=request.POST['stripeToken']
        )

        list_of_refs = []
        ref = ""
        for eachChar in str_of_refs:
             if eachChar != ",":
                 ref = ref + eachChar
             else: 
                 list_of_refs.append(ref)
                 ref = ""

        remove_basket_items = AddToBasket.objects.filter(user=user)
        remove_basket_items.delete()


        quote_instance = Quote.objects.filter(submitted_by=user)
        for eachQuote in list_of_refs:

            eachQuote = eachQuote.replace("[","").replace("]","")
            instance = quote_instance.get(id=eachQuote)
            instance.purchased = True
            instance.save()
          
        context = {"token" : total, "str_of_refs": str_of_refs}
        return render(request, 'checkout_success.html', context = context)