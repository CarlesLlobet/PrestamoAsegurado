from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def faq(request):
    return render(request, 'preguntasfrequentes.html')

def servicios(request):
    return render(request, 'servicios.html')

def empresa(request):
    return render(request, 'empresa.html')