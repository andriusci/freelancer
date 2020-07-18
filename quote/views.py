# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from user_accounts.views import user_login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from quote.forms import  QuoteUploadForm, UploadFileForm
from chat.forms import ChatForm
from chat.models import Chat
from quote.models import Upload, QuoteFiles, Quote
from basket.forms import AddToBasketForm
from django.core.files import File 
from datetime import datetime

from django.contrib import messages








def quote(request):
     #return quote page
      return render(request, 'quote.html')


@login_required(login_url='/login/')
#1.return quote page for logged-in users.
#2.if quote form submitted, calculate the price depending on the number of words in the submitted documents.
#and return a quote page with the quote information.
#3. save the quote and the files in the database. (see section Features > Quote in the READ.ME for reasoning)
def quote_logged(request):
    current_user = request.user
    user = current_user.username

    upload_form = QuoteUploadForm
    context = { "price": "",
                "upload_form": upload_form, 
                "add_to_basket_form": AddToBasketForm,
    }

    if request.method == "POST":
      time = datetime.now()
      
      form = QuoteUploadForm(request.POST, request.FILES)
      if form.is_valid:
           files = request.FILES.getlist('document')
           category = request.POST.get('category')
           title = request.POST.get('description')
           count = 0
           for eachFile in files: 
               raw = eachFile.read()
               count = count + len(raw.split())
              
      if count > 1000:
         price = count / 100
         discount = price * 0.9
      else:
         price = 10
      if category != "general":
         price = price * 1.1
      price = round(price)
     
                   
    
     
      quote_instance = Quote(
                             category = category,
                             word_count = count,
                             uploaded_on = time,
                             price = price,
                             title= title,
                             submitted_by = user )

      quote_instance.save()
      
      quote_ref = quote_instance.pk

    
      
      for eachFile in files:
            quote_file_instance = QuoteFiles(file_name = eachFile.name, quote_ref = quote_ref, user = user)
            quote_file_instance.save()

            file_name = str(quote_ref) +"_"+ eachFile.name
             
            eachFile.name = file_name          
            upload_file = Upload( document = eachFile )
            upload_file.save()
           
                                                                
      messages.add_message(request, messages.INFO, quote_ref, extra_tags='quote')
      messages.add_message(request, messages.INFO, price, extra_tags='price')

        
      return redirect(reverse('quote_logged'))
    else:
      return render(request, 'quote_logged.html', context)

@login_required(login_url='/login/')
def reupload(request, quote_ref, file_name):
    current_user = request.user
    user = current_user.username
    uploadForm = UploadFileForm
    chatForm = ChatForm
    if request.user.is_superuser:
        quote = Quote.objects.get(id = quote_ref)
        user = quote.submitted_by
    chat = Chat.objects.all().filter(user = user, 
                                     quote_ref = quote_ref, 
                                     file_name = file_name)                        
    context = {"quote_ref": quote_ref,"file_name": file_name, "file": "nothing", "uploadForm": uploadForm, "chatForm": chatForm, "chat":chat }
    if request.method =="POST":
      if request.user.is_superuser:
       form = UploadFileForm(request.POST, request.FILES)
       files = request.FILES.get('files')
       status = QuoteFiles.objects.get(quote_ref = quote_ref, file_name = file_name)
       status.status = "Ready"
       status.save()
       fileName = str(quote_ref) +"_"+ files.name
       files.name = fileName
       upload_file = Upload( document = files)
       upload_file.save()
       
       chat = Chat.objects.all().filter(user = user, quote_ref = quote_ref, file_name = file_name)
       
       context = {"quote_ref": quote_ref,"file_name": file_name, "file": files, "uploadForm": uploadForm, "chatForm": chatForm, "chat":chat }
       messages.add_message(request, messages.INFO, "upload", extra_tags='upload')
      
   

    
    return render(request, 'reupload.html', context = context)

@login_required(login_url='/login/')
def accept(request, quote_ref, file_name):
    current_user = request.user
    user = current_user.username
    quote_file = QuoteFiles.objects.get(quote_ref = quote_ref, file_name = file_name)
    #check if request is from authorised user
    if user == quote_file.user:
       quote_file.status = "Accepted"
       quote_file.save()

       messages.add_message(request, messages.INFO, "accepted", extra_tags='accepted')

        
    return redirect(reverse('user_account'))

def accept_quote(request, quote_ref):
   if request.user.is_superuser:
      quote = Quote.objects.get(id = quote_ref)
      quote.status = "Accepted"
      quote.save()
      messages.add_message(request, messages.INFO, "quote_accepted")
      return redirect(reverse('user_account'))
   else:
      html = "<html><body><h1>Nothing here:)</h1></html>" % now
      return HttpResponse(html)
