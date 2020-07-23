from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import AddToBasket
from django.contrib import messages
from quote.forms import  QuoteUploadForm
from quote.models import Upload, Quote, QuoteFiles
from basket.forms import AddToBasketForm


@login_required(login_url='/login/')
#Creates basket item list, calculates total price and returns basket page with the information.
def basket(request):
        current_user = request.user
        user = current_user.username
        basket_items = AddToBasket.objects.all().filter(user=user)
        quote_ref_list = []
        for eachItem in basket_items:
              quote_ref_list.append(eachItem.quote_ref)
        basket_item_list = []
        price_list = []
        for eachQuote in quote_ref_list:
             #from the quote object return each quote price, ref and title 
              quote = Quote.objects.all().filter(id=eachQuote)
              total_price = 0
              for eachQuote in quote:
                 quote_ref = eachQuote.id
                 total_price = total_price + quote_ref
                 price = eachQuote.price
                 title = eachQuote.title
                 price_list.append(price)
                 basket_item_list.append({"quote_ref": quote_ref, "price": price, "title": title})
              
        total = sum(price_list)
        str_of_refs = quote_ref_list #used by checkout form in the basket page to send the list of quote references to the checkout view
        context = {"list": basket_item_list, "total" : total,"str_of_refs": str_of_refs}

        return render(request, 'basket.html', context)


@login_required(login_url='/login/')
def add_to_basket(request):
      #Adds quote to the basket and informs the user.
      if request.method == "POST":
           current_user = request.user
           user = current_user.username#get current user

           data = request.POST.copy()
           quote_ref = data.get('quote_ref')#get quote reference

           
           quote = Quote.objects.get(id=quote_ref)#get quote instance, for the actions bellow:
           
    
           if quote.added_to_basket != True: #check if the quote is not already in the basket.
              quote.added_to_basket = True   # change the status of the quote's object field "added_to_basket" to True (needed for data analysis)
              quote.save()

              add_to_basket = AddToBasket(user=user,
                                       quote_ref = quote_ref) # add the quote reference to the basket objects (used to create basket items list in the basket view)
              add_to_basket.save()
              
              messages.add_message(request, messages.INFO, "added")# create "added to the basket" message (will pop up on the screen)

              return redirect(reverse('quote_logged'))
           else:
              upload_form = QuoteUploadForm
              context = { "price": "",
                          "upload_form": upload_form, 
                          "add_to_basket_form": AddToBasketForm,
                          "warning": True }
              return render(request, 'quote_logged.html', context)
      else:
         return redirect(reverse('basket'))#if url entered manually redirect to basket page
        
        
        
def remove_from_basket(request):
    #removes item from user's basket and changes quote's added_to_basket status to false.
    if request.user.is_authenticated:
      if request.method == "POST":
           current_user = request.user
           user = current_user.username

           data = request.POST.copy()
           quote_ref = data.get('quote_ref')
           
           #change status of quote instance to False. (used for data analysis)
           quote = Quote.objects.get(id=quote_ref)
           quote.added_to_basket = False
           quote.save()
           
           #remove the quote from the user's basket.
           remove = AddToBasket.objects.get(quote_ref=quote_ref)
           remove.delete()

    return redirect(reverse('basket'))