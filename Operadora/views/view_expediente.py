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
        expedient = models.expediente.objects.get(numexp=numexp)
        if expedient.tipo == "Personal":
            # TODO: Pillar les dades necessaries per aquest tipus
            empreses_seves = models.empresa.objects.get(numexp=numexp)
            # TODO: Ficarla al context
            context.update({'numexp', expedient.numexp})
            context.update({'hora', expedient.datayhora})
            i = 0
            for e in empreses_seves:
                context.update({'nomempresa' + i, e.nombre})
                context.update({'nomempresa' + i, e.cargo})
                i += 1
        elif expedient.tipo == "Hipotecario":
            # TODO: Pillar les dades necessaries per aquest tipus
            empreses_seves = models.empresa.objects.get(numexp=numexp)
            # TODO: Ficarla al context
            context.update({'numexp', expedient.numexp})
            context.update({'hora', expedient.datayhora})
            i = 0
            for e in empreses_seves:
                context.update({'nomempresa' + i, e.nombre})
                context.update({'nomempresa' + i, e.cargo})
                i += 1
        elif expedient.tipo == "Microcredito":
            # TODO: Pillar les dades necessaries per aquest tipus
            empreses_seves = models.empresa.objects.get(numexp=numexp)
            # TODO: Ficarla al context
            context.update({'numexp', expedient.numexp})
            context.update({'hora', expedient.datayhora})
            i = 0
            for e in empreses_seves:
                context.update({'nomempresa' + i, e.nombre})
                context.update({'nomempresa' + i, e.cargo})
                i += 1
        elif expedient.tipo == "Coche":
            # TODO: Pillar les dades necessaries per aquest tipus
            empreses_seves = models.empresa.objects.get(numexp=numexp)
            # TODO: Ficarla al context
            context.update({'numexp', expedient.numexp})
            context.update({'hora', expedient.datayhora})
            i = 0
            for e in empreses_seves:
                context.update({'nomempresa' + i, e.nombre})
                context.update({'nomempresa' + i, e.cargo})
                i += 1
        return render(request, 'form2_exped.html', context)

