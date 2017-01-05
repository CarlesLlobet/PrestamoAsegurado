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
        message.Body = u'Acaba de crearse una cuenta. \n Su usuario sera ' + unicode(
            numexp) + u' y su contraseña' + unicode(
            person.dni) + u'\n Gracias por su atencion,\n\n Cordialmente, \n Prestamo Asegurado'
        sender = Mailer('localhost')
        sender.send(message)
        return HttpResponseRedirect('/formularios')
    else:
        expediente = models.expediente.objects.get(numexp=numexp)
        context.update({'expediente': expediente})

        persona = models.persona.objects.get(numexp=numexp, avalista=False)
        context.update({'persona': persona})

        personaanexos = models.personaanexos.objects.get(numexp=numexp, avalista=False)
        context.update({'personaanexos': personaanexos})

        juvilacion = models.juvilacion.objects.get(numexp=numexp, avalista=False)
        context.update({'juvilacion': juvilacion})

        paro = models.paro.objects.get(numexp=numexp, avalista=False)
        context.update({'paro': paro})

        empreses = []
        empresa = models.empresa.objects.all().filter(numexp=numexp, avalista=False)
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

        viviendas = []
        vivienda = models.vivienda.objects.all().filter(numexp=numexp, avalista=False)
        for t in vivienda:
            aux = {}
            aux['direccion'] = t.direccion
            aux['poblacion'] = t.poblacion
            aux['provincia'] = t.provincia
            aux['codigopostal'] = t.codigopostal
            aux['valorvivienda'] = t.valorvivienda
            aux['valorhipoteca'] = t.valorhipoteca
            aux['estapagada'] = t.estapagada
            aux['sinopagadaanos'] = t.sinopagadaanos
            aux['sinopagadaentidad'] = t.sinopagadaentidad
            aux['sinopagadapagahipoteca'] = t.sinopagadapagahipoteca
            aux['librecargos'] = t.librecargos
            aux['metros'] = t.metros
            aux['porciento'] = t.porciento
            aux['valoralquilada'] = t.valoralquilada
            aux['pagaalquiler'] = t.pagaalquiler
            aux['tipo'] = t.tipo
            viviendas.append(aux)
        context.update({'vivienda': viviendas})

        debecreditos = []
        debecredito = models.debecredito.objects.all().filter(numexp=numexp, avalista=False)
        for t in debecredito:
            aux = {}
            aux['tipo'] = t.tipo
            aux['porcientoavalista'] = t.porcientoavalista
            aux['importe'] = t.importe
            aux['cuota'] = t.cuota
            aux['entidad'] = t.entidad
            debecreditos.append(aux)
        context.update({'debecredito': debecreditos})

        debetarjetas = []
        debetarjeta = models.debetarjeta.objects.all().filter(numexp=numexp, avalista=False)
        for t in debetarjeta:
            aux = {}
            aux['cuota'] = t.cuota
            aux['importe'] = t.importe
            aux['entidad'] = t.entidad
            debetarjetas.append(aux)
        context.update({'debetarjeta': debetarjetas})

        deberecivoss = []
        deberecivos = models.deberecivos.objects.all().filter(numexp=numexp, avalista=False)
        for t in deberecivos:
            aux = {}
            aux['importe'] = t.importe
            deberecivoss.append(aux)
        context.update({'deberecivos': deberecivoss})

        debemorosos = []
        debemoroso = models.debemoroso.objects.all().filter(numexp=numexp, avalista=False)
        for t in debemoroso:
            aux = {}
            aux['importe'] = t.importe
            aux['quien'] = t.quien
            debemorosos.append(aux)
        context.update({'debemoroso': debemorosos})


        cochecito = models.coches.objects.get(numexp=numexp)
        context.update({'coches': cochecito})

        return render(request, 'form2_exped.html', context)

