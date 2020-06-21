from django.shortcuts import render
from chat.models import Chat
from chat.forms import ChatForm
from quote.models import Quote, QuoteFiles
from django.shortcuts import render, redirect, reverse

def chat(request):
  if request.method == "POST":
     
      current_user = request.user
      user = current_user.username

      form = ChatForm(request.POST)
      if form.is_valid:
           message = request.POST.get('message')
           quote_ref = request.POST.get('quote_ref')
           file_name = request.POST.get('file_name')
           
          
           if request.user.is_superuser:
             superuser = True
             quote = Quote.objects.get(id = quote_ref)
             user = quote.submitted_by
           else:
             superuser = False
             user = user
             #change file status to pending
          
           chat_instance = Chat(message = message,
                           quote_ref = quote_ref,
                           file_name = file_name,
                           user = user,
                           superuser = superuser )
                     
      chat_instance.save()

      quote_file = QuoteFiles.objects.get(quote_ref = quote_ref, file_name = file_name)                              
      quote_file.status = "Pending"
      quote_file.save() 
      return redirect(reverse('reupload', args=(quote_ref, file_name)))