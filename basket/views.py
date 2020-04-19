from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def basket(request):

      return render(request, 'basket.html')

  