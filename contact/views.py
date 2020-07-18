from django.shortcuts import render
from contact.forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

def contact(request):
    contactForm = ContactForm
    context = {"contactForm": ContactForm}
    if request.method == "POST":
       contactForm = ContactForm(request.POST)
       if contactForm.is_valid:
           data = request.POST.copy()
           name =  data.get('name')
           email =  data.get('email')
           message = data.get('email_body') + " " + name + email
           destination = "testdjango123123@gmail.com"
           subject = "name: " + name + " email: " + email
           send_mail(subject, message, email, [destination])
           messages.add_message(request, messages.INFO, "contact succsess")
       else:
           messages.add_message(request, messages.INFO, "contact fail")
       return render(request, 'contact.html', context = context)
    else:
       return render(request, 'contact.html', context = context)
