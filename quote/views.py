from django.shortcuts import render
from django.http import HttpResponseRedirect

from quote.forms import QuoteManualForm, QuoteUploadForm


def quote(request):
    #Return quote page. Incase of quote form submit return quote.
    manual_form = QuoteManualForm
    upload_form = QuoteUploadForm
    context = { "price": "","manual_form": manual_form, "upload_form": upload_form }
    

    if request.method == "POST":
      if request.POST['form'] == "Submit":
        data = request.POST.copy()
        count = int(data.get('word_count'))
        if count > 1000:
          price = round(count / 100)
        else:
          price = 10
        context = { "price": price, "manual_form": manual_form, "upload_form" : upload_form }
        return render(request, 'quote.html', context)
      if request.POST['form'] == "Upload":
        form = QuoteUploadForm(request.POST, request.FILES)
        if form.is_valid:
          
          status = "yes"
          form.save()
         
        context = { "price": form,"manual_form": manual_form, "upload_form": upload_form }
        return render(request, 'quote.html', context)
    else:
        return render(request, 'quote.html', context)


