# core/views.py
from django.shortcuts import render
from .models import Duyuru
def homepage(request):
    return render(request, 'core/AnaSayfa.html')

def ayazjam(request):
    return render(request, 'core/AyazJam.html')

def robox(request):
    return render(request, 'core/Robo-X.html')

def acmix(request):
    return render(request, 'core/ACMiX.html')

def sponsor(request):
    return render(request, 'core/Sponsor.html')

def acm_nedir(request):
    return render(request, 'core/ACM-Nedir.html')

def contact(request):
    return render(request, 'core/Contact.html')
def homepage(request):
    duyurular = Duyuru.objects.all()  # Tüm duyuruları al
    return render(request, 'core/AnaSayfa.html', {'duyurular': duyurular})