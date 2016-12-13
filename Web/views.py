from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'web_index.html')

def faq(request):
    return render(request, 'web_faq.html')

def servicios(request):
    return render(request, 'web_services.html')

def empresa(request):
    return render(request, 'web_empresa.html')