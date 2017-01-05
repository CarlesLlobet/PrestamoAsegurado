# -*- coding: utf-8 -*-
from datetime import datetime

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from mailer import Mailer, Message

from Operadora import forms
from Operadora import models


def group_check(user):
    return user.groups.filter(name__in=['Operadoras'])


@login_required(login_url="/")
@user_passes_test(group_check)
def index(request):
    # context = {}
    # if request.method == 'POST':
    #    form = forms.formBuscar(request.POST)
    #    if form.is_valid():
    #        numexp = form.cleaned_data['numexp']
    #        dni = form.cleaned_data['dni']
    #        if 'numexp' in request.POST:
    #            expedient = models.expediente.objects.get(numexp=numexp)
    #        elif 'dni' in request.POST:
    #            expedient = models.expediente.objects.get(dni=dni)
    #        return HttpResponseRedirect('/expediente/' + expedient.numexp)
    # else:
    #    form = forms.formBuscar()
    #    context.update({"form": form})
    lastNum2 = models.expediente.objects.all().order_by("numexp").last()
    lastNum = 0
    if not lastNum2:
        lastNum = 40000
    else:
        lastNum = lastNum2.numexp + 1
    models.expediente.objects.create(numexp=lastNum, tipo="None")
    return render(request, 'form_index.html', {'numexp': lastNum})



@login_required(login_url="/")
@user_passes_test(group_check)
def send(request):
    return render(request, 'form_send.html', )



