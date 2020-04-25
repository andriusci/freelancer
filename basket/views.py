from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import AddToBasket 
from django.contrib import messages


@login_required(login_url='/login/')
def basket(request):
      return render(request, 'basket.html')


@login_required(login_url='/login/')
def add_to_basket(request):

    if request.method == "POST":
           data = request.POST.copy()
           user = (data.get('user'))
           quote_ref = data.get('quote_ref')
     
           add_to_basket = AddToBasket(user=user,
                                       quote_ref = quote_ref)
           add_to_basket.save()

           messages.add_message(request, messages.INFO, 'added')
           return redirect(reverse('quote'))
    return redirect(reverse('quote'))