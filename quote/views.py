from django.shortcuts import render
from django.http import HttpResponseRedirect

from quote.forms import QuoteManualForm, QuoteUploadForm
from quote.models import Upload, Quote, QuoteFiles
from basket.forms import AddToBasketForm
from django.core.files import File 
from datetime import datetime




def quote(request):
    #Return quote page. Incase of quote form submit return quote.
    manual_form = QuoteManualForm
    upload_form = QuoteUploadForm
    context = { "price": "",
                "manual_form": manual_form, 
                "upload_form": upload_form, 
                "add_to_basket_form": AddToBasketForm }
    

    if request.method == "POST":

      time = datetime.now()

      if request.POST['form'] == "Submit":
        data = request.POST.copy()
        count = int(data.get('word_count'))
        category = data.get('categories')
        

      if request.POST['form'] == "Upload":
        form = QuoteUploadForm(request.POST, request.FILES)
        if form.is_valid:
           files = request.FILES.getlist('document')
           category = request.POST.get('categories')
           count = 0
           for eachFile in files: 
               raw = eachFile.read()
               count = count + len(raw.split())
            
      

         
           
      if count > 1000:
         price = count / 100
      else:
         price = 10
      if category != "General":
         price = price * 1.1
      price = round(price)
     
   
                   
      #populate quote model intance fields:
     
      quote_instance = Quote(category = category,
                             word_count = count,
                             uploaded_on = time,
                             price = price,)

      quote_instance.save()
      
      quote_ref = quote_instance.pk
      if request.POST['form'] == "Upload":
        for eachFile in files:
            file_name = str(quote_ref) + eachFile.name
        
            quote_file_instance = QuoteFiles(name = file_name,
                                             quote_ref = quote_ref)
            quote_file_instance.save()  

            eachFile.name =file_name          
            upload_file = Upload( document = eachFile )
            upload_file.save()


      current_user = request.user
      
      initial = {
                 'user': current_user.username,
                 'quote_ref': 3 
}
     
      context = { "price": price, 
                  "manual_form": manual_form,
                  "upload_form" : upload_form,  
                  "add_to_basket_form": AddToBasketForm(initial=initial)
                   }
      

      return render(request, 'quote.html', context)
    else:
        return render(request, 'quote.html', context)


