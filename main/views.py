from django.shortcuts import render,redirect
from django.contrib.auth import logout

from . import models
from . import forms

# Create your views here.
def home(request):

    return render(request, 'home.html')
