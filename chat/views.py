from django.shortcuts import render
from chat.models import Chat
from chat.forms import ChatForm
from quote.models import Quote, QuoteFiles
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

def chat(request, quote_ref, file_name):
  #enables chat functionality
  #takes user input and saves it together with associated data such as relevant file name.
  if request.method == "POST":
      current_user = request.user
      user = current_user.username
      form = ChatForm(request.POST)
      if form.is_valid:
           message = request.POST.get('message')
           quote_ref = request.POST.get('quote_ref')
           file_name = request.POST.get('file_name')
           
           #ckeck if user is freelancer (used in the chat to align messages to left or right)
          
           if request.user.is_superuser:
             superuser = True
             quote = Quote.objects.get(id = quote_ref)
             user = quote.submitted_by
           else:
             superuser = False
             user = user

           chat_instance = Chat(message = message,
                           quote_ref = quote_ref,
                           file_name = file_name,
                           user = user,
                           superuser = superuser )
                     
           chat_instance.save()
      if not request.user.is_superuser:
         quote_file = QuoteFiles.objects.get(quote_ref = quote_ref, file_name = file_name)                              
         quote_file.status = "Pending"
         quote_file.save() 
      return redirect(reverse('chat', args=(quote_ref, file_name)))

  else:
     html = "<html><body> The page you are trying to access does not exist.</body></html>" 
     return HttpResponse(html)