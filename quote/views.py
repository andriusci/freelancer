from django.shortcuts import render
from django.http import HttpResponseRedirect

from quote.forms import QuoteForm


def quote(request):
    #Return quote page. Incase of quote form submit return quote.
    form = QuoteForm
    context = { "price": "","form": form }
    

    if request.method == "POST":
        data = request.POST.copy()
        count = int(data.get('word_count'))
        if count > 1000:
          price = round((count - 1000) / 100 + 15)
        else:
          price = 15
        context = { "price": price,"form": form }
        return render(request, 'quote.html', context)
    else:
        return render(request, 'quote.html', context)
