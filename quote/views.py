from django.shortcuts import render
from django.http import HttpResponseRedirect

from quote.forms import QuoteManualForm, QuoteUploadForm
from django.core.files import File 





def quote(request):
    #Return quote page. Incase of quote form submit return quote.
    manual_form = QuoteManualForm
    upload_form = QuoteUploadForm
    context = { "price": "","manual_form": manual_form, "upload_form": upload_form }
    

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
      if count > 1000:
         price = round(count / 100)
      else:
         price = 10
      context = { "price": price, "manual_form": manual_form, "upload_form" : upload_form }
      return render(request, 'quote.html', context)
    else:
        return render(request, 'quote.html', context)


