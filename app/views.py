from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re
from django.db.models import Q
def acceuil (request) :
    return render(request, 'app/acceuil.html')
# Create your views here.

def contact (request) :
    return render (request, 'app/contact.html')

def connexion (request) :
    return render (request, 'compte/connexion.html')
