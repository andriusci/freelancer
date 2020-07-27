from django.shortcuts import render
from chat.models import Chat
from chat.forms import ChatForm
from quote.models import Quote, QuoteFiles
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from quote.forms import  QuoteUploadForm, UploadFileForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def chat(request, quote_ref, file_name):

  current_user = request.user
  user = current_user.username

  uploadForm = UploadFileForm
  chatForm = ChatForm

  if request.user.is_superuser:
        quote = Quote.objects.get(id = quote_ref)
        user = quote.submitted_by
  try:
        quote_file = QuoteFiles.objects.get(file_name = file_name, quote_ref = quote_ref, user = user)
  except:
        html = "<html><body> <h1>The page you are looking for does not exist</h1>.</body></html>" 
        return HttpResponse(html)
  else:
        chat = Chat.objects.all().filter(user = user, quote_ref = quote_ref, file_name = file_name)
        context = {"quote_ref": quote_ref,"file_name": file_name, "uploadForm": uploadForm, "chatForm": chatForm, "chat":chat }
        return render(request, 'chat.html', context = context)

def chat_send(request):
  if request.method == "POST":
      uploadForm = UploadFileForm
      chatForm = ChatForm

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
           
           #create the chat object 
           chat_instance = Chat(message = message,
                           quote_ref = quote_ref,
                           file_name = file_name,
                           user = user,
                           superuser = superuser )
           chat_instance.save()

      #if the chat message is send by the customer, change the file status to pending
      if not request.user.is_superuser:
         quote_file = QuoteFiles.objects.get(quote_ref = quote_ref, file_name = file_name)                              
         quote_file.status = "Pending"
         quote_file.save() 
      else:
         quote = Quote.objects.get(id = quote_ref)
         user = quote.submitted_by

      chat = Chat.objects.all().filter(user = user, quote_ref = quote_ref, file_name = file_name)
      context = {"quote_ref": quote_ref,"file_name": file_name, "uploadForm": uploadForm, "chatForm": chatForm, "chat":chat }
      return render(request, 'chat.html', context = context)
  else:
    html = "<html><body><h1>The page you are looking for does not exist</h1></html>" 
    return HttpResponse(html)