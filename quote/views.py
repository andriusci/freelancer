from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from quote.forms import  QuoteUploadForm, UploadFileForm
from chat.forms import ChatForm
from quote.models import Upload, Quote, QuoteFiles
from basket.forms import AddToBasketForm
from django.core.files import File 
from datetime import datetime

from django.contrib import messages






def quote(request):
      return render(request, 'quote.html')


@login_required(login_url='/login/')
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
      

     # if request.POST['form'] == "Upload":
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
     
                   
      #populate quote model intance fields:
     
      quote_instance = Quote(
                             category = category,
                             word_count = count,
                             uploaded_on = time,
                             price = price,
                             title= title,
                             submitted_by = user )

      quote_instance.save()
      
      quote_ref = quote_instance.pk

     # if request.POST['form'] == "Upload":
      
      for eachFile in files:
            quote_file_instance = QuoteFiles(file_name = eachFile.name, quote_ref = quote_ref)
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


def reupload(request, quote_ref, file_name):
    uploadForm = UploadFileForm
    chatForm = ChatForm
    context = {"quote_ref": quote_ref,"file_name": file_name, "file": "nothing", "uploadForm": uploadForm, "chatForm": chatForm }
    if request.method =="POST":
       form = UploadFileForm(request.POST, request.FILES)
       files = request.FILES.get('files')

       fileName = str(quote_ref) +"_"+ files.name
       files.name = fileName
       upload_file = Upload( document = files)
       upload_file.save()

       context = {"quote_ref": quote_ref,"file_name": file_name, "file": files, "uploadForm": uploadForm, "chatForm": chatForm }
       messages.add_message(request, messages.INFO, "upload", extra_tags='upload')
       return render(request, 'reupload.html', context = context)
    else:
       return render(request, 'reupload.html', context = context)