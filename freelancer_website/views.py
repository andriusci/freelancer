from django.shortcuts import render, redirect, reverse

def index(request):
    #Return the index.html file
     return render(request, 'index.html')

