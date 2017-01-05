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
def expediente(request, numexp):
    context = {}
    if request.method == 'POST':
        person = models.persona.objects.get(numexp=numexp)
        user = User.objects.create_user(numexp, person.email, person.dni)
        user.save()
        g = Group.objects.get(name='Clients')
        g.user_set.add(user)
        message = Message(From="prestamo@noreply.com",
                          To=[person.email],
                          Subject=u'Nueva cuenta en Prestamo Asegurado')
        message.Body = u'Acaba de crearse una cuenta para que pueda enviarnos las fotos de ... \n Su usuario sera ' + unicode(
            numexp) + u' y su contraseña' + unicode(
            person.dni) + u'\n Gracias por su atencion,\n\n Cordialmente, \n Prestamo Asegurado'
        sender = Mailer('localhost')
        sender.send(message)
        return HttpResponseRedirect('/formularios')
    else:
        expediente = models.expediente.objects.get(numexp=numexp)
        persona = models.persona.objects.get(numexp=numexp, avalista=False)
        context.update({'expediente': expediente})
        context.update({'persona': persona})
        empreses = []
        empresa = models.empresa.objects.all(numexp=numexp, avalista=False)
        for t in empresa:
            aux = {}
            aux['nombre'] = t.nombre
            aux['cargo'] = t.cargo
            aux['actividad'] = t.actividad
            aux['ingresos'] = t.ingresos
            aux['pagas'] = t.pagas
            aux['otrosingresos'] = t.otrosingresos
            aux['antiguedad'] = t.antiguedad
            empreses.append(aux)
        context.update({'empresa': empreses})

        return render(request, 'form2_exped.html', context)

