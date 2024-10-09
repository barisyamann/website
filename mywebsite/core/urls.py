# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('ayazjam/', views.ayazjam, name='ayazjam'),
    path('robo-x/', views.robox, name='robox'),
    path('acmix/', views.acmix, name='acmix'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('acm-nedir/', views.acm_nedir, name='acm_nedir'),
    path('contact/', views.contact, name='contact'),
]
