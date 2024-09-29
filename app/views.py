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
from django.contrib.auth.decorators import login_required
# Create your views here.

def acceuil (request) :
    return render(request, 'app/acceuil.html')


def contact (request) :
    return render (request, 'app/contact.html')

def connexion (request) :
    return render (request, 'compte/connexion.html')

@login_required
def form (request) :
    return render (request, 'app/form_wallet.html')