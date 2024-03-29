# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

from Web import forms

def index(request):
    context = {}
    logout(request)
    if request.method == "POST":
        form = forms.formLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            usr = authenticate(username=user, password=passwd)
            if usr is not None:
                if usr.is_active:
                    login(request, usr)
                    if user == "operadora":
                        return HttpResponseRedirect('/formularios')
                    else:
                        return HttpResponseRedirect('/formularios') #TODO: Canviar pel lloc on van els users a penjar fotos
            else:
                form = forms.formLogin()
                context.update({"incorrect": "incorrect"})
                context.update({"form": form})
                return render(request,'web_index.html', context)
    else:
        form = forms.formLogin()
        context.update({"form": form})
    return render(request, 'web_index.html', context)

def faq(request):
    context = {}
    logout(request)
    if request.method == "POST":
        form = forms.formLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            usr = authenticate(username=user, password=passwd)
            if usr is not None:
                if usr.is_active:
                    login(request, usr)
                    if user == "operadora":
                        return HttpResponseRedirect('/formularios')
                    else:
                        return HttpResponseRedirect(
                            '/formularios')  # TODO: Canviar pel lloc on van els users a penjar fotos
            else:
                form = forms.formLogin()
                context.update({"incorrect": "incorrect"})
                context.update({"form": form})
                return render(request, 'web_index.html', context)
    else:
        form = forms.formLogin()
        context.update({"form": form})
    return render(request, 'web_faq.html', context)

def servicios(request):
    context = {}
    logout(request)
    if request.method == "POST":
        form = forms.formLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            usr = authenticate(username=user, password=passwd)
            if usr is not None:
                if usr.is_active:
                    login(request, usr)
                    if user == "operadora":
                        return HttpResponseRedirect('/formularios')
                    else:
                        return HttpResponseRedirect(
                            '/formularios')  # TODO: Canviar pel lloc on van els users a penjar fotos
            else:
                form = forms.formLogin()
                context.update({"incorrect": "incorrect"})
                context.update({"form": form})
                return render(request, 'web_index.html', context)
    else:
        form = forms.formLogin()
        context.update({"form": form})
    return render(request, 'web_services.html', context)

def empresa(request):
    context = {}
    logout(request)
    if request.method == "POST":
        form = forms.formLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            usr = authenticate(username=user, password=passwd)
            if usr is not None:
                if usr.is_active:
                    login(request, usr)
                    if user == "operadora":
                        return HttpResponseRedirect('/formularios')
                    else:
                        return HttpResponseRedirect(
                            '/formularios')  # TODO: Canviar pel lloc on van els users a penjar fotos
            else:
                form = forms.formLogin()
                context.update({"incorrect": "incorrect"})
                context.update({"form": form})
                return render(request, 'web_index.html', context)
    else:
        form = forms.formLogin()
        context.update({"form": form})
    return render(request, 'web_empresa.html', context)

def politica(request):
    context = {}
    logout(request)
    if request.method == "POST":
        form = forms.formLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            usr = authenticate(username=user, password=passwd)
            if usr is not None:
                if usr.is_active:
                    login(request, usr)
                    if user == "operadora":
                        return HttpResponseRedirect('/formularios')
                    else:
                        return HttpResponseRedirect(
                            '/formularios')  # TODO: Canviar pel lloc on van els users a penjar fotos
            else:
                form = forms.formLogin()
                context.update({"incorrect": "incorrect"})
                context.update({"form": form})
                return render(request, 'web_index.html', context)
    else:
        form = forms.formLogin()
        context.update({"form": form})
    return render(request, 'web_politica.html', context)

def aviso(request):
    context = {}
    logout(request)
    if request.method == "POST":
        form = forms.formLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            usr = authenticate(username=user, password=passwd)
            if usr is not None:
                if usr.is_active:
                    login(request, usr)
                    if user == "operadora":
                        return HttpResponseRedirect('/formularios')
                    else:
                        return HttpResponseRedirect(
                            '/formularios')  # TODO: Canviar pel lloc on van els users a penjar fotos
            else:
                form = forms.formLogin()
                context.update({"incorrect": "incorrect"})
                context.update({"form": form})
                return render(request, 'web_index.html', context)
    else:
        form = forms.formLogin()
        context.update({"form": form})
    return render(request, 'web_aviso.html', context)

def gastos(request):
    context = {}
    logout(request)
    if request.method == "POST":
        form = forms.formLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            usr = authenticate(username=user, password=passwd)
            if usr is not None:
                if usr.is_active:
                    login(request, usr)
                    if user == "operadora":
                        return HttpResponseRedirect('/formularios')
                    else:
                        return HttpResponseRedirect(
                            '/formularios')  # TODO: Canviar pel lloc on van els users a penjar fotos
            else:
                form = forms.formLogin()
                context.update({"incorrect": "incorrect"})
                context.update({"form": form})
                return render(request, 'web_index.html', context)
    else:
        form = forms.formLogin()
        context.update({"form": form})
    return render(request, 'web_gastos.html', context)

def cookies(request):
    context = {}
    logout(request)
    if request.method == "POST":
        form = forms.formLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            usr = authenticate(username=user, password=passwd)
            if usr is not None:
                if usr.is_active:
                    login(request, usr)
                    if user == "operadora":
                        return HttpResponseRedirect('/formularios')
                    else:
                        return HttpResponseRedirect(
                            '/formularios')  # TODO: Canviar pel lloc on van els users a penjar fotos
            else:
                form = forms.formLogin()
                context.update({"incorrect": "incorrect"})
                context.update({"form": form})
                return render(request, 'web_index.html', context)
    else:
        form = forms.formLogin()
        context.update({"form": form})
    return render(request, 'web_cookies.html', context)