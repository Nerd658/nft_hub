from django.shortcuts import render

def acceuil (request) :
    return render(request, 'app/acceuil.html')
# Create your views here.
