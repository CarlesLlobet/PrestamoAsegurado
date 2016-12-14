from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate

from Web import forms


def index(request):
    if request.method=="POST":
        form = forms.formLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            passwd = form.cleaned_data['passwd']
            login = authenticate(username=user, password=passwd)
            if login is not None:
                if login.username == "opera":
                    return HttpResponseRedirect('/formularios')
                else:
                    return HttpResponseRedirect('/formularios') #TODO: Canviar pel lloc on van els users a penjar fotos
    return render(request, 'web_index.html')

def faq(request):
    return render(request, 'web_faq.html')

def servicios(request):
    return render(request, 'web_services.html')

def empresa(request):
    return render(request, 'web_empresa.html')