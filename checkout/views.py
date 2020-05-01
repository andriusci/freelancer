from django.shortcuts import render


def checkout(request):
     if request.method == "POST":
          return render(request, 'checkout_success.html')
     return render(request, 'checkout.html')