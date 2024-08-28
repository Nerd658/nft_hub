from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil , name="acceuil"),
    path('contact', views.contact , name="contact"),
    path('connexion', views.connexion , name="connexion"),
    
    
]