from django.shortcuts import render
from django.http import HttpResponseRedirect

from quote.forms import QuoteManualForm, QuoteUploadForm
from quote.models import Upload
from django.core.files import File 





def quote(request):
    #Return quote page. Incase of quote form submit return quote.
    manual_form = QuoteManualForm
    upload_form = QuoteUploadForm
    context = { "price": "","manual_form": manual_form, "upload_form": upload_form, "file": "" }
    

    if request.method == "POST":
      if request.POST['form'] == "Submit":
        data = request.POST.copy()
        count = int(data.get('word_count'))
      if request.POST['form'] == "Upload":
        form = QuoteUploadForm(request.POST, request.FILES)
        if form.is_valid:
           files = request.FILES.getlist('document')
           count = 0
           for eachFile in files: 
               raw = eachFile.read()
               count = count + len(raw.split())

               #upload_file = Upload( document = eachFile )
               #upload_file.save()

               file1 = eachFile.file
              
      if count > 1000:
         price = round(count / 100)
      else:
         price = 10
      context = { "price": price, "manual_form": manual_form, "upload_form" : upload_form, "file": file1 }
      return render(request, 'quote.html', context)
    else:
        return render(request, 'quote.html', context)


