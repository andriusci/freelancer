from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import AddToBasket
from django.contrib import messages
from quote.models import Quote


@login_required(login_url='/login/')
def basket(request):

        #MakePaymentForm
        current_user = request.user
        user = current_user.username

        basket_items = AddToBasket.objects.all().filter(user=user)
        

        quote_ref_list = []
       
        for eachItem in basket_items:
              quote_ref_list.append(eachItem.quote_ref)

        basket_item_list = []
        price_list = []
        for eachQuote in quote_ref_list:
             #from the quote object return each quotes price, ref and title 
              quote = Quote.objects.all().filter(id=eachQuote)

              total_price = 0
              for eachQuote in quote:
                 quote_ref = eachQuote.id
                 total_price = total_price + quote_ref
                 price = eachQuote.price
                 title = eachQuote.title
                 
                 price_list.append(price)
                 basket_item_list.append({"quote_ref": quote_ref, "price": price, "title": title})
              #add those too list of dict
        total = sum(price_list)
        str_of_refs = str(quote_ref_list)
        context = {"list": basket_item_list, "total" : total,"str_of_refs": str_of_refs}

        return render(request, 'basket.html', context)



def add_to_basket(request):
    
    if request.user.is_authenticated:
      if request.method == "POST":
           current_user = request.user
           user = current_user.username

           data = request.POST.copy()
           quote_ref = data.get('quote_ref')
           
           quote = Quote.objects.get(id=quote_ref)
           quote.added_to_basket = True
           quote.save()

           add_to_basket = AddToBasket(user=user,
                                       quote_ref = quote_ref)
           add_to_basket.save()

           context = {"username": user, "quote": quote.id }

           return redirect(reverse('basket'))
      else:


           context = {"username": user, "quote": quote.id}
   
      return render(request, 'basket.html', context)
        
        
        
def remove_from_basket(request):
    if request.user.is_authenticated:
      if request.method == "POST":
           current_user = request.user
           user = current_user.username

           data = request.POST.copy()
           quote_ref = data.get('quote_ref')
           
           quote = Quote.objects.get(id=quote_ref)
           quote.added_to_basket = False
           quote.save()
      
           remove = AddToBasket.objects.get(quote_ref=quote_ref)
           remove.delete()

    return redirect(reverse('basket'))