# -*- coding: utf-8 -*-
from datetime import datetime

from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render

from Operadora import forms
from Operadora import models

from mailer import Mailer, Message


def index(request):
    context = {}
    if request.method == 'POST':
        form = forms.formBuscar(request.POST)
        if form.is_valid():
            numexp = form.cleaned_data['numexp']
            dni = form.cleaned_data['dni']
            if 'numexp' in request.POST:
                expedient = models.expediente.objects.get(numexp=numexp)
            elif 'dni' in request.POST:
                expedient = models.expediente.objects.get(dni=dni)
            return HttpResponseRedirect('/expediente/' + expedient.numexp)
    else:
        form = forms.formBuscar()
        context.update({"form": form})
        return render(request, 'form_index.html', context)


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


def asnef(request):
    context = {}
    return render(request, 'form_asnef.html', context)


def coche(request):
    context = {}
    if request.method == 'POST':
        form = forms.formCoche(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dni = form.cleaned_data['dni']
            direccion = form.cleaned_data['direccion']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            movil = form.cleaned_data['movil']
            fechanacimiento = form.cleaned_data['fechanacimiento']
            nacionalidad = form.cleaned_data['nacionalidad']
            estadocivil = form.cleaned_data['estadocivil']
            tipocasado = form.cleaned_data['tipocasado']
            numerohijos = form.cleaned_data['numerohijos']
            mayoresdeedad = form.cleaned_data['mayoresdeedad']
            cuantosacargo = form.cleaned_data['cuantosacargo']
            ingresohijos = form.cleaned_data['ingresohijos']
            anotacionespersonales = form.cleaned_data['anotacionespersonales']
            cotizacion = form.cleaned_data['cotizacion']
            tipotrabajo = form.cleaned_data['tipotrabajo']
            finalizacontrato = form.cleaned_data['finalizacontrato']
            nombreempresa1 = form.cleaned_data['nombreempresa1']
            cargoempresa1 = form.cleaned_data['cargoempresa1']
            actividadempresa1 = form.cleaned_data['actividadempresa1']
            ingresosempresa1 = form.cleaned_data['ingresosempresa1']
            pagasempresa1 = form.cleaned_data['pagasempresa1']
            otrosingresosempresa1 = form.cleaned_data['otrosingresosempresa1']
            antiguedadempresa1 = form.cleaned_data['antiguedadempresa1']
            nombreempresa2 = form.cleaned_data['nombreempresa2']
            cargoempresa2 = form.cleaned_data['cargoempresa2']
            actividadempresa2 = form.cleaned_data['actividadempresa2']
            ingresosempresa2 = form.cleaned_data['ingresosempresa2']
            pagasempresa2 = form.cleaned_data['pagasempresa2']
            otrosingresosempresa2 = form.cleaned_data['otrosingresosempresa2']
            antiguedadempresa2 = form.cleaned_data['antiguedadempresa2']
            nombreempresa3 = form.cleaned_data['nombreempresa3']
            cargoempresa3 = form.cleaned_data['cargoempresa3']
            actividadempresa3 = form.cleaned_data['actividadempresa3']
            ingresosempresa3 = form.cleaned_data['ingresosempresa3']
            pagasempresa3 = form.cleaned_data['pagasempresa3']
            otrosingresosempresa3 = form.cleaned_data['otrosingresosempresa3']
            antiguedadempresa3 = form.cleaned_data['antiguedadempresa3']
            importejuvilacion = form.cleaned_data['importejuvilacion']
            numerodepagasjuvilacion = form.cleaned_data['numerodepagasjuvilacion']
            iniciojuvilacion = form.cleaned_data['iniciojuvilacion']
            finjuvilacion = form.cleaned_data['finjuvilacion']
            parodesdecuando = form.cleaned_data['parodesdecuando']
            parocuantocobra = form.cleaned_data['parocuantocobra']
            otrosingresos = form.cleaned_data['otrosingresos']
            otrosgastos = form.cleaned_data['otrosgastos']
            otrosingresostexto = form.cleaned_data['otrosingresostexto']
            otrosgastostexto = form.cleaned_data['otrosgastostexto']
            anotacionesingresos = form.cleaned_data['anotacionesingresos']
            viviendavalor1 = form.cleaned_data['viviendavalor1']
            viviendavalorhipoteca1 = form.cleaned_data['viviendavalorhipoteca1']
            viviendaestapagada1 = form.cleaned_data['viviendaestapagada1']
            viviendalibredecargos1 = form.cleaned_data['viviendalibredecargos1']
            viviendacuotamensual1 = form.cleaned_data['viviendacuotamensual1']
            viviendaanos1 = form.cleaned_data['viviendaanos1']
            viviendaentidad1 = form.cleaned_data['viviendaentidad1']
            viviendametros1 = form.cleaned_data['viviendametros1']
            viviendaporciento1 = form.cleaned_data['viviendaporciento1']
            viviendadireccion1 = form.cleaned_data['viviendadireccion1']
            viviendapoblacion1 = form.cleaned_data['viviendapoblacion1']
            viviendaprovincia1 = form.cleaned_data['viviendaprovincia1']
            viviendacodigopostal1 = form.cleaned_data['viviendacodigopostal1']
            viviendavalor2 = form.cleaned_data['viviendavalor2']
            viviendavalorhipoteca2 = form.cleaned_data['viviendavalorhipoteca2']
            viviendaestapagada2 = form.cleaned_data['viviendaestapagada2']
            viviendalibredecargos2 = form.cleaned_data['viviendalibredecargos2']
            viviendacuotamensual2 = form.cleaned_data['viviendacuotamensual2']
            viviendaanos2 = form.cleaned_data['viviendaanos2']
            viviendaentidad2 = form.cleaned_data['viviendaentidad2']
            viviendametros2 = form.cleaned_data['viviendametros2']
            viviendaporciento2 = form.cleaned_data['viviendaporciento2']
            viviendadireccion2 = form.cleaned_data['viviendadireccion2']
            viviendapoblacion2 = form.cleaned_data['viviendapoblacion2']
            viviendaprovincia2 = form.cleaned_data['viviendaprovincia2']
            viviendacodigopostal2 = form.cleaned_data['viviendacodigopostal2']
            viviendavalor3 = form.cleaned_data['viviendavalor3']
            viviendavalorhipoteca3 = form.cleaned_data['viviendavalorhipoteca3']
            viviendaestapagada3 = form.cleaned_data['viviendaestapagada3']
            viviendalibredecargos3 = form.cleaned_data['viviendalibredecargos3']
            viviendacuotamensual3 = form.cleaned_data['viviendacuotamensual3']
            viviendaanos3 = form.cleaned_data['viviendaanos3']
            viviendaentidad3 = form.cleaned_data['viviendaentidad3']
            viviendametros3 = form.cleaned_data['viviendametros3']
            viviendaporciento3 = form.cleaned_data['viviendaporciento3']
            viviendadireccion3 = form.cleaned_data['viviendadireccion3']
            viviendapoblacion3 = form.cleaned_data['viviendapoblacion3']
            viviendaprovincia3 = form.cleaned_data['viviendaprovincia3']
            viviendacodigopostal3 = form.cleaned_data['viviendacodigopostal3']
            viviendaalquiladavalor1 = form.cleaned_data['viviendaalquiladavalor1']
            viviendaalquiladavalorhipoteca1 = form.cleaned_data['viviendaalquiladavalorhipoteca1']
            viviendaalquiladaestapagada1 = form.cleaned_data['viviendaalquiladaestapagada1']
            viviendaalquiladalibredecargos1 = form.cleaned_data['viviendaalquiladalibredecargos1']
            viviendaalquiladacuotamensual1 = form.cleaned_data['viviendaalquiladacuotamensual1']
            viviendaalquiladaanos1 = form.cleaned_data['viviendaalquiladaanos1']
            viviendaalquiladaentidad1 = form.cleaned_data['viviendaalquiladaentidad1']
            viviendaalquiladametros1 = form.cleaned_data['viviendaalquiladametros1']
            viviendaalquiladaporciento1 = form.cleaned_data['viviendaalquiladaporciento1']
            viviendaalquiladadireccion1 = form.cleaned_data['viviendaalquiladadireccion1']
            viviendaalquiladapoblacion1 = form.cleaned_data['viviendaalquiladapoblacion1']
            viviendaalquiladaprovincia1 = form.cleaned_data['viviendaalquiladaprovincia1']
            viviendaalquiladacodigopostal1 = form.cleaned_data['viviendaalquiladacodigopostal1']
            viviendaalquiladacobraalquiler1 = form.cleaned_data['viviendaalquiladacobraalquiler1']
            viviendaalquiladavalor2 = form.cleaned_data['viviendaalquiladavalor2']
            viviendaalquiladavalorhipoteca2 = form.cleaned_data['viviendaalquiladavalorhipoteca2']
            viviendaalquiladaestapagada2 = form.cleaned_data['viviendaalquiladaestapagada2']
            viviendaalquiladalibredecargos2 = form.cleaned_data['viviendaalquiladalibredecargos2']
            viviendaalquiladacuotamensual2 = form.cleaned_data['viviendaalquiladacuotamensual2']
            viviendaalquiladaanos2 = form.cleaned_data['viviendaalquiladaanos2']
            viviendaalquiladaentidad2 = form.cleaned_data['viviendaalquiladaentidad2']
            viviendaalquiladametros2 = form.cleaned_data['viviendaalquiladametros2']
            viviendaalquiladaporciento2 = form.cleaned_data['viviendaalquiladaporciento2']
            viviendaalquiladadireccion2 = form.cleaned_data['viviendaalquiladadireccion2']
            viviendaalquiladapoblacion2 = form.cleaned_data['viviendaalquiladapoblacion2']
            viviendaalquiladaprovincia2 = form.cleaned_data['viviendaalquiladaprovincia2']
            viviendaalquiladacodigopostal2 = form.cleaned_data['viviendaalquiladacodigopostal2']
            viviendaalquiladacobraalquiler2 = form.cleaned_data['viviendaalquiladacobraalquiler2']
            viviendaalquiladavalor3 = form.cleaned_data['viviendaalquiladavalor3']
            viviendaalquiladavalorhipoteca3 = form.cleaned_data['viviendaalquiladavalorhipoteca3']
            viviendaalquiladaestapagada3 = form.cleaned_data['viviendaalquiladaestapagada3']
            viviendaalquiladalibredecargos3 = form.cleaned_data['viviendaalquiladalibredecargos3']
            viviendaalquiladacuotamensual3 = form.cleaned_data['viviendaalquiladacuotamensual3']
            viviendaalquiladaanos3 = form.cleaned_data['viviendaalquiladaanos3']
            viviendaalquiladaentidad3 = form.cleaned_data['viviendaalquiladaentidad3']
            viviendaalquiladametros3 = form.cleaned_data['viviendaalquiladametros3']
            viviendaalquiladaporciento3 = form.cleaned_data['viviendaalquiladaporciento3']
            viviendaalquiladadireccion3 = form.cleaned_data['viviendaalquiladadireccion3']
            viviendaalquiladapoblacion3 = form.cleaned_data['viviendaalquiladapoblacion3']
            viviendaalquiladaprovincia3 = form.cleaned_data['viviendaalquiladaprovincia3']
            viviendaalquiladacodigopostal3 = form.cleaned_data['viviendaalquiladacodigopostal3']
            viviendaalquiladacobraalquiler3 = form.cleaned_data['viviendaalquiladacobraalquiler3']
            alquilerpaga1 = form.cleaned_data['alquilerpaga1']
            alquilermetros1 = form.cleaned_data['alquilermetros1']
            alquilerdireccion1 = form.cleaned_data['alquilerdireccion1']
            alquilerpoblacion1 = form.cleaned_data['alquilerpoblacion1']
            alquilerprovincia1 = form.cleaned_data['alquilerprovincia1']
            alquilercodigopostal1 = form.cleaned_data['alquilercodigopostal1']
            alquilerpaga2 = form.cleaned_data['alquilerpaga2']
            alquilermetros2 = form.cleaned_data['alquilermetros2']
            alquilerdireccion2 = form.cleaned_data['alquilerdireccion2']
            alquilerpoblacion2 = form.cleaned_data['alquilerpoblacion2']
            alquilerprovincia2 = form.cleaned_data['alquilerprovincia2']
            alquilercodigopostal2 = form.cleaned_data['alquilercodigopostal2']
            alquilerpaga3 = form.cleaned_data['alquilerpaga3']
            alquilermetros3 = form.cleaned_data['alquilermetros3']
            alquilerdireccion3 = form.cleaned_data['alquilerdireccion3']
            alquilerpoblacion3 = form.cleaned_data['alquilerpoblacion3']
            alquilerprovincia3 = form.cleaned_data['alquilerprovincia3']
            alquilercodigopostal3 = form.cleaned_data['alquilercodigopostal3']
            direccionpersonal = form.cleaned_data['direccionpersonal']
            poblacionpersonal = form.cleaned_data['poblacionpersonal']
            provinciapersonal = form.cleaned_data['provinciapersonal']
            codigopostalpersonal = form.cleaned_data['codigopostalpersonal']
            anotacionesviviendas = form.cleaned_data['anotacionesviviendas']
            creditotipo1 = form.cleaned_data['creditotipo1']
            creditotantoporciento1 = form.cleaned_data['creditotantoporciento1']
            creditoimporte1 = form.cleaned_data['creditoimporte1']
            creditocuota1 = form.cleaned_data['creditocuota1']
            creditoentidad1 = form.cleaned_data['creditoentidad1']
            creditotipo2 = form.cleaned_data['creditotipo2']
            creditotantoporciento2 = form.cleaned_data['creditotantoporciento2']
            creditoimporte2 = form.cleaned_data['creditoimporte2']
            creditocuota2 = form.cleaned_data['creditocuota2']
            creditoentidad2 = form.cleaned_data['creditoentidad2']
            creditotipo3 = form.cleaned_data['creditotipo3']
            creditotantoporciento3 = form.cleaned_data['creditotantoporciento3']
            creditoimporte3 = form.cleaned_data['creditoimporte3']
            creditocuota3 = form.cleaned_data['creditocuota3']
            creditoentidad3 = form.cleaned_data['creditoentidad3']
            tarjetacuota1 = form.cleaned_data['tarjetacuota1']
            tarjetaimporte1 = form.cleaned_data['tarjetaimporte1']
            tarjetaentidad1 = form.cleaned_data['tarjetaentidad1']
            tarjetacuota2 = form.cleaned_data['tarjetacuota2']
            tarjetaimporte2 = form.cleaned_data['tarjetaimporte2']
            tarjetaentidad2 = form.cleaned_data['tarjetaentidad2']
            tarjetacuota3 = form.cleaned_data['tarjetacuota3']
            tarjetaimporte3 = form.cleaned_data['tarjetaimporte3']
            tarjetaentidad3 = form.cleaned_data['tarjetaentidad3']
            recivosimporte1 = form.cleaned_data['recivosimporte1']
            recivosimporte2 = form.cleaned_data['recivosimporte2']
            recivosimporte3 = form.cleaned_data['recivosimporte3']
            morosoimporte1 = form.cleaned_data['morosoimporte1']
            morosoquien1 = form.cleaned_data['morosoquien1']
            morosoimporte2 = form.cleaned_data['morosoimporte2']
            morosoquien2 = form.cleaned_data['morosoquien2']
            morosoimporte3 = form.cleaned_data['morosoimporte3']
            morosoquien3 = form.cleaned_data['morosoquien3']
            anotacionesfinancieras = form.cleaned_data['anotacionesfinancieras']
            motor = form.cleaned_data['motor']
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            antiguedad = form.cleaned_data['antiguedad']
            matricula = form.cleaned_data['matricula']
            estadovehiculo = form.cleaned_data['estadovehiculo']
            anotacionescoche = form.cleaned_data['anotacionescoche']
            metodopago = form.cleaned_data['metodopago']
            anotacionesdestinado = form.cleaned_data['anotacionesdestinado']
            justificante = form.cleaned_data['justificante']
            autorizacion = form.cleaned_data['autorizacion']
            medio = form.cleaned_data['medio']
            numexp = form.cleaned_data['numexp']
            datayhora = form.cleaned_data['datayhora']

            expedient = models.expediente.objects.create(numexp=numexp, tipo="Coche", fecha_hora=datayhora)
            persona = models.persona.objects.create(numexp=numexp, nombre=name, dni=dni, direccion=direccion,
                                                    email=email, telefono=telefono, movil=movil,
                                                    fechanacimiento=fechanacimiento,
                                                    nacionalidad=nacionalidad, estadocivil=estadocivil,
                                                    tipocasado=tipocasado, numerodehijos=numerohijos,
                                                    sihijosmayores18=mayoresdeedad, sihijoscuantoscargo=cuantosacargo,
                                                    sihijosingreso=ingresohijos, justificante=justificante,
                                                    autoriza=autorizacion, medio=medio, metodopago=metodopago)
            personaanexos = models.personaanexos.objects.create(numexp=numexp, seguridadsocial=cotizacion,
                                                                siajenatipo=tipotrabajo,
                                                                siajenatemporal=finalizacontrato,
                                                                otrosingresos=otrosingresos,
                                                                otrosingresostexto=otrosingresostexto,
                                                                otrosgastos=otrosgastos,
                                                                otrosgastostexto=otrosgastostexto)
            paro = models.paro.objectos.create(numexp=numexp, desdecuando=parodesdecuando, cobra=parocuantocobra)
            juvilacion = models.juvilacion.objetos.create(numexp, importe=importejuvilacion,
                                                          pagas=numerodepagasjuvilacion, fechainicio=iniciojuvilacion,
                                                          fechafin=finjuvilacion)
            anotaciones = models.anotaciones.objects.create(numexp=numexp, personales=anotacionespersonales,
                                                            empresa=anotacionesingresos, vivienda=anotacionesviviendas,
                                                            financieros=anotacionesfinancieras,
                                                            destinado=anotacionesdestinado, coche=anotacionescoche)
            coches = models.coches.objects.create(numexp=numexp, motor=motor, marca=marca, modelo=modelo,
                                                  antiguedad=antiguedad, matricula=matricula,
                                                  estadodelvehiculo=estadovehiculo)

            if viviendadireccion1:
                vivienda = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion1,
                                                          poblacion=viviendapoblacion1, provincia=viviendaprovincia1,
                                                          codigopostal=viviendacodigopostal1,
                                                          valorvivienda=viviendavalor1,
                                                          valorhipoteca=viviendavalorhipoteca1,
                                                          estapagada=viviendaestapagada1, sinopagadaanos=viviendaanos1,
                                                          sinopagadaentidad=viviendaentidad1,
                                                          sinopagadapagahipoteca=viviendacuotamensual1,
                                                          librecargos=viviendalibredecargos1, metros=viviendametros1,
                                                          porciento=viviendaporciento1)

            if viviendadireccion2:
                vivienda2 = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion2,
                                                           poblacion=viviendapoblacion2, provincia=viviendaprovincia2,
                                                           codigopostal=viviendacodigopostal2,
                                                           valorvivienda=viviendavalor2,
                                                           valorhipoteca=viviendavalorhipoteca2,
                                                           estapagada=viviendaestapagada2, sinopagadaanos=viviendaanos2,
                                                           sinopagadaentidad=viviendaentidad2,
                                                           sinopagadapagahipoteca=viviendacuotamensual2,
                                                           librecargos=viviendalibredecargos2, metros=viviendametros2,
                                                           porciento=viviendaporciento2)

            if viviendadireccion3:
                vivienda3 = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion3,
                                                           poblacion=viviendapoblacion3, provincia=viviendaprovincia3,
                                                           codigopostal=viviendacodigopostal3,
                                                           valorvivienda=viviendavalor3,
                                                           valorhipoteca=viviendavalorhipoteca3,
                                                           estapagada=viviendaestapagada3, sinopagadaanos=viviendaanos3,
                                                           sinopagadaentidad=viviendaentidad3,
                                                           sinopagadapagahipoteca=viviendacuotamensual3,
                                                           librecargos=viviendalibredecargos3, metros=viviendametros3,
                                                           porciento=viviendaporciento3)

            if viviendaalquiladadireccion1:
                viviendaalquilada = models.vivienda.objects.create(numexp=numexp, direccion=viviendaalquiladadireccion1,
                                                                   poblacion=viviendaalquiladapoblacion1,
                                                                   provincia=viviendaalquiladaprovincia1,
                                                                   codigopostal=viviendaalquiladacodigopostal1,
                                                                   valorvivienda=viviendaalquiladavalor1,
                                                                   valorhipoteca=viviendaalquiladavalorhipoteca1,
                                                                   estapagada=viviendaalquiladaestapagada1,
                                                                   sinopagadaanos=viviendaalquiladaanos1,
                                                                   sinopagadaentidad=viviendaalquiladaentidad1,
                                                                   librecargos=viviendaalquiladalibredecargos1,
                                                                   metros=viviendaalquiladametros1,
                                                                   porciento=viviendaalquiladaporciento1,
                                                                   valoralquilada=viviendaalquiladacobraalquiler1,
                                                                   sinopagadapagahipoteca=viviendaalquiladacuotamensual1)

            if viviendaalquiladadireccion2:
                viviendaalquilada2 = models.vivienda.objects.create(numexp=numexp,
                                                                    direccion=viviendaalquiladadireccion2,
                                                                    poblacion=viviendaalquiladapoblacion2,
                                                                    provincia=viviendaalquiladaprovincia2,
                                                                    codigopostal=viviendaalquiladacodigopostal2,
                                                                    valorvivienda=viviendaalquiladavalor2,
                                                                    valorhipoteca=viviendaalquiladavalorhipoteca2,
                                                                    estapagada=viviendaalquiladaestapagada2,
                                                                    sinopagadaanos=viviendaalquiladaanos2,
                                                                    sinopagadaentidad=viviendaalquiladaentidad2,
                                                                    librecargos=viviendaalquiladalibredecargos2,
                                                                    metros=viviendaalquiladametros2,
                                                                    porciento=viviendaalquiladaporciento2,
                                                                    valoralquilada=viviendaalquiladacobraalquiler2,
                                                                    sinopagadapagahipoteca=viviendaalquiladacuotamensual2)

            if viviendaalquiladadireccion3:
                viviendaalquilada3 = models.vivienda.objects.create(numexp=numexp,
                                                                    direccion=viviendaalquiladadireccion3,
                                                                    poblacion=viviendaalquiladapoblacion3,
                                                                    provincia=viviendaalquiladaprovincia3,
                                                                    codigopostal=viviendaalquiladacodigopostal3,
                                                                    valorvivienda=viviendaalquiladavalor3,
                                                                    valorhipoteca=viviendaalquiladavalorhipoteca3,
                                                                    estapagada=viviendaalquiladaestapagada3,
                                                                    sinopagadaanos=viviendaalquiladaanos3,
                                                                    sinopagadaentidad=viviendaalquiladaentidad3,
                                                                    librecargos=viviendaalquiladalibredecargos3,
                                                                    metros=viviendaalquiladametros3,
                                                                    porciento=viviendaalquiladaporciento3,
                                                                    valoralquilada=viviendaalquiladacobraalquiler3,
                                                                    sinopagadapagahipoteca=viviendaalquiladacuotamensual3)

            if alquilerdireccion1:
                alquiler = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion1,
                                                          poblacion=alquilerpoblacion1, provincia=alquilerprovincia1,
                                                          codigopostal=alquilercodigopostal1, metros=alquilermetros1,
                                                          pagaalquiler=alquilerpaga1)

            if alquilerdireccion2:
                alquiler2 = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion2,
                                                           poblacion=alquilerpoblacion2, provincia=alquilerprovincia2,
                                                           codigopostal=alquilercodigopostal2, metros=alquilermetros2,
                                                           pagaalquiler=alquilerpaga2)

            if alquilerdireccion3:
                alquiler3 = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion3,
                                                           poblacion=alquilerpoblacion3, provincia=alquilerprovincia3,
                                                           codigopostal=alquilercodigopostal3, metros=alquilermetros3,
                                                           pagaalquiler=alquilerpaga3)

            if direccionpersonal:
                vivienda = models.vivienda.objects.create(numexp=numexp, direccion=direccionpersonal,
                                                          poblacion=poblacionpersonal, provincia=provinciapersonal,
                                                          codigopostal=codigopostalpersonal)

            if nombreempresa1:
                empresa = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa1, cargo=cargoempresa1,
                                                        actividad=actividadempresa1, ingresos=ingresosempresa1,
                                                        pagas=pagasempresa1, otrosingresos=otrosingresosempresa1,
                                                        antiguedad=antiguedadempresa1)

            if nombreempresa2:
                empresa2 = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa2, cargo=cargoempresa2,
                                                         actividad=actividadempresa2, ingresos=ingresosempresa2,
                                                         pagas=pagasempresa2, otrosingresos=otrosingresosempresa2,
                                                         antiguedad=antiguedadempresa2)

            if nombreempresa3:
                empresa3 = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa3, cargo=cargoempresa3,
                                                         actividad=actividadempresa3, ingresos=ingresosempresa3,
                                                         pagas=pagasempresa3, otrosingresos=otrosingresosempresa3,
                                                         antiguedad=antiguedadempresa3)

            if creditotipo1:
                debecredito1 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo1,
                                                                 porcientoavalista=creditotantoporciento1,
                                                                 importe=creditoimporte1, cuota=creditocuota1,
                                                                 entidad=creditoentidad1)
            if creditotipo2:
                debecredito2 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo2,
                                                                 porcientoavalista=creditotantoporciento2,
                                                                 importe=creditoimporte2, cuota=creditocuota2,
                                                                 entidad=creditoentidad2)
            if creditotipo3:
                debecredito3 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo3,
                                                                 porcientoavalista=creditotantoporciento3,
                                                                 importe=creditoimporte3, cuota=creditocuota3,
                                                                 entidad=creditoentidad3)
            if tarjetacuota1:
                debetarjeta1 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota1,
                                                                 importe=tarjetaimporte1,
                                                                 entidad=tarjetaentidad1)
            if tarjetacuota2:
                debetarjeta2 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota2,
                                                                 importe=tarjetaimporte2,
                                                                 entidad=tarjetaentidad2)
            if tarjetacuota3:
                debetarjeta3 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota3,
                                                                 importe=tarjetaimporte3,
                                                                 entidad=tarjetaentidad3)
            if recivosimporte1:
                deberecivo1s = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte1)
            if recivosimporte2:
                deberecivos2 = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte2)
            if recivosimporte3:
                deberecivos3 = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte3)
            if morosoimporte1:
                debemoroso1 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte1,
                                                               quien=morosoquien1)
            if morosoimporte2:
                debemoroso2 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte2,
                                                               quien=morosoquien2)
            if morosoimporte3:
                debemoroso3 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte3,
                                                               quien=morosoquien3)

            return HttpResponseRedirect('/formularios/')
        else:
            print form.errors
    else:
        form = forms.formCoche()
        lastNum = models.expediente.objects.all().order_by("numexp").last()
        if not lastNum:
            lastNum = 40000
        else:
            lastNum += 1
        form.fields["numexp"].initial = lastNum
        form.fields["datayhora"].initial = datetime.now()
        context.update({"form": form})
        return render(request, 'form_coche.html', context)


def microcredito(request):
    context = {}
    if request.method == 'POST':
        form = forms.formMicrocredito(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dni = form.cleaned_data['dni']
            direccion = form.cleaned_data['direccion']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            movil = form.cleaned_data['movil']
            fechanacimiento = form.cleaned_data['fechanacimiento']
            nacionalidad = form.cleaned_data['nacionalidad']
            estadocivil = form.cleaned_data['estadocivil']
            tipocasado = form.cleaned_data['tipocasado']
            numerohijos = form.cleaned_data['numerohijos']
            mayoresdeedad = form.cleaned_data['mayoresdeedad']
            cuantosacargo = form.cleaned_data['cuantosacargo']
            ingresohijos = form.cleaned_data['ingresohijos']
            anotacionespersonales = form.cleaned_data['anotacionespersonales']
            cotizacion = form.cleaned_data['cotizacion']
            tipotrabajo = form.cleaned_data['tipotrabajo']
            finalizacontrato = form.cleaned_data['finalizacontrato']
            nombreempresa1 = form.cleaned_data['nombreempresa1']
            cargoempresa1 = form.cleaned_data['cargoempresa1']
            actividadempresa1 = form.cleaned_data['actividadempresa1']
            ingresosempresa1 = form.cleaned_data['ingresosempresa1']
            pagasempresa1 = form.cleaned_data['pagasempresa1']
            otrosingresosempresa1 = form.cleaned_data['otrosingresosempresa1']
            antiguedadempresa1 = form.cleaned_data['antiguedadempresa1']
            nombreempresa2 = form.cleaned_data['nombreempresa2']
            cargoempresa2 = form.cleaned_data['cargoempresa2']
            actividadempresa2 = form.cleaned_data['actividadempresa2']
            ingresosempresa2 = form.cleaned_data['ingresosempresa2']
            pagasempresa2 = form.cleaned_data['pagasempresa2']
            otrosingresosempresa2 = form.cleaned_data['otrosingresosempresa2']
            antiguedadempresa2 = form.cleaned_data['antiguedadempresa2']
            nombreempresa3 = form.cleaned_data['nombreempresa3']
            cargoempresa3 = form.cleaned_data['cargoempresa3']
            actividadempresa3 = form.cleaned_data['actividadempresa3']
            ingresosempresa3 = form.cleaned_data['ingresosempresa3']
            pagasempresa3 = form.cleaned_data['pagasempresa3']
            otrosingresosempresa3 = form.cleaned_data['otrosingresosempresa3']
            antiguedadempresa3 = form.cleaned_data['antiguedadempresa3']
            importejuvilacion = form.cleaned_data['importejuvilacion']
            numerodepagasjuvilacion = form.cleaned_data['numerodepagasjuvilacion']
            iniciojuvilacion = form.cleaned_data['iniciojuvilacion']
            finjuvilacion = form.cleaned_data['finjuvilacion']
            parodesdecuando = form.cleaned_data['parodesdecuando']
            parocuantocobra = form.cleaned_data['parocuantocobra']
            otrosingresos = form.cleaned_data['otrosingresos']
            otrosgastos = form.cleaned_data['otrosgastos']
            otrosingresostexto = form.cleaned_data['otrosingresostexto']
            otrosgastostexto = form.cleaned_data['otrosgastostexto']
            anotacionesingresos = form.cleaned_data['anotacionesingresos']
            viviendavalor1 = form.cleaned_data['viviendavalor1']
            viviendavalorhipoteca1 = form.cleaned_data['viviendavalorhipoteca1']
            viviendaestapagada1 = form.cleaned_data['viviendaestapagada1']
            viviendalibredecargos1 = form.cleaned_data['viviendalibredecargos1']
            viviendacuotamensual1 = form.cleaned_data['viviendacuotamensual1']
            viviendaanos1 = form.cleaned_data['viviendaanos1']
            viviendaentidad1 = form.cleaned_data['viviendaentidad1']
            viviendametros1 = form.cleaned_data['viviendametros1']
            viviendaporciento1 = form.cleaned_data['viviendaporciento1']
            viviendadireccion1 = form.cleaned_data['viviendadireccion1']
            viviendapoblacion1 = form.cleaned_data['viviendapoblacion1']
            viviendaprovincia1 = form.cleaned_data['viviendaprovincia1']
            viviendacodigopostal1 = form.cleaned_data['viviendacodigopostal1']
            viviendavalor2 = form.cleaned_data['viviendavalor2']
            viviendavalorhipoteca2 = form.cleaned_data['viviendavalorhipoteca2']
            viviendaestapagada2 = form.cleaned_data['viviendaestapagada2']
            viviendalibredecargos2 = form.cleaned_data['viviendalibredecargos2']
            viviendacuotamensual2 = form.cleaned_data['viviendacuotamensual2']
            viviendaanos2 = form.cleaned_data['viviendaanos2']
            viviendaentidad2 = form.cleaned_data['viviendaentidad2']
            viviendametros2 = form.cleaned_data['viviendametros2']
            viviendaporciento2 = form.cleaned_data['viviendaporciento2']
            viviendadireccion2 = form.cleaned_data['viviendadireccion2']
            viviendapoblacion2 = form.cleaned_data['viviendapoblacion2']
            viviendaprovincia2 = form.cleaned_data['viviendaprovincia2']
            viviendacodigopostal2 = form.cleaned_data['viviendacodigopostal2']
            viviendavalor3 = form.cleaned_data['viviendavalor3']
            viviendavalorhipoteca3 = form.cleaned_data['viviendavalorhipoteca3']
            viviendaestapagada3 = form.cleaned_data['viviendaestapagada3']
            viviendalibredecargos3 = form.cleaned_data['viviendalibredecargos3']
            viviendacuotamensual3 = form.cleaned_data['viviendacuotamensual3']
            viviendaanos3 = form.cleaned_data['viviendaanos3']
            viviendaentidad3 = form.cleaned_data['viviendaentidad3']
            viviendametros3 = form.cleaned_data['viviendametros3']
            viviendaporciento3 = form.cleaned_data['viviendaporciento3']
            viviendadireccion3 = form.cleaned_data['viviendadireccion3']
            viviendapoblacion3 = form.cleaned_data['viviendapoblacion3']
            viviendaprovincia3 = form.cleaned_data['viviendaprovincia3']
            viviendacodigopostal3 = form.cleaned_data['viviendacodigopostal3']
            viviendaalquiladavalor1 = form.cleaned_data['viviendaalquiladavalor1']
            viviendaalquiladavalorhipoteca1 = form.cleaned_data['viviendaalquiladavalorhipoteca1']
            viviendaalquiladaestapagada1 = form.cleaned_data['viviendaalquiladaestapagada1']
            viviendaalquiladalibredecargos1 = form.cleaned_data['viviendaalquiladalibredecargos1']
            viviendaalquiladacuotamensual1 = form.cleaned_data['viviendaalquiladacuotamensual1']
            viviendaalquiladaanos1 = form.cleaned_data['viviendaalquiladaanos1']
            viviendaalquiladaentidad1 = form.cleaned_data['viviendaalquiladaentidad1']
            viviendaalquiladametros1 = form.cleaned_data['viviendaalquiladametros1']
            viviendaalquiladaporciento1 = form.cleaned_data['viviendaalquiladaporciento1']
            viviendaalquiladadireccion1 = form.cleaned_data['viviendaalquiladadireccion1']
            viviendaalquiladapoblacion1 = form.cleaned_data['viviendaalquiladapoblacion1']
            viviendaalquiladaprovincia1 = form.cleaned_data['viviendaalquiladaprovincia1']
            viviendaalquiladacodigopostal1 = form.cleaned_data['viviendaalquiladacodigopostal1']
            viviendaalquiladacobraalquiler1 = form.cleaned_data['viviendaalquiladacobraalquiler1']
            viviendaalquiladavalor2 = form.cleaned_data['viviendaalquiladavalor2']
            viviendaalquiladavalorhipoteca2 = form.cleaned_data['viviendaalquiladavalorhipoteca2']
            viviendaalquiladaestapagada2 = form.cleaned_data['viviendaalquiladaestapagada2']
            viviendaalquiladalibredecargos2 = form.cleaned_data['viviendaalquiladalibredecargos2']
            viviendaalquiladacuotamensual2 = form.cleaned_data['viviendaalquiladacuotamensual2']
            viviendaalquiladaanos2 = form.cleaned_data['viviendaalquiladaanos2']
            viviendaalquiladaentidad2 = form.cleaned_data['viviendaalquiladaentidad2']
            viviendaalquiladametros2 = form.cleaned_data['viviendaalquiladametros2']
            viviendaalquiladaporciento2 = form.cleaned_data['viviendaalquiladaporciento2']
            viviendaalquiladadireccion2 = form.cleaned_data['viviendaalquiladadireccion2']
            viviendaalquiladapoblacion2 = form.cleaned_data['viviendaalquiladapoblacion2']
            viviendaalquiladaprovincia2 = form.cleaned_data['viviendaalquiladaprovincia2']
            viviendaalquiladacodigopostal2 = form.cleaned_data['viviendaalquiladacodigopostal2']
            viviendaalquiladacobraalquiler2 = form.cleaned_data['viviendaalquiladacobraalquiler2']
            viviendaalquiladavalor3 = form.cleaned_data['viviendaalquiladavalor3']
            viviendaalquiladavalorhipoteca3 = form.cleaned_data['viviendaalquiladavalorhipoteca3']
            viviendaalquiladaestapagada3 = form.cleaned_data['viviendaalquiladaestapagada3']
            viviendaalquiladalibredecargos3 = form.cleaned_data['viviendaalquiladalibredecargos3']
            viviendaalquiladacuotamensual3 = form.cleaned_data['viviendaalquiladacuotamensual3']
            viviendaalquiladaanos3 = form.cleaned_data['viviendaalquiladaanos3']
            viviendaalquiladaentidad3 = form.cleaned_data['viviendaalquiladaentidad3']
            viviendaalquiladametros3 = form.cleaned_data['viviendaalquiladametros3']
            viviendaalquiladaporciento3 = form.cleaned_data['viviendaalquiladaporciento3']
            viviendaalquiladadireccion3 = form.cleaned_data['viviendaalquiladadireccion3']
            viviendaalquiladapoblacion3 = form.cleaned_data['viviendaalquiladapoblacion3']
            viviendaalquiladaprovincia3 = form.cleaned_data['viviendaalquiladaprovincia3']
            viviendaalquiladacodigopostal3 = form.cleaned_data['viviendaalquiladacodigopostal3']
            viviendaalquiladacobraalquiler3 = form.cleaned_data['viviendaalquiladacobraalquiler3']
            alquilerpaga1 = form.cleaned_data['alquilerpaga1']
            alquilermetros1 = form.cleaned_data['alquilermetros1']
            alquilerdireccion1 = form.cleaned_data['alquilerdireccion1']
            alquilerpoblacion1 = form.cleaned_data['alquilerpoblacion1']
            alquilerprovincia1 = form.cleaned_data['alquilerprovincia1']
            alquilercodigopostal1 = form.cleaned_data['alquilercodigopostal1']
            alquilerpaga2 = form.cleaned_data['alquilerpaga2']
            alquilermetros2 = form.cleaned_data['alquilermetros2']
            alquilerdireccion2 = form.cleaned_data['alquilerdireccion2']
            alquilerpoblacion2 = form.cleaned_data['alquilerpoblacion2']
            alquilerprovincia2 = form.cleaned_data['alquilerprovincia2']
            alquilercodigopostal2 = form.cleaned_data['alquilercodigopostal2']
            alquilerpaga3 = form.cleaned_data['alquilerpaga3']
            alquilermetros3 = form.cleaned_data['alquilermetros3']
            alquilerdireccion3 = form.cleaned_data['alquilerdireccion3']
            alquilerpoblacion3 = form.cleaned_data['alquilerpoblacion3']
            alquilerprovincia3 = form.cleaned_data['alquilerprovincia3']
            alquilercodigopostal3 = form.cleaned_data['alquilercodigopostal3']
            direccionpersonal = form.cleaned_data['direccionpersonal']
            poblacionpersonal = form.cleaned_data['poblacionpersonal']
            provinciapersonal = form.cleaned_data['provinciapersonal']
            codigopostalpersonal = form.cleaned_data['codigopostalpersonal']
            anotacionesviviendas = form.cleaned_data['anotacionesviviendas']
            creditotipo1 = form.cleaned_data['creditotipo1']
            creditotantoporciento1 = form.cleaned_data['creditotantoporciento1']
            creditoimporte1 = form.cleaned_data['creditoimporte1']
            creditocuota1 = form.cleaned_data['creditocuota1']
            creditoentidad1 = form.cleaned_data['creditoentidad1']
            creditotipo2 = form.cleaned_data['creditotipo2']
            creditotantoporciento2 = form.cleaned_data['creditotantoporciento2']
            creditoimporte2 = form.cleaned_data['creditoimporte2']
            creditocuota2 = form.cleaned_data['creditocuota2']
            creditoentidad2 = form.cleaned_data['creditoentidad2']
            creditotipo3 = form.cleaned_data['creditotipo3']
            creditotantoporciento3 = form.cleaned_data['creditotantoporciento3']
            creditoimporte3 = form.cleaned_data['creditoimporte3']
            creditocuota3 = form.cleaned_data['creditocuota3']
            creditoentidad3 = form.cleaned_data['creditoentidad3']
            tarjetacuota1 = form.cleaned_data['tarjetacuota1']
            tarjetaimporte1 = form.cleaned_data['tarjetaimporte1']
            tarjetaentidad1 = form.cleaned_data['tarjetaentidad1']
            tarjetacuota2 = form.cleaned_data['tarjetacuota2']
            tarjetaimporte2 = form.cleaned_data['tarjetaimporte2']
            tarjetaentidad2 = form.cleaned_data['tarjetaentidad2']
            tarjetacuota3 = form.cleaned_data['tarjetacuota3']
            tarjetaimporte3 = form.cleaned_data['tarjetaimporte3']
            tarjetaentidad3 = form.cleaned_data['tarjetaentidad3']
            recivosimporte1 = form.cleaned_data['recivosimporte1']
            recivosimporte2 = form.cleaned_data['recivosimporte2']
            recivosimporte3 = form.cleaned_data['recivosimporte3']
            morosoimporte1 = form.cleaned_data['morosoimporte1']
            morosoquien1 = form.cleaned_data['morosoquien1']
            morosoimporte2 = form.cleaned_data['morosoimporte2']
            morosoquien2 = form.cleaned_data['morosoquien2']
            morosoimporte3 = form.cleaned_data['morosoimporte3']
            morosoquien3 = form.cleaned_data['morosoquien3']
            anotacionesfinancieras = form.cleaned_data['anotacionesfinancieras']
            metodopago = form.cleaned_data['metodopago']
            anotacionesdestinado = form.cleaned_data['anotacionesdestinado']
            justificante = form.cleaned_data['justificante']
            autorizacion = form.cleaned_data['autorizacion']
            medio = form.cleaned_data['medio']
            numexp = form.cleaned_data['numexp']
            datayhora = form.cleaned_data['datayhora']

            expedient = models.expediente.objects.create(numexp=numexp, tipo="Coche", fecha_hora=datayhora)
            persona = models.persona.objects.create(numexp=numexp, nombre=name, dni=dni, direccion=direccion,
                                                    email=email, telefono=telefono, movil=movil,
                                                    fechanacimiento=fechanacimiento,
                                                    nacionalidad=nacionalidad, estadocivil=estadocivil,
                                                    tipocasado=tipocasado, numerodehijos=numerohijos,
                                                    sihijosmayores18=mayoresdeedad, sihijoscuantoscargo=cuantosacargo,
                                                    sihijosingreso=ingresohijos, justificante=justificante,
                                                    autoriza=autorizacion, medio=medio, metodopago=metodopago)
            personaanexos = models.personaanexos.objects.create(numexp=numexp, seguridadsocial=cotizacion,
                                                                siajenatipo=tipotrabajo,
                                                                siajenatemporal=finalizacontrato,
                                                                otrosingresos=otrosingresos,
                                                                otrosingresostexto=otrosingresostexto,
                                                                otrosgastos=otrosgastos,
                                                                otrosgastostexto=otrosgastostexto)
            paro = models.paro.objectos.create(numexp=numexp, desdecuando=parodesdecuando, cobra=parocuantocobra)
            juvilacion = models.juvilacion.objetos.create(numexp, importe=importejuvilacion,
                                                          pagas=numerodepagasjuvilacion, fechainicio=iniciojuvilacion,
                                                          fechafin=finjuvilacion)
            anotaciones = models.anotaciones.objects.create(numexp=numexp, personales=anotacionespersonales,
                                                            empresa=anotacionesingresos, vivienda=anotacionesviviendas,
                                                            financieros=anotacionesfinancieras,
                                                            destinado=anotacionesdestinado, coche=anotacionescoche)

            if viviendadireccion1:
                vivienda = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion1,
                                                          poblacion=viviendapoblacion1, provincia=viviendaprovincia1,
                                                          codigopostal=viviendacodigopostal1,
                                                          valorvivienda=viviendavalor1,
                                                          valorhipoteca=viviendavalorhipoteca1,
                                                          estapagada=viviendaestapagada1, sinopagadaanos=viviendaanos1,
                                                          sinopagadaentidad=viviendaentidad1,
                                                          sinopagadapagahipoteca=viviendacuotamensual1,
                                                          librecargos=viviendalibredecargos1, metros=viviendametros1,
                                                          porciento=viviendaporciento1)

            if viviendadireccion2:
                vivienda2 = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion2,
                                                           poblacion=viviendapoblacion2, provincia=viviendaprovincia2,
                                                           codigopostal=viviendacodigopostal2,
                                                           valorvivienda=viviendavalor2,
                                                           valorhipoteca=viviendavalorhipoteca2,
                                                           estapagada=viviendaestapagada2, sinopagadaanos=viviendaanos2,
                                                           sinopagadaentidad=viviendaentidad2,
                                                           sinopagadapagahipoteca=viviendacuotamensual2,
                                                           librecargos=viviendalibredecargos2, metros=viviendametros2,
                                                           porciento=viviendaporciento2)

            if viviendadireccion3:
                vivienda3 = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion3,
                                                           poblacion=viviendapoblacion3, provincia=viviendaprovincia3,
                                                           codigopostal=viviendacodigopostal3,
                                                           valorvivienda=viviendavalor3,
                                                           valorhipoteca=viviendavalorhipoteca3,
                                                           estapagada=viviendaestapagada3, sinopagadaanos=viviendaanos3,
                                                           sinopagadaentidad=viviendaentidad3,
                                                           sinopagadapagahipoteca=viviendacuotamensual3,
                                                           librecargos=viviendalibredecargos3, metros=viviendametros3,
                                                           porciento=viviendaporciento3)

            if viviendaalquiladadireccion1:
                viviendaalquilada = models.vivienda.objects.create(numexp=numexp, direccion=viviendaalquiladadireccion1,
                                                                   poblacion=viviendaalquiladapoblacion1,
                                                                   provincia=viviendaalquiladaprovincia1,
                                                                   codigopostal=viviendaalquiladacodigopostal1,
                                                                   valorvivienda=viviendaalquiladavalor1,
                                                                   valorhipoteca=viviendaalquiladavalorhipoteca1,
                                                                   estapagada=viviendaalquiladaestapagada1,
                                                                   sinopagadaanos=viviendaalquiladaanos1,
                                                                   sinopagadaentidad=viviendaalquiladaentidad1,
                                                                   librecargos=viviendaalquiladalibredecargos1,
                                                                   metros=viviendaalquiladametros1,
                                                                   porciento=viviendaalquiladaporciento1,
                                                                   valoralquilada=viviendaalquiladacobraalquiler1,
                                                                   sinopagadapagahipoteca=viviendaalquiladacuotamensual1)

            if viviendaalquiladadireccion2:
                viviendaalquilada2 = models.vivienda.objects.create(numexp=numexp,
                                                                    direccion=viviendaalquiladadireccion2,
                                                                    poblacion=viviendaalquiladapoblacion2,
                                                                    provincia=viviendaalquiladaprovincia2,
                                                                    codigopostal=viviendaalquiladacodigopostal2,
                                                                    valorvivienda=viviendaalquiladavalor2,
                                                                    valorhipoteca=viviendaalquiladavalorhipoteca2,
                                                                    estapagada=viviendaalquiladaestapagada2,
                                                                    sinopagadaanos=viviendaalquiladaanos2,
                                                                    sinopagadaentidad=viviendaalquiladaentidad2,
                                                                    librecargos=viviendaalquiladalibredecargos2,
                                                                    metros=viviendaalquiladametros2,
                                                                    porciento=viviendaalquiladaporciento2,
                                                                    valoralquilada=viviendaalquiladacobraalquiler2,
                                                                    sinopagadapagahipoteca=viviendaalquiladacuotamensual2)

            if viviendaalquiladadireccion3:
                viviendaalquilada3 = models.vivienda.objects.create(numexp=numexp,
                                                                    direccion=viviendaalquiladadireccion3,
                                                                    poblacion=viviendaalquiladapoblacion3,
                                                                    provincia=viviendaalquiladaprovincia3,
                                                                    codigopostal=viviendaalquiladacodigopostal3,
                                                                    valorvivienda=viviendaalquiladavalor3,
                                                                    valorhipoteca=viviendaalquiladavalorhipoteca3,
                                                                    estapagada=viviendaalquiladaestapagada3,
                                                                    sinopagadaanos=viviendaalquiladaanos3,
                                                                    sinopagadaentidad=viviendaalquiladaentidad3,
                                                                    librecargos=viviendaalquiladalibredecargos3,
                                                                    metros=viviendaalquiladametros3,
                                                                    porciento=viviendaalquiladaporciento3,
                                                                    valoralquilada=viviendaalquiladacobraalquiler3,
                                                                    sinopagadapagahipoteca=viviendaalquiladacuotamensual3)

            if alquilerdireccion1:
                alquiler = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion1,
                                                          poblacion=alquilerpoblacion1, provincia=alquilerprovincia1,
                                                          codigopostal=alquilercodigopostal1, metros=alquilermetros1,
                                                          pagaalquiler=alquilerpaga1)

            if alquilerdireccion2:
                alquiler2 = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion2,
                                                           poblacion=alquilerpoblacion2, provincia=alquilerprovincia2,
                                                           codigopostal=alquilercodigopostal2, metros=alquilermetros2,
                                                           pagaalquiler=alquilerpaga2)

            if alquilerdireccion3:
                alquiler3 = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion3,
                                                           poblacion=alquilerpoblacion3, provincia=alquilerprovincia3,
                                                           codigopostal=alquilercodigopostal3, metros=alquilermetros3,
                                                           pagaalquiler=alquilerpaga3)

            if direccionpersonal:
                vivienda = models.vivienda.objects.create(numexp=numexp, direccion=direccionpersonal,
                                                          poblacion=poblacionpersonal, provincia=provinciapersonal,
                                                          codigopostal=codigopostalpersonal)

            if nombreempresa1:
                empresa = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa1, cargo=cargoempresa1,
                                                        actividad=actividadempresa1, ingresos=ingresosempresa1,
                                                        pagas=pagasempresa1, otrosingresos=otrosingresosempresa1,
                                                        antiguedad=antiguedadempresa1)

            if nombreempresa2:
                empresa2 = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa2, cargo=cargoempresa2,
                                                         actividad=actividadempresa2, ingresos=ingresosempresa2,
                                                         pagas=pagasempresa2, otrosingresos=otrosingresosempresa2,
                                                         antiguedad=antiguedadempresa2)

            if nombreempresa3:
                empresa3 = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa3, cargo=cargoempresa3,
                                                         actividad=actividadempresa3, ingresos=ingresosempresa3,
                                                         pagas=pagasempresa3, otrosingresos=otrosingresosempresa3,
                                                         antiguedad=antiguedadempresa3)

            if creditotipo1:
                debecredito1 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo1,
                                                                 porcientoavalista=creditotantoporciento1,
                                                                 importe=creditoimporte1, cuota=creditocuota1,
                                                                 entidad=creditoentidad1)
            if creditotipo2:
                debecredito2 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo2,
                                                                 porcientoavalista=creditotantoporciento2,
                                                                 importe=creditoimporte2, cuota=creditocuota2,
                                                                 entidad=creditoentidad2)
            if creditotipo3:
                debecredito3 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo3,
                                                                 porcientoavalista=creditotantoporciento3,
                                                                 importe=creditoimporte3, cuota=creditocuota3,
                                                                 entidad=creditoentidad3)
            if tarjetacuota1:
                debetarjeta1 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota1,
                                                                 importe=tarjetaimporte1,
                                                                 entidad=tarjetaentidad1)
            if tarjetacuota2:
                debetarjeta2 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota2,
                                                                 importe=tarjetaimporte2,
                                                                 entidad=tarjetaentidad2)
            if tarjetacuota3:
                debetarjeta3 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota3,
                                                                 importe=tarjetaimporte3,
                                                                 entidad=tarjetaentidad3)
            if recivosimporte1:
                deberecivo1s = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte1)
            if recivosimporte2:
                deberecivos2 = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte2)
            if recivosimporte3:
                deberecivos3 = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte3)
            if morosoimporte1:
                debemoroso1 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte1,
                                                               quien=morosoquien1)
            if morosoimporte2:
                debemoroso2 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte2,
                                                               quien=morosoquien2)
            if morosoimporte3:
                debemoroso3 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte3,
                                                               quien=morosoquien3)

            return HttpResponseRedirect('/microcredito/')
        else:
            print form.errors
    else:
        form = forms.formMicrocredito()
        lastNum = models.expediente.objects.all().order_by("numexp").last()
        if not lastNum:
            lastNum = 40000
        else:
            lastNum += 1
        form.fields["numexp"].initial = lastNum
        form.fields["datayhora"].initial = datetime.now()
        context.update({"form": form})
        return render(request, 'form_microcre.html', context)


def personal(request):
    context = {}
    if request.method == 'POST':
        form = forms.formPersonal(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dni = form.cleaned_data['dni']
            direccion = form.cleaned_data['direccion']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            movil = form.cleaned_data['movil']
            fechanacimiento = form.cleaned_data['fechanacimiento']
            nacionalidad = form.cleaned_data['nacionalidad']
            estadocivil = form.cleaned_data['estadocivil']
            tipocasado = form.cleaned_data['tipocasado']
            numerohijos = form.cleaned_data['numerohijos']
            mayoresdeedad = form.cleaned_data['mayoresdeedad']
            cuantosacargo = form.cleaned_data['cuantosacargo']
            ingresohijos = form.cleaned_data['ingresohijos']
            anotacionespersonales = form.cleaned_data['anotacionespersonales']
            cotizacion = form.cleaned_data['cotizacion']
            tipotrabajo = form.cleaned_data['tipotrabajo']
            finalizacontrato = form.cleaned_data['finalizacontrato']
            nombreempresa1 = form.cleaned_data['nombreempresa1']
            cargoempresa1 = form.cleaned_data['cargoempresa1']
            actividadempresa1 = form.cleaned_data['actividadempresa1']
            ingresosempresa1 = form.cleaned_data['ingresosempresa1']
            pagasempresa1 = form.cleaned_data['pagasempresa1']
            otrosingresosempresa1 = form.cleaned_data['otrosingresosempresa1']
            antiguedadempresa1 = form.cleaned_data['antiguedadempresa1']
            nombreempresa2 = form.cleaned_data['nombreempresa2']
            cargoempresa2 = form.cleaned_data['cargoempresa2']
            actividadempresa2 = form.cleaned_data['actividadempresa2']
            ingresosempresa2 = form.cleaned_data['ingresosempresa2']
            pagasempresa2 = form.cleaned_data['pagasempresa2']
            otrosingresosempresa2 = form.cleaned_data['otrosingresosempresa2']
            antiguedadempresa2 = form.cleaned_data['antiguedadempresa2']
            nombreempresa3 = form.cleaned_data['nombreempresa3']
            cargoempresa3 = form.cleaned_data['cargoempresa3']
            actividadempresa3 = form.cleaned_data['actividadempresa3']
            ingresosempresa3 = form.cleaned_data['ingresosempresa3']
            pagasempresa3 = form.cleaned_data['pagasempresa3']
            otrosingresosempresa3 = form.cleaned_data['otrosingresosempresa3']
            antiguedadempresa3 = form.cleaned_data['antiguedadempresa3']
            importejuvilacion = form.cleaned_data['importejuvilacion']
            numerodepagasjuvilacion = form.cleaned_data['numerodepagasjuvilacion']
            iniciojuvilacion = form.cleaned_data['iniciojuvilacion']
            finjuvilacion = form.cleaned_data['finjuvilacion']
            parodesdecuando = form.cleaned_data['parodesdecuando']
            parocuantocobra = form.cleaned_data['parocuantocobra']
            otrosingresos = form.cleaned_data['otrosingresos']
            otrosgastos = form.cleaned_data['otrosgastos']
            otrosingresostexto = form.cleaned_data['otrosingresostexto']
            otrosgastostexto = form.cleaned_data['otrosgastostexto']
            anotacionesingresos = form.cleaned_data['anotacionesingresos']
            viviendavalor1 = form.cleaned_data['viviendavalor1']
            viviendavalorhipoteca1 = form.cleaned_data['viviendavalorhipoteca1']
            viviendaestapagada1 = form.cleaned_data['viviendaestapagada1']
            viviendalibredecargos1 = form.cleaned_data['viviendalibredecargos1']
            viviendacuotamensual1 = form.cleaned_data['viviendacuotamensual1']
            viviendaanos1 = form.cleaned_data['viviendaanos1']
            viviendaentidad1 = form.cleaned_data['viviendaentidad1']
            viviendametros1 = form.cleaned_data['viviendametros1']
            viviendaporciento1 = form.cleaned_data['viviendaporciento1']
            viviendadireccion1 = form.cleaned_data['viviendadireccion1']
            viviendapoblacion1 = form.cleaned_data['viviendapoblacion1']
            viviendaprovincia1 = form.cleaned_data['viviendaprovincia1']
            viviendacodigopostal1 = form.cleaned_data['viviendacodigopostal1']
            viviendavalor2 = form.cleaned_data['viviendavalor2']
            viviendavalorhipoteca2 = form.cleaned_data['viviendavalorhipoteca2']
            viviendaestapagada2 = form.cleaned_data['viviendaestapagada2']
            viviendalibredecargos2 = form.cleaned_data['viviendalibredecargos2']
            viviendacuotamensual2 = form.cleaned_data['viviendacuotamensual2']
            viviendaanos2 = form.cleaned_data['viviendaanos2']
            viviendaentidad2 = form.cleaned_data['viviendaentidad2']
            viviendametros2 = form.cleaned_data['viviendametros2']
            viviendaporciento2 = form.cleaned_data['viviendaporciento2']
            viviendadireccion2 = form.cleaned_data['viviendadireccion2']
            viviendapoblacion2 = form.cleaned_data['viviendapoblacion2']
            viviendaprovincia2 = form.cleaned_data['viviendaprovincia2']
            viviendacodigopostal2 = form.cleaned_data['viviendacodigopostal2']
            viviendavalor3 = form.cleaned_data['viviendavalor3']
            viviendavalorhipoteca3 = form.cleaned_data['viviendavalorhipoteca3']
            viviendaestapagada3 = form.cleaned_data['viviendaestapagada3']
            viviendalibredecargos3 = form.cleaned_data['viviendalibredecargos3']
            viviendacuotamensual3 = form.cleaned_data['viviendacuotamensual3']
            viviendaanos3 = form.cleaned_data['viviendaanos3']
            viviendaentidad3 = form.cleaned_data['viviendaentidad3']
            viviendametros3 = form.cleaned_data['viviendametros3']
            viviendaporciento3 = form.cleaned_data['viviendaporciento3']
            viviendadireccion3 = form.cleaned_data['viviendadireccion3']
            viviendapoblacion3 = form.cleaned_data['viviendapoblacion3']
            viviendaprovincia3 = form.cleaned_data['viviendaprovincia3']
            viviendacodigopostal3 = form.cleaned_data['viviendacodigopostal3']
            viviendaalquiladavalor1 = form.cleaned_data['viviendaalquiladavalor1']
            viviendaalquiladavalorhipoteca1 = form.cleaned_data['viviendaalquiladavalorhipoteca1']
            viviendaalquiladaestapagada1 = form.cleaned_data['viviendaalquiladaestapagada1']
            viviendaalquiladalibredecargos1 = form.cleaned_data['viviendaalquiladalibredecargos1']
            viviendaalquiladacuotamensual1 = form.cleaned_data['viviendaalquiladacuotamensual1']
            viviendaalquiladaanos1 = form.cleaned_data['viviendaalquiladaanos1']
            viviendaalquiladaentidad1 = form.cleaned_data['viviendaalquiladaentidad1']
            viviendaalquiladametros1 = form.cleaned_data['viviendaalquiladametros1']
            viviendaalquiladaporciento1 = form.cleaned_data['viviendaalquiladaporciento1']
            viviendaalquiladadireccion1 = form.cleaned_data['viviendaalquiladadireccion1']
            viviendaalquiladapoblacion1 = form.cleaned_data['viviendaalquiladapoblacion1']
            viviendaalquiladaprovincia1 = form.cleaned_data['viviendaalquiladaprovincia1']
            viviendaalquiladacodigopostal1 = form.cleaned_data['viviendaalquiladacodigopostal1']
            viviendaalquiladacobraalquiler1 = form.cleaned_data['viviendaalquiladacobraalquiler1']
            viviendaalquiladavalor2 = form.cleaned_data['viviendaalquiladavalor2']
            viviendaalquiladavalorhipoteca2 = form.cleaned_data['viviendaalquiladavalorhipoteca2']
            viviendaalquiladaestapagada2 = form.cleaned_data['viviendaalquiladaestapagada2']
            viviendaalquiladalibredecargos2 = form.cleaned_data['viviendaalquiladalibredecargos2']
            viviendaalquiladacuotamensual2 = form.cleaned_data['viviendaalquiladacuotamensual2']
            viviendaalquiladaanos2 = form.cleaned_data['viviendaalquiladaanos2']
            viviendaalquiladaentidad2 = form.cleaned_data['viviendaalquiladaentidad2']
            viviendaalquiladametros2 = form.cleaned_data['viviendaalquiladametros2']
            viviendaalquiladaporciento2 = form.cleaned_data['viviendaalquiladaporciento2']
            viviendaalquiladadireccion2 = form.cleaned_data['viviendaalquiladadireccion2']
            viviendaalquiladapoblacion2 = form.cleaned_data['viviendaalquiladapoblacion2']
            viviendaalquiladaprovincia2 = form.cleaned_data['viviendaalquiladaprovincia2']
            viviendaalquiladacodigopostal2 = form.cleaned_data['viviendaalquiladacodigopostal2']
            viviendaalquiladacobraalquiler2 = form.cleaned_data['viviendaalquiladacobraalquiler2']
            viviendaalquiladavalor3 = form.cleaned_data['viviendaalquiladavalor3']
            viviendaalquiladavalorhipoteca3 = form.cleaned_data['viviendaalquiladavalorhipoteca3']
            viviendaalquiladaestapagada3 = form.cleaned_data['viviendaalquiladaestapagada3']
            viviendaalquiladalibredecargos3 = form.cleaned_data['viviendaalquiladalibredecargos3']
            viviendaalquiladacuotamensual3 = form.cleaned_data['viviendaalquiladacuotamensual3']
            viviendaalquiladaanos3 = form.cleaned_data['viviendaalquiladaanos3']
            viviendaalquiladaentidad3 = form.cleaned_data['viviendaalquiladaentidad3']
            viviendaalquiladametros3 = form.cleaned_data['viviendaalquiladametros3']
            viviendaalquiladaporciento3 = form.cleaned_data['viviendaalquiladaporciento3']
            viviendaalquiladadireccion3 = form.cleaned_data['viviendaalquiladadireccion3']
            viviendaalquiladapoblacion3 = form.cleaned_data['viviendaalquiladapoblacion3']
            viviendaalquiladaprovincia3 = form.cleaned_data['viviendaalquiladaprovincia3']
            viviendaalquiladacodigopostal3 = form.cleaned_data['viviendaalquiladacodigopostal3']
            viviendaalquiladacobraalquiler3 = form.cleaned_data['viviendaalquiladacobraalquiler3']
            alquilerpaga1 = form.cleaned_data['alquilerpaga1']
            alquilermetros1 = form.cleaned_data['alquilermetros1']
            alquilerdireccion1 = form.cleaned_data['alquilerdireccion1']
            alquilerpoblacion1 = form.cleaned_data['alquilerpoblacion1']
            alquilerprovincia1 = form.cleaned_data['alquilerprovincia1']
            alquilercodigopostal1 = form.cleaned_data['alquilercodigopostal1']
            alquilerpaga2 = form.cleaned_data['alquilerpaga2']
            alquilermetros2 = form.cleaned_data['alquilermetros2']
            alquilerdireccion2 = form.cleaned_data['alquilerdireccion2']
            alquilerpoblacion2 = form.cleaned_data['alquilerpoblacion2']
            alquilerprovincia2 = form.cleaned_data['alquilerprovincia2']
            alquilercodigopostal2 = form.cleaned_data['alquilercodigopostal2']
            alquilerpaga3 = form.cleaned_data['alquilerpaga3']
            alquilermetros3 = form.cleaned_data['alquilermetros3']
            alquilerdireccion3 = form.cleaned_data['alquilerdireccion3']
            alquilerpoblacion3 = form.cleaned_data['alquilerpoblacion3']
            alquilerprovincia3 = form.cleaned_data['alquilerprovincia3']
            alquilercodigopostal3 = form.cleaned_data['alquilercodigopostal3']
            direccionpersonal = form.cleaned_data['direccionpersonal']
            poblacionpersonal = form.cleaned_data['poblacionpersonal']
            provinciapersonal = form.cleaned_data['provinciapersonal']
            codigopostalpersonal = form.cleaned_data['codigopostalpersonal']
            anotacionesviviendas = form.cleaned_data['anotacionesviviendas']
            creditotipo1 = form.cleaned_data['creditotipo1']
            creditotantoporciento1 = form.cleaned_data['creditotantoporciento1']
            creditoimporte1 = form.cleaned_data['creditoimporte1']
            creditocuota1 = form.cleaned_data['creditocuota1']
            creditoentidad1 = form.cleaned_data['creditoentidad1']
            creditotipo2 = form.cleaned_data['creditotipo2']
            creditotantoporciento2 = form.cleaned_data['creditotantoporciento2']
            creditoimporte2 = form.cleaned_data['creditoimporte2']
            creditocuota2 = form.cleaned_data['creditocuota2']
            creditoentidad2 = form.cleaned_data['creditoentidad2']
            creditotipo3 = form.cleaned_data['creditotipo3']
            creditotantoporciento3 = form.cleaned_data['creditotantoporciento3']
            creditoimporte3 = form.cleaned_data['creditoimporte3']
            creditocuota3 = form.cleaned_data['creditocuota3']
            creditoentidad3 = form.cleaned_data['creditoentidad3']
            tarjetacuota1 = form.cleaned_data['tarjetacuota1']
            tarjetaimporte1 = form.cleaned_data['tarjetaimporte1']
            tarjetaentidad1 = form.cleaned_data['tarjetaentidad1']
            tarjetacuota2 = form.cleaned_data['tarjetacuota2']
            tarjetaimporte2 = form.cleaned_data['tarjetaimporte2']
            tarjetaentidad2 = form.cleaned_data['tarjetaentidad2']
            tarjetacuota3 = form.cleaned_data['tarjetacuota3']
            tarjetaimporte3 = form.cleaned_data['tarjetaimporte3']
            tarjetaentidad3 = form.cleaned_data['tarjetaentidad3']
            recivosimporte1 = form.cleaned_data['recivosimporte1']
            recivosimporte2 = form.cleaned_data['recivosimporte2']
            recivosimporte3 = form.cleaned_data['recivosimporte3']
            morosoimporte1 = form.cleaned_data['morosoimporte1']
            morosoquien1 = form.cleaned_data['morosoquien1']
            morosoimporte2 = form.cleaned_data['morosoimporte2']
            morosoquien2 = form.cleaned_data['morosoquien2']
            morosoimporte3 = form.cleaned_data['morosoimporte3']
            morosoquien3 = form.cleaned_data['morosoquien3']
            anotacionesfinancieras = form.cleaned_data['anotacionesfinancieras']
            anotacionesavalista = form.cleaned_data['anotacionesavalista']
            metodopago = form.cleaned_data['metodopago']
            anotacionesdestinado = form.cleaned_data['anotacionesdestinado']
            justificante = form.cleaned_data['justificante']
            autorizacion = form.cleaned_data['autorizacion']
            medio = form.cleaned_data['medio']
            numexp = form.cleaned_data['numexp']
            datayhora = form.cleaned_data['datayhora']
            avalistaame = form.cleaned_data['avalistaame']
            avalistani = form.cleaned_data['avalistani']
            avalistaireccion = form.cleaned_data['avalistaireccion']
            avalistamail = form.cleaned_data['avalistamail']
            avalistaelefono = form.cleaned_data['avalistaelefono']
            avalistaovil = form.cleaned_data['avalistaovil']
            avalistaechanacimiento = form.cleaned_data['avalistaechanacimiento']
            avalistaacionalidad = form.cleaned_data['avalistaacionalidad']
            avalistastadocivil = form.cleaned_data['avalistastadocivil']
            avalistaipocasado = form.cleaned_data['avalistaipocasado']
            avalistaumerohijos = form.cleaned_data['avalistaumerohijos']
            avalistaayoresdeedad = form.cleaned_data['avalistaayoresdeedad']
            avalistauantosacargo = form.cleaned_data['avalistauantosacargo']
            avalistangresohijos = form.cleaned_data['avalistangresohijos']
            avalistaotizacion = form.cleaned_data['avalistaotizacion']
            avalistaipotrabajo = form.cleaned_data['avalistaipotrabajo']
            avalistainalizacontrato = form.cleaned_data['avalistainalizacontrato']
            avalistaombreempresa1 = form.cleaned_data['avalistaombreempresa1']
            avalistaargoempresa1 = form.cleaned_data['avalistaargoempresa1']
            avalistactividadempresa1 = form.cleaned_data['avalistactividadempresa1']
            avalistangresosempresa1 = form.cleaned_data['avalistangresosempresa1']
            avalistaagasempresa1 = form.cleaned_data['avalistaagasempresa1']
            avalistatrosingresosempresa1 = form.cleaned_data['avalistatrosingresosempresa1']
            avalistantiguedadempresa1 = form.cleaned_data['avalistantiguedadempresa1']
            avalistaombreempresa2 = form.cleaned_data['avalistaombreempresa2']
            avalistaargoempresa2 = form.cleaned_data['avalistaargoempresa2']
            avalistactividadempresa2 = form.cleaned_data['avalistactividadempresa2']
            avalistangresosempresa2 = form.cleaned_data['avalistangresosempresa2']
            avalistaagasempresa2 = form.cleaned_data['avalistaagasempresa2']
            avalistatrosingresosempresa2 = form.cleaned_data['avalistatrosingresosempresa2']
            avalistantiguedadempresa2 = form.cleaned_data['avalistantiguedadempresa2']
            avalistaombreempresa3 = form.cleaned_data['avalistaombreempresa3']
            avalistaargoempresa3 = form.cleaned_data['avalistaargoempresa3']
            avalistactividadempresa3 = form.cleaned_data['avalistactividadempresa3']
            avalistangresosempresa3 = form.cleaned_data['avalistangresosempresa3']
            avalistaagasempresa3 = form.cleaned_data['avalistaagasempresa3']
            avalistatrosingresosempresa3 = form.cleaned_data['avalistatrosingresosempresa3']
            avalistantiguedadempresa3 = form.cleaned_data['avalistantiguedadempresa3']
            avalistamportejuvilacion = form.cleaned_data['avalistamportejuvilacion']
            avalistaumerodepagasjuvilacion = form.cleaned_data['avalistaumerodepagasjuvilacion']
            avalistaniciojuvilacion = form.cleaned_data['avalistaniciojuvilacion']
            avalistainjuvilacion = form.cleaned_data['avalistainjuvilacion']
            avalistaarodesdecuando = form.cleaned_data['avalistaarodesdecuando']
            avalistaarocuantocobra = form.cleaned_data['avalistaarocuantocobra']
            avalistatrosingresos = form.cleaned_data['avalistatrosingresos']
            avalistatrosgastos = form.cleaned_data['avalistatrosgastos']
            avalistatrosingresostexto = form.cleaned_data['avalistatrosingresostexto']
            avalistatrosgastostexto = form.cleaned_data['avalistatrosgastostexto']
            avalistaiviendavalor1 = form.cleaned_data['avalistaiviendavalor1']
            avalistaiviendavalorhipoteca1 = form.cleaned_data['avalistaiviendavalorhipoteca1']
            avalistaiviendaestapagada1 = form.cleaned_data['avalistaiviendaestapagada1']
            avalistaiviendalibredecargos1 = form.cleaned_data['avalistaiviendalibredecargos1']
            avalistaiviendacuotamensual1 = form.cleaned_data['avalistaiviendacuotamensual1']
            avalistaiviendaanos1 = form.cleaned_data['avalistaiviendaanos1']
            avalistaiviendaentidad1 = form.cleaned_data['avalistaiviendaentidad1']
            avalistaiviendametros1 = form.cleaned_data['avalistaiviendametros1']
            avalistaiviendaporciento1 = form.cleaned_data['avalistaiviendaporciento1']
            avalistaiviendadireccion1 = form.cleaned_data['avalistaiviendadireccion1']
            avalistaiviendapoblacion1 = form.cleaned_data['avalistaiviendapoblacion1']
            avalistaiviendaprovincia1 = form.cleaned_data['avalistaiviendaprovincia1']
            avalistaiviendacodigopostal1 = form.cleaned_data['avalistaiviendacodigopostal1']
            avalistaiviendavalor2 = form.cleaned_data['avalistaiviendavalor2']
            avalistaiviendavalorhipoteca2 = form.cleaned_data['avalistaiviendavalorhipoteca2']
            avalistaiviendaestapagada2 = form.cleaned_data['avalistaiviendaestapagada2']
            avalistaiviendalibredecargos2 = form.cleaned_data['avalistaiviendalibredecargos2']
            avalistaiviendacuotamensual2 = form.cleaned_data['avalistaiviendacuotamensual2']
            avalistaiviendaanos2 = form.cleaned_data['avalistaiviendaanos2']
            avalistaiviendaentidad2 = form.cleaned_data['avalistaiviendaentidad2']
            avalistaiviendametros2 = form.cleaned_data['avalistaiviendametros2']
            avalistaiviendaporciento2 = form.cleaned_data['avalistaiviendaporciento2']
            avalistaiviendadireccion2 = form.cleaned_data['avalistaiviendadireccion2']
            avalistaiviendapoblacion2 = form.cleaned_data['avalistaiviendapoblacion2']
            avalistaiviendaprovincia2 = form.cleaned_data['avalistaiviendaprovincia2']
            avalistaiviendacodigopostal2 = form.cleaned_data['avalistaiviendacodigopostal2']
            avalistaiviendavalor3 = form.cleaned_data['avalistaiviendavalor3']
            avalistaiviendavalorhipoteca3 = form.cleaned_data['avalistaiviendavalorhipoteca3']
            avalistaiviendaestapagada3 = form.cleaned_data['avalistaiviendaestapagada3']
            avalistaiviendalibredecargos3 = form.cleaned_data['avalistaiviendalibredecargos3']
            avalistaiviendacuotamensual3 = form.cleaned_data['avalistaiviendacuotamensual3']
            avalistaiviendaanos3 = form.cleaned_data['avalistaiviendaanos3']
            avalistaiviendaentidad3 = form.cleaned_data['avalistaiviendaentidad3']
            avalistaiviendametros3 = form.cleaned_data['avalistaiviendametros3']
            avalistaiviendaporciento3 = form.cleaned_data['avalistaiviendaporciento3']
            avalistaiviendadireccion3 = form.cleaned_data['avalistaiviendadireccion3']
            avalistaiviendapoblacion3 = form.cleaned_data['avalistaiviendapoblacion3']
            avalistaiviendaprovincia3 = form.cleaned_data['avalistaiviendaprovincia3']
            avalistaiviendacodigopostal3 = form.cleaned_data['avalistaiviendacodigopostal3']
            avalistaiviendaalquiladavalor1 = form.cleaned_data['avalistaiviendaalquiladavalor1']
            avalistaiviendaalquiladavalorhipoteca1 = form.cleaned_data['avalistaiviendaalquiladavalorhipoteca1']
            avalistaiviendaalquiladaestapagada1 = form.cleaned_data['avalistaiviendaalquiladaestapagada1']
            avalistaiviendaalquiladalibredecargos1 = form.cleaned_data['avalistaiviendaalquiladalibredecargos1']
            avalistaiviendaalquiladacuotamensual1 = form.cleaned_data['avalistaiviendaalquiladacuotamensual1']
            avalistaiviendaalquiladaanos1 = form.cleaned_data['avalistaiviendaalquiladaanos1']
            avalistaiviendaalquiladaentidad1 = form.cleaned_data['avalistaiviendaalquiladaentidad1']
            avalistaiviendaalquiladametros1 = form.cleaned_data['avalistaiviendaalquiladametros1']
            avalistaiviendaalquiladaporciento1 = form.cleaned_data['avalistaiviendaalquiladaporciento1']
            avalistaiviendaalquiladadireccion1 = form.cleaned_data['avalistaiviendaalquiladadireccion1']
            avalistaiviendaalquiladapoblacion1 = form.cleaned_data['avalistaiviendaalquiladapoblacion1']
            avalistaiviendaalquiladaprovincia1 = form.cleaned_data['avalistaiviendaalquiladaprovincia1']
            avalistaiviendaalquiladacodigopostal1 = form.cleaned_data['avalistaiviendaalquiladacodigopostal1']
            avalistaiviendaalquiladacobraalquiler1 = form.cleaned_data['avalistaiviendaalquiladacobraalquiler1']
            avalistaiviendaalquiladavalor2 = form.cleaned_data['avalistaiviendaalquiladavalor2']
            avalistaiviendaalquiladavalorhipoteca2 = form.cleaned_data['avalistaiviendaalquiladavalorhipoteca2']
            avalistaiviendaalquiladaestapagada2 = form.cleaned_data['avalistaiviendaalquiladaestapagada2']
            avalistaiviendaalquiladalibredecargos2 = form.cleaned_data['avalistaiviendaalquiladalibredecargos2']
            avalistaiviendaalquiladacuotamensual2 = form.cleaned_data['avalistaiviendaalquiladacuotamensual2']
            avalistaiviendaalquiladaanos2 = form.cleaned_data['avalistaiviendaalquiladaanos2']
            avalistaiviendaalquiladaentidad2 = form.cleaned_data['avalistaiviendaalquiladaentidad2']
            avalistaiviendaalquiladametros2 = form.cleaned_data['avalistaiviendaalquiladametros2']
            avalistaiviendaalquiladaporciento2 = form.cleaned_data['avalistaiviendaalquiladaporciento2']
            avalistaiviendaalquiladadireccion2 = form.cleaned_data['avalistaiviendaalquiladadireccion2']
            avalistaiviendaalquiladapoblacion2 = form.cleaned_data['avalistaiviendaalquiladapoblacion2']
            avalistaiviendaalquiladaprovincia2 = form.cleaned_data['avalistaiviendaalquiladaprovincia2']
            avalistaiviendaalquiladacodigopostal2 = form.cleaned_data['avalistaiviendaalquiladacodigopostal2']
            avalistaiviendaalquiladacobraalquiler2 = form.cleaned_data['avalistaiviendaalquiladacobraalquiler2']
            avalistaiviendaalquiladavalor3 = form.cleaned_data['avalistaiviendaalquiladavalor3']
            avalistaiviendaalquiladavalorhipoteca3 = form.cleaned_data['avalistaiviendaalquiladavalorhipoteca3']
            avalistaiviendaalquiladaestapagada3 = form.cleaned_data['avalistaiviendaalquiladaestapagada3']
            avalistaiviendaalquiladalibredecargos3 = form.cleaned_data['avalistaiviendaalquiladalibredecargos3']
            avalistaiviendaalquiladacuotamensual3 = form.cleaned_data['avalistaiviendaalquiladacuotamensual3']
            avalistaiviendaalquiladaanos3 = form.cleaned_data['avalistaiviendaalquiladaanos3']
            avalistaiviendaalquiladaentidad3 = form.cleaned_data['avalistaiviendaalquiladaentidad3']
            avalistaiviendaalquiladametros3 = form.cleaned_data['avalistaiviendaalquiladametros3']
            avalistaiviendaalquiladaporciento3 = form.cleaned_data['avalistaiviendaalquiladaporciento3']
            avalistaiviendaalquiladadireccion3 = form.cleaned_data['avalistaiviendaalquiladadireccion3']
            avalistaiviendaalquiladapoblacion3 = form.cleaned_data['avalistaiviendaalquiladapoblacion3']
            avalistaiviendaalquiladaprovincia3 = form.cleaned_data['avalistaiviendaalquiladaprovincia3']
            avalistaiviendaalquiladacodigopostal3 = form.cleaned_data['avalistaiviendaalquiladacodigopostal3']
            avalistaiviendaalquiladacobraalquiler3 = form.cleaned_data['avalistaiviendaalquiladacobraalquiler3']
            avalistalquilerpaga1 = form.cleaned_data['avalistalquilerpaga1']
            avalistalquilermetros1 = form.cleaned_data['avalistalquilermetros1']
            avalistalquilerdireccion1 = form.cleaned_data['avalistalquilerdireccion1']
            avalistalquilerpoblacion1 = form.cleaned_data['avalistalquilerpoblacion1']
            avalistalquilerprovincia1 = form.cleaned_data['avalistalquilerprovincia1']
            avalistalquilercodigopostal1 = form.cleaned_data['avalistalquilercodigopostal1']
            avalistalquilerpaga2 = form.cleaned_data['avalistalquilerpaga2']
            avalistalquilermetros2 = form.cleaned_data['avalistalquilermetros2']
            avalistalquilerdireccion2 = form.cleaned_data['avalistalquilerdireccion2']
            avalistalquilerpoblacion2 = form.cleaned_data['avalistalquilerpoblacion2']
            avalistalquilerprovincia2 = form.cleaned_data['avalistalquilerprovincia2']
            avalistalquilercodigopostal2 = form.cleaned_data['avalistalquilercodigopostal2']
            avalistalquilerpaga3 = form.cleaned_data['avalistalquilerpaga3']
            avalistalquilermetros3 = form.cleaned_data['avalistalquilermetros3']
            avalistalquilerdireccion3 = form.cleaned_data['avalistalquilerdireccion3']
            avalistalquilerpoblacion3 = form.cleaned_data['avalistalquilerpoblacion3']
            avalistalquilerprovincia3 = form.cleaned_data['avalistalquilerprovincia3']
            avalistalquilercodigopostal3 = form.cleaned_data['avalistalquilercodigopostal3']
            avalistaireccionpersonal = form.cleaned_data['avalistaireccionpersonal']
            avalistaoblacionpersonal = form.cleaned_data['avalistaoblacionpersonal']
            avalistarovinciapersonal = form.cleaned_data['avalistarovinciapersonal']
            avalistaodigopostalpersonal = form.cleaned_data['avalistaodigopostalpersonal']
            avalistareditotipo1 = form.cleaned_data['avalistareditotipo1']
            avalistareditotantoporciento1 = form.cleaned_data['avalistareditotantoporciento1']
            avalistareditoimporte1 = form.cleaned_data['avalistareditoimporte1']
            avalistareditocuota1 = form.cleaned_data['avalistareditocuota1']
            avalistareditoentidad1 = form.cleaned_data['avalistareditoentidad1']
            avalistareditotipo2 = form.cleaned_data['avalistareditotipo2']
            avalistareditotantoporciento2 = form.cleaned_data['avalistareditotantoporciento2']
            avalistareditoimporte2 = form.cleaned_data['avalistareditoimporte2']
            avalistareditocuota2 = form.cleaned_data['avalistareditocuota2']
            avalistareditoentidad2 = form.cleaned_data['avalistareditoentidad2']
            avalistareditotipo3 = form.cleaned_data['avalistareditotipo3']
            avalistareditotantoporciento3 = form.cleaned_data['avalistareditotantoporciento3']
            avalistareditoimporte3 = form.cleaned_data['avalistareditoimporte3']
            avalistareditocuota3 = form.cleaned_data['avalistareditocuota3']
            avalistareditoentidad3 = form.cleaned_data['avalistareditoentidad3']
            avalistaarjetacuota1 = form.cleaned_data['avalistaarjetacuota1']
            avalistaarjetaimporte1 = form.cleaned_data['avalistaarjetaimporte1']
            avalistaarjetaentidad1 = form.cleaned_data['avalistaarjetaentidad1']
            avalistaarjetacuota2 = form.cleaned_data['avalistaarjetacuota2']
            avalistaarjetaimporte2 = form.cleaned_data['avalistaarjetaimporte2']
            avalistaarjetaentidad2 = form.cleaned_data['avalistaarjetaentidad2']
            avalistaarjetacuota3 = form.cleaned_data['avalistaarjetacuota3']
            avalistaarjetaimporte3 = form.cleaned_data['avalistaarjetaimporte3']
            avalistaarjetaentidad3 = form.cleaned_data['avalistaarjetaentidad3']
            avalistaecivosimporte1 = form.cleaned_data['avalistaecivosimporte1']
            avalistaecivosimporte2 = form.cleaned_data['avalistaecivosimporte2']
            avalistaecivosimporte3 = form.cleaned_data['avalistaecivosimporte3']
            avalistaorosoimporte1 = form.cleaned_data['avalistaorosoimporte1']
            avalistaorosoquien1 = form.cleaned_data['avalistaorosoquien1']
            avalistaorosoimporte2 = form.cleaned_data['avalistaorosoimporte2']
            avalistaorosoquien2 = form.cleaned_data['avalistaorosoquien2']
            avalistaorosoimporte3 = form.cleaned_data['avalistaorosoimporte3']
            avalistaorosoquien3 = form.cleaned_data['avalistaorosoquien3']

            expedient = models.expediente.objects.create(numexp=numexp, tipo="Coche", fecha_hora=datayhora)
            persona = models.persona.objects.create(numexp=numexp, nombre=name, dni=dni, direccion=direccion,
                                                    email=email, telefono=telefono, movil=movil,
                                                    fechanacimiento=fechanacimiento,
                                                    nacionalidad=nacionalidad, estadocivil=estadocivil,
                                                    tipocasado=tipocasado, numerodehijos=numerohijos,
                                                    sihijosmayores18=mayoresdeedad, sihijoscuantoscargo=cuantosacargo,
                                                    sihijosingreso=ingresohijos, justificante=justificante,
                                                    autoriza=autorizacion, medio=medio, metodopago=metodopago)
            personaanexos = models.personaanexos.objects.create(numexp=numexp, seguridadsocial=cotizacion,
                                                                siajenatipo=tipotrabajo,
                                                                siajenatemporal=finalizacontrato,
                                                                otrosingresos=otrosingresos,
                                                                otrosingresostexto=otrosingresostexto,
                                                                otrosgastos=otrosgastos,
                                                                otrosgastostexto=otrosgastostexto)
            paro = models.paro.objectos.create(numexp=numexp, desdecuando=parodesdecuando, cobra=parocuantocobra)
            juvilacion = models.juvilacion.objetos.create(numexp, importe=importejuvilacion,
                                                          pagas=numerodepagasjuvilacion, fechainicio=iniciojuvilacion,
                                                          fechafin=finjuvilacion)
            anotaciones = models.anotaciones.objects.create(numexp=numexp, personales=anotacionespersonales,
                                                            empresa=anotacionesingresos, vivienda=anotacionesviviendas,
                                                            financieros=anotacionesfinancieras,
                                                            destinado=anotacionesdestinado,
                                                            avalista=anotacionesavalista)

            if viviendadireccion1:
                vivienda = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion1,
                                                          poblacion=viviendapoblacion1, provincia=viviendaprovincia1,
                                                          codigopostal=viviendacodigopostal1,
                                                          valorvivienda=viviendavalor1,
                                                          valorhipoteca=viviendavalorhipoteca1,
                                                          estapagada=viviendaestapagada1, sinopagadaanos=viviendaanos1,
                                                          sinopagadaentidad=viviendaentidad1,
                                                          sinopagadapagahipoteca=viviendacuotamensual1,
                                                          librecargos=viviendalibredecargos1, metros=viviendametros1,
                                                          porciento=viviendaporciento1)

            if viviendadireccion2:
                vivienda2 = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion2,
                                                           poblacion=viviendapoblacion2, provincia=viviendaprovincia2,
                                                           codigopostal=viviendacodigopostal2,
                                                           valorvivienda=viviendavalor2,
                                                           valorhipoteca=viviendavalorhipoteca2,
                                                           estapagada=viviendaestapagada2, sinopagadaanos=viviendaanos2,
                                                           sinopagadaentidad=viviendaentidad2,
                                                           sinopagadapagahipoteca=viviendacuotamensual2,
                                                           librecargos=viviendalibredecargos2, metros=viviendametros2,
                                                           porciento=viviendaporciento2)

            if viviendadireccion3:
                vivienda3 = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion3,
                                                           poblacion=viviendapoblacion3, provincia=viviendaprovincia3,
                                                           codigopostal=viviendacodigopostal3,
                                                           valorvivienda=viviendavalor3,
                                                           valorhipoteca=viviendavalorhipoteca3,
                                                           estapagada=viviendaestapagada3, sinopagadaanos=viviendaanos3,
                                                           sinopagadaentidad=viviendaentidad3,
                                                           sinopagadapagahipoteca=viviendacuotamensual3,
                                                           librecargos=viviendalibredecargos3, metros=viviendametros3,
                                                           porciento=viviendaporciento3)

            if viviendaalquiladadireccion1:
                viviendaalquilada = models.vivienda.objects.create(numexp=numexp, direccion=viviendaalquiladadireccion1,
                                                                   poblacion=viviendaalquiladapoblacion1,
                                                                   provincia=viviendaalquiladaprovincia1,
                                                                   codigopostal=viviendaalquiladacodigopostal1,
                                                                   valorvivienda=viviendaalquiladavalor1,
                                                                   valorhipoteca=viviendaalquiladavalorhipoteca1,
                                                                   estapagada=viviendaalquiladaestapagada1,
                                                                   sinopagadaanos=viviendaalquiladaanos1,
                                                                   sinopagadaentidad=viviendaalquiladaentidad1,
                                                                   librecargos=viviendaalquiladalibredecargos1,
                                                                   metros=viviendaalquiladametros1,
                                                                   porciento=viviendaalquiladaporciento1,
                                                                   valoralquilada=viviendaalquiladacobraalquiler1,
                                                                   sinopagadapagahipoteca=viviendaalquiladacuotamensual1)

            if viviendaalquiladadireccion2:
                viviendaalquilada2 = models.vivienda.objects.create(numexp=numexp,
                                                                    direccion=viviendaalquiladadireccion2,
                                                                    poblacion=viviendaalquiladapoblacion2,
                                                                    provincia=viviendaalquiladaprovincia2,
                                                                    codigopostal=viviendaalquiladacodigopostal2,
                                                                    valorvivienda=viviendaalquiladavalor2,
                                                                    valorhipoteca=viviendaalquiladavalorhipoteca2,
                                                                    estapagada=viviendaalquiladaestapagada2,
                                                                    sinopagadaanos=viviendaalquiladaanos2,
                                                                    sinopagadaentidad=viviendaalquiladaentidad2,
                                                                    librecargos=viviendaalquiladalibredecargos2,
                                                                    metros=viviendaalquiladametros2,
                                                                    porciento=viviendaalquiladaporciento2,
                                                                    valoralquilada=viviendaalquiladacobraalquiler2,
                                                                    sinopagadapagahipoteca=viviendaalquiladacuotamensual2)

            if viviendaalquiladadireccion3:
                viviendaalquilada3 = models.vivienda.objects.create(numexp=numexp,
                                                                    direccion=viviendaalquiladadireccion3,
                                                                    poblacion=viviendaalquiladapoblacion3,
                                                                    provincia=viviendaalquiladaprovincia3,
                                                                    codigopostal=viviendaalquiladacodigopostal3,
                                                                    valorvivienda=viviendaalquiladavalor3,
                                                                    valorhipoteca=viviendaalquiladavalorhipoteca3,
                                                                    estapagada=viviendaalquiladaestapagada3,
                                                                    sinopagadaanos=viviendaalquiladaanos3,
                                                                    sinopagadaentidad=viviendaalquiladaentidad3,
                                                                    librecargos=viviendaalquiladalibredecargos3,
                                                                    metros=viviendaalquiladametros3,
                                                                    porciento=viviendaalquiladaporciento3,
                                                                    valoralquilada=viviendaalquiladacobraalquiler3,
                                                                    sinopagadapagahipoteca=viviendaalquiladacuotamensual3)

            if alquilerdireccion1:
                alquiler = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion1,
                                                          poblacion=alquilerpoblacion1, provincia=alquilerprovincia1,
                                                          codigopostal=alquilercodigopostal1, metros=alquilermetros1,
                                                          pagaalquiler=alquilerpaga1)

            if alquilerdireccion2:
                alquiler2 = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion2,
                                                           poblacion=alquilerpoblacion2, provincia=alquilerprovincia2,
                                                           codigopostal=alquilercodigopostal2, metros=alquilermetros2,
                                                           pagaalquiler=alquilerpaga2)

            if alquilerdireccion3:
                alquiler3 = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion3,
                                                           poblacion=alquilerpoblacion3, provincia=alquilerprovincia3,
                                                           codigopostal=alquilercodigopostal3, metros=alquilermetros3,
                                                           pagaalquiler=alquilerpaga3)

            if direccionpersonal:
                vivienda = models.vivienda.objects.create(numexp=numexp, direccion=direccionpersonal,
                                                          poblacion=poblacionpersonal, provincia=provinciapersonal,
                                                          codigopostal=codigopostalpersonal)

            if nombreempresa1:
                empresa = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa1, cargo=cargoempresa1,
                                                        actividad=actividadempresa1, ingresos=ingresosempresa1,
                                                        pagas=pagasempresa1, otrosingresos=otrosingresosempresa1,
                                                        antiguedad=antiguedadempresa1)

            if nombreempresa2:
                empresa2 = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa2, cargo=cargoempresa2,
                                                         actividad=actividadempresa2, ingresos=ingresosempresa2,
                                                         pagas=pagasempresa2, otrosingresos=otrosingresosempresa2,
                                                         antiguedad=antiguedadempresa2)

            if nombreempresa3:
                empresa3 = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa3, cargo=cargoempresa3,
                                                         actividad=actividadempresa3, ingresos=ingresosempresa3,
                                                         pagas=pagasempresa3, otrosingresos=otrosingresosempresa3,
                                                         antiguedad=antiguedadempresa3)

            if creditotipo1:
                debecredito1 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo1,
                                                                 porcientoavalista=creditotantoporciento1,
                                                                 importe=creditoimporte1, cuota=creditocuota1,
                                                                 entidad=creditoentidad1)
            if creditotipo2:
                debecredito2 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo2,
                                                                 porcientoavalista=creditotantoporciento2,
                                                                 importe=creditoimporte2, cuota=creditocuota2,
                                                                 entidad=creditoentidad2)
            if creditotipo3:
                debecredito3 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo3,
                                                                 porcientoavalista=creditotantoporciento3,
                                                                 importe=creditoimporte3, cuota=creditocuota3,
                                                                 entidad=creditoentidad3)
            if tarjetacuota1:
                debetarjeta1 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota1,
                                                                 importe=tarjetaimporte1,
                                                                 entidad=tarjetaentidad1)
            if tarjetacuota2:
                debetarjeta2 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota2,
                                                                 importe=tarjetaimporte2,
                                                                 entidad=tarjetaentidad2)
            if tarjetacuota3:
                debetarjeta3 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota3,
                                                                 importe=tarjetaimporte3,
                                                                 entidad=tarjetaentidad3)
            if recivosimporte1:
                deberecivo1s = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte1)
            if recivosimporte2:
                deberecivos2 = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte2)
            if recivosimporte3:
                deberecivos3 = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte3)
            if morosoimporte1:
                debemoroso1 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte1,
                                                               quien=morosoquien1)
            if morosoimporte2:
                debemoroso2 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte2,
                                                               quien=morosoquien2)
            if morosoimporte3:
                debemoroso3 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte3,
                                                               quien=morosoquien3)

            avalpersona = models.persona.objects.create(numexp=numexp, nombre=avalistaame, avalista=True,
                                                        dni=avalistani,
                                                        direccion=avalistaireccion, email=avalistamail,
                                                        telefono=avalistaelefono, movil=avalistaovil,
                                                        fechanacimiento=avalistaechanacimiento,
                                                        nacionalidad=avalistaacionalidad,
                                                        estadocivil=avalistastadocivil,
                                                        tipocasado=avalistaipocasado, numerodehijos=avalistaumerohijos,
                                                        sihijosmayores18=avalistaayoresdeedad,
                                                        sihijoscuantoscargo=avalistauantosacargo,
                                                        sihijosingreso=avalistangresohijos)
            avalpersonaanexos = models.personaanexos.objects.create(numexp=numexp, avalista=True,
                                                                    seguridadsocial=avalistaotizacion,
                                                                    siajenatipo=avalistaipotrabajo,
                                                                    siajenatemporal=avalistainalizacontrato,
                                                                    otrosingresos=avalistatrosingresos,
                                                                    otrosingresostexto=avalistatrosingresostexto,
                                                                    otrosgastos=avalistatrosgastos,
                                                                    otrosgastostexto=avalistatrosgastostexto)
            avalparo = models.paro.objectos.create(numexp=numexp, avalista=True, desdecuando=avalistaarodesdecuando,
                                                   cobra=avalistaarocuantocobra)
            avaljuvilacion = models.juvilacion.objetos.create(numexp, avalista=True, importe=avalistamportejuvilacion,
                                                              pagas=avalistaumerodepagasjuvilacion,
                                                              fechainicio=avalistaniciojuvilacion,
                                                              fechafin=avalistainjuvilacion)

            if avalistaiviendadireccion1:
                avalvivienda = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                              direccion=avalistaiviendadireccion1,
                                                              poblacion=avalistaiviendapoblacion1,
                                                              provincia=avalistaiviendaprovincia1,
                                                              codigopostal=avalistaiviendacodigopostal1,
                                                              valorvivienda=avalistaiviendavalor1,
                                                              valorhipoteca=avalistaiviendavalorhipoteca1,
                                                              estapagada=avalistaiviendaestapagada1,
                                                              sinopagadaanos=avalistaiviendaanos1,
                                                              sinopagadaentidad=avalistaiviendaentidad1,
                                                              sinopagadapagahipoteca=avalistaiviendacuotamensual1,
                                                              librecargos=avalistaiviendalibredecargos1,
                                                              metros=avalistaiviendametros1,
                                                              porciento=avalistaiviendaporciento1)

            if avalistaiviendadireccion2:
                avalvivienda2 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                               direccion=avalistaiviendadireccion2,
                                                               poblacion=avalistaiviendapoblacion2,
                                                               provincia=avalistaiviendaprovincia2,
                                                               codigopostal=avalistaiviendacodigopostal2,
                                                               valorvivienda=avalistaiviendavalor2,
                                                               valorhipoteca=avalistaiviendavalorhipoteca2,
                                                               estapagada=avalistaiviendaestapagada2,
                                                               sinopagadaanos=avalistaiviendaanos2,
                                                               sinopagadaentidad=avalistaiviendaentidad2,
                                                               sinopagadapagahipoteca=avalistaiviendacuotamensual2,
                                                               librecargos=avalistaiviendalibredecargos2,
                                                               metros=avalistaiviendametros2,
                                                               porciento=avalistaiviendaporciento2)

            if avalistaiviendadireccion3:
                avalvivienda3 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                               direccion=avalistaiviendadireccion3,
                                                               poblacion=avalistaiviendapoblacion3,
                                                               provincia=avalistaiviendaprovincia3,
                                                               codigopostal=avalistaiviendacodigopostal3,
                                                               valorvivienda=avalistaiviendavalor3,
                                                               valorhipoteca=avalistaiviendavalorhipoteca3,
                                                               estapagada=avalistaiviendaestapagada3,
                                                               sinopagadaanos=avalistaiviendaanos3,
                                                               sinopagadaentidad=avalistaiviendaentidad3,
                                                               sinopagadapagahipoteca=avalistaiviendacuotamensual3,
                                                               librecargos=avalistaiviendalibredecargos3,
                                                               metros=avalistaiviendametros3,
                                                               porciento=avalistaiviendaporciento3)

            if avalistaiviendaalquiladadireccion1:
                avalviviendaalquilada = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                                       direccion=avalistaiviendaalquiladadireccion1,
                                                                       poblacion=avalistaiviendaalquiladapoblacion1,
                                                                       provincia=avalistaiviendaalquiladaprovincia1,
                                                                       codigopostal=avalistaiviendaalquiladacodigopostal1,
                                                                       valorvivienda=avalistaiviendaalquiladavalor1,
                                                                       valorhipoteca=avalistaiviendaalquiladavalorhipoteca1,
                                                                       estapagada=avalistaiviendaalquiladaestapagada1,
                                                                       sinopagadaanos=avalistaiviendaalquiladaanos1,
                                                                       sinopagadaentidad=avalistaiviendaalquiladaentidad1,
                                                                       librecargos=avalistaiviendaalquiladalibredecargos1,
                                                                       metros=avalistaiviendaalquiladametros1,
                                                                       porciento=avalistaiviendaalquiladaporciento1,
                                                                       valoralquilada=avalistaiviendaalquiladacobraalquiler1,
                                                                       sinopagadapagahipoteca=avalistaiviendaalquiladacuotamensual1)

            if avalistaiviendaalquiladadireccion2:
                avalviviendaalquilada2 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                                        direccion=avalistaiviendaalquiladadireccion2,
                                                                        poblacion=avalistaiviendaalquiladapoblacion2,
                                                                        provincia=avalistaiviendaalquiladaprovincia2,
                                                                        codigopostal=avalistaiviendaalquiladacodigopostal2,
                                                                        valorvivienda=avalistaiviendaalquiladavalor2,
                                                                        valorhipoteca=avalistaiviendaalquiladavalorhipoteca2,
                                                                        estapagada=avalistaiviendaalquiladaestapagada2,
                                                                        sinopagadaanos=avalistaiviendaalquiladaanos2,
                                                                        sinopagadaentidad=avalistaiviendaalquiladaentidad2,
                                                                        librecargos=avalistaiviendaalquiladalibredecargos2,
                                                                        metros=avalistaiviendaalquiladametros2,
                                                                        porciento=avalistaiviendaalquiladaporciento2,
                                                                        valoralquilada=avalistaiviendaalquiladacobraalquiler2,
                                                                        sinopagadapagahipoteca=avalistaiviendaalquiladacuotamensual2)

            if avalistaiviendaalquiladadireccion3:
                avalviviendaalquilada3 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                                        direccion=avalistaiviendaalquiladadireccion3,
                                                                        poblacion=avalistaiviendaalquiladapoblacion3,
                                                                        provincia=avalistaiviendaalquiladaprovincia3,
                                                                        codigopostal=avalistaiviendaalquiladacodigopostal3,
                                                                        valorvivienda=avalistaiviendaalquiladavalor3,
                                                                        valorhipoteca=avalistaiviendaalquiladavalorhipoteca3,
                                                                        estapagada=avalistaiviendaalquiladaestapagada3,
                                                                        sinopagadaanos=avalistaiviendaalquiladaanos3,
                                                                        sinopagadaentidad=avalistaiviendaalquiladaentidad3,
                                                                        librecargos=avalistaiviendaalquiladalibredecargos3,
                                                                        metros=avalistaiviendaalquiladametros3,
                                                                        porciento=avalistaiviendaalquiladaporciento3,
                                                                        valoralquilada=avalistaiviendaalquiladacobraalquiler3,
                                                                        sinopagadapagahipoteca=avalistaiviendaalquiladacuotamensual3)

            if avalistalquilerdireccion1:
                avalalquiler = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                              direccion=avalistalquilerdireccion1,
                                                              poblacion=avalistalquilerpoblacion1,
                                                              provincia=avalistalquilerprovincia1,
                                                              codigopostal=avalistalquilercodigopostal1,
                                                              metros=avalistalquilermetros1,
                                                              pagaalquiler=avalistalquilerpaga1)

            if avalistalquilerdireccion2:
                avalalquiler2 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                               direccion=avalistalquilerdireccion2,
                                                               poblacion=avalistalquilerpoblacion2,
                                                               provincia=avalistalquilerprovincia2,
                                                               codigopostal=avalistalquilercodigopostal2,
                                                               metros=avalistalquilermetros2,
                                                               pagaalquiler=avalistalquilerpaga2)

            if avalistalquilerdireccion3:
                avalalquiler3 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                               direccion=avalistalquilerdireccion3,
                                                               poblacion=avalistalquilerpoblacion3,
                                                               provincia=avalistalquilerprovincia3,
                                                               codigopostal=avalistalquilercodigopostal3,
                                                               metros=avalistalquilermetros3,
                                                               pagaalquiler=avalistalquilerpaga3)

            if avalistaireccionpersonal:
                avalvivienda = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                              direccion=avalistaireccionpersonal,
                                                              poblacion=avalistaoblacionpersonal,
                                                              provincia=avalistarovinciapersonal,
                                                              codigopostal=avalistaodigopostalpersonal)

            if avalistaombreempresa1:
                avalempresa = models.empresa.objects.create(numexp=numexp, avalista=True,
                                                            nombre=avalistaombreempresa1, cargo=avalistaargoempresa1,
                                                            actividad=avalistactividadempresa1,
                                                            ingresos=avalistangresosempresa1,
                                                            pagas=avalistaagasempresa1,
                                                            otrosingresos=avalistatrosingresosempresa1,
                                                            antiguedad=avalistantiguedadempresa1)

            if avalistaombreempresa2:
                avalempresa2 = models.empresa.objects.create(numexp=numexp, avalista=True,
                                                             nombre=avalistaombreempresa2, cargo=avalistaargoempresa2,
                                                             actividad=avalistactividadempresa2,
                                                             ingresos=avalistangresosempresa2,
                                                             pagas=avalistaagasempresa2,
                                                             otrosingresos=avalistatrosingresosempresa2,
                                                             antiguedad=avalistantiguedadempresa2)

            if avalistaombreempresa3:
                avalempresa3 = models.empresa.objects.create(numexp=numexp, avalista=True,
                                                             nombre=avalistaombreempresa3, cargo=avalistaargoempresa3,
                                                             actividad=avalistactividadempresa3,
                                                             ingresos=avalistangresosempresa3,
                                                             pagas=avalistaagasempresa3,
                                                             otrosingresos=avalistatrosingresosempresa3,
                                                             antiguedad=avalistantiguedadempresa3)

            if avalistareditotipo1:
                avaldebecredito1 = models.debecredito.objetos.create(numexp=numexp, avalista=True,
                                                                     tipo=avalistareditotipo1,
                                                                     porcientoavalista=avalistareditotantoporciento1,
                                                                     importe=avalistareditoimporte1,
                                                                     cuota=avalistareditocuota1,
                                                                     entidad=avalistareditoentidad1)
            if avalistareditotipo2:
                avaldebecredito2 = models.debecredito.objetos.create(numexp=numexp, avalista=True,
                                                                     tipo=avalistareditotipo2,
                                                                     porcientoavalista=avalistareditotantoporciento2,
                                                                     importe=avalistareditoimporte2,
                                                                     cuota=avalistareditocuota2,
                                                                     entidad=avalistareditoentidad2)
            if avalistareditotipo3:
                avaldebecredito3 = models.debecredito.objetos.create(numexp=numexp, avalista=True,
                                                                     tipo=avalistareditotipo3,
                                                                     porcientoavalista=avalistareditotantoporciento3,
                                                                     importe=avalistareditoimporte3,
                                                                     cuota=avalistareditocuota3,
                                                                     entidad=avalistareditoentidad3)
            if avalistaarjetacuota1:
                avaldebetarjeta1 = models.debetarjeta.objetos.create(numexp=numexp, avalista=True,
                                                                     cuota=avalistaarjetacuota1,
                                                                     importe=avalistaarjetaimporte1,
                                                                     entidad=avalistaarjetaentidad1)
            if avalistaarjetacuota2:
                avaldebetarjeta2 = models.debetarjeta.objetos.create(numexp=numexp, avalista=True,
                                                                     cuota=avalistaarjetacuota2,
                                                                     importe=avalistaarjetaimporte2,
                                                                     entidad=avalistaarjetaentidad2)
            if avalistaarjetacuota3:
                avaldebetarjeta3 = models.debetarjeta.objetos.create(numexp=numexp, avalista=True,
                                                                     cuota=avalistaarjetacuota3,
                                                                     importe=avalistaarjetaimporte3,
                                                                     entidad=avalistaarjetaentidad3)
            if avalistaecivosimporte1:
                avaldeberecivo1s = models.deberecivos.objetos.create(numexp=numexp, avalista=True,
                                                                     importe=avalistaecivosimporte1)
            if avalistaecivosimporte2:
                avaldeberecivos2 = models.deberecivos.objetos.create(numexp=numexp, avalista=True,
                                                                     importe=avalistaecivosimporte2)
            if avalistaecivosimporte3:
                avaldeberecivos3 = models.deberecivos.objetos.create(numexp=numexp, avalista=True,
                                                                     importe=avalistaecivosimporte3)
            if avalistaorosoimporte1:
                avaldebemoroso1 = models.debemoroso.objects.create(numexp=numexp, avalista=True,
                                                                   importe=avalistaorosoimporte1,
                                                                   quien=avalistaorosoquien1)
            if avalistaorosoimporte2:
                avaldebemoroso2 = models.debemoroso.objects.create(numexp=numexp, avalista=True,
                                                                   importe=avalistaorosoimporte2,
                                                                   quien=avalistaorosoquien2)
            if avalistaorosoimporte3:
                avaldebemoroso3 = models.debemoroso.objects.create(numexp=numexp, avalista=True,
                                                                   importe=avalistaorosoimporte3,
                                                                   quien=avalistaorosoquien3)

            return HttpResponseRedirect('/formularios/')
        else:
            print form.errors
    else:
        form = forms.formPersonal()
        lastNum = models.expediente.objects.all().order_by("numexp").last()
        if not lastNum:
            lastNum = 40000
        else:
            lastNum += 1
        form.fields["numexp"].initial = lastNum
        form.fields["datayhora"].initial = datetime.now()
        context.update({"form": form})
        return render(request, 'form_person.html', context)


def hipotecario(request):
    context = {}
    if request.method == 'POST':
        form = forms.formHipotecario(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dni = form.cleaned_data['dni']
            direccion = form.cleaned_data['direccion']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            movil = form.cleaned_data['movil']
            fechanacimiento = form.cleaned_data['fechanacimiento']
            nacionalidad = form.cleaned_data['nacionalidad']
            estadocivil = form.cleaned_data['estadocivil']
            tipocasado = form.cleaned_data['tipocasado']
            numerohijos = form.cleaned_data['numerohijos']
            mayoresdeedad = form.cleaned_data['mayoresdeedad']
            cuantosacargo = form.cleaned_data['cuantosacargo']
            ingresohijos = form.cleaned_data['ingresohijos']
            anotacionespersonales = form.cleaned_data['anotacionespersonales']
            cotizacion = form.cleaned_data['cotizacion']
            tipotrabajo = form.cleaned_data['tipotrabajo']
            finalizacontrato = form.cleaned_data['finalizacontrato']
            nombreempresa1 = form.cleaned_data['nombreempresa1']
            cargoempresa1 = form.cleaned_data['cargoempresa1']
            actividadempresa1 = form.cleaned_data['actividadempresa1']
            ingresosempresa1 = form.cleaned_data['ingresosempresa1']
            pagasempresa1 = form.cleaned_data['pagasempresa1']
            otrosingresosempresa1 = form.cleaned_data['otrosingresosempresa1']
            antiguedadempresa1 = form.cleaned_data['antiguedadempresa1']
            nombreempresa2 = form.cleaned_data['nombreempresa2']
            cargoempresa2 = form.cleaned_data['cargoempresa2']
            actividadempresa2 = form.cleaned_data['actividadempresa2']
            ingresosempresa2 = form.cleaned_data['ingresosempresa2']
            pagasempresa2 = form.cleaned_data['pagasempresa2']
            otrosingresosempresa2 = form.cleaned_data['otrosingresosempresa2']
            antiguedadempresa2 = form.cleaned_data['antiguedadempresa2']
            nombreempresa3 = form.cleaned_data['nombreempresa3']
            cargoempresa3 = form.cleaned_data['cargoempresa3']
            actividadempresa3 = form.cleaned_data['actividadempresa3']
            ingresosempresa3 = form.cleaned_data['ingresosempresa3']
            pagasempresa3 = form.cleaned_data['pagasempresa3']
            otrosingresosempresa3 = form.cleaned_data['otrosingresosempresa3']
            antiguedadempresa3 = form.cleaned_data['antiguedadempresa3']
            importejuvilacion = form.cleaned_data['importejuvilacion']
            numerodepagasjuvilacion = form.cleaned_data['numerodepagasjuvilacion']
            iniciojuvilacion = form.cleaned_data['iniciojuvilacion']
            finjuvilacion = form.cleaned_data['finjuvilacion']
            parodesdecuando = form.cleaned_data['parodesdecuando']
            parocuantocobra = form.cleaned_data['parocuantocobra']
            otrosingresos = form.cleaned_data['otrosingresos']
            otrosgastos = form.cleaned_data['otrosgastos']
            otrosingresostexto = form.cleaned_data['otrosingresostexto']
            otrosgastostexto = form.cleaned_data['otrosgastostexto']
            anotacionesingresos = form.cleaned_data['anotacionesingresos']
            viviendavalor1 = form.cleaned_data['viviendavalor1']
            viviendavalorhipoteca1 = form.cleaned_data['viviendavalorhipoteca1']
            viviendaestapagada1 = form.cleaned_data['viviendaestapagada1']
            viviendalibredecargos1 = form.cleaned_data['viviendalibredecargos1']
            viviendacuotamensual1 = form.cleaned_data['viviendacuotamensual1']
            viviendaanos1 = form.cleaned_data['viviendaanos1']
            viviendaentidad1 = form.cleaned_data['viviendaentidad1']
            viviendametros1 = form.cleaned_data['viviendametros1']
            viviendaporciento1 = form.cleaned_data['viviendaporciento1']
            viviendadireccion1 = form.cleaned_data['viviendadireccion1']
            viviendapoblacion1 = form.cleaned_data['viviendapoblacion1']
            viviendaprovincia1 = form.cleaned_data['viviendaprovincia1']
            viviendacodigopostal1 = form.cleaned_data['viviendacodigopostal1']
            viviendavalor2 = form.cleaned_data['viviendavalor2']
            viviendavalorhipoteca2 = form.cleaned_data['viviendavalorhipoteca2']
            viviendaestapagada2 = form.cleaned_data['viviendaestapagada2']
            viviendalibredecargos2 = form.cleaned_data['viviendalibredecargos2']
            viviendacuotamensual2 = form.cleaned_data['viviendacuotamensual2']
            viviendaanos2 = form.cleaned_data['viviendaanos2']
            viviendaentidad2 = form.cleaned_data['viviendaentidad2']
            viviendametros2 = form.cleaned_data['viviendametros2']
            viviendaporciento2 = form.cleaned_data['viviendaporciento2']
            viviendadireccion2 = form.cleaned_data['viviendadireccion2']
            viviendapoblacion2 = form.cleaned_data['viviendapoblacion2']
            viviendaprovincia2 = form.cleaned_data['viviendaprovincia2']
            viviendacodigopostal2 = form.cleaned_data['viviendacodigopostal2']
            viviendavalor3 = form.cleaned_data['viviendavalor3']
            viviendavalorhipoteca3 = form.cleaned_data['viviendavalorhipoteca3']
            viviendaestapagada3 = form.cleaned_data['viviendaestapagada3']
            viviendalibredecargos3 = form.cleaned_data['viviendalibredecargos3']
            viviendacuotamensual3 = form.cleaned_data['viviendacuotamensual3']
            viviendaanos3 = form.cleaned_data['viviendaanos3']
            viviendaentidad3 = form.cleaned_data['viviendaentidad3']
            viviendametros3 = form.cleaned_data['viviendametros3']
            viviendaporciento3 = form.cleaned_data['viviendaporciento3']
            viviendadireccion3 = form.cleaned_data['viviendadireccion3']
            viviendapoblacion3 = form.cleaned_data['viviendapoblacion3']
            viviendaprovincia3 = form.cleaned_data['viviendaprovincia3']
            viviendacodigopostal3 = form.cleaned_data['viviendacodigopostal3']
            viviendaalquiladavalor1 = form.cleaned_data['viviendaalquiladavalor1']
            viviendaalquiladavalorhipoteca1 = form.cleaned_data['viviendaalquiladavalorhipoteca1']
            viviendaalquiladaestapagada1 = form.cleaned_data['viviendaalquiladaestapagada1']
            viviendaalquiladalibredecargos1 = form.cleaned_data['viviendaalquiladalibredecargos1']
            viviendaalquiladacuotamensual1 = form.cleaned_data['viviendaalquiladacuotamensual1']
            viviendaalquiladaanos1 = form.cleaned_data['viviendaalquiladaanos1']
            viviendaalquiladaentidad1 = form.cleaned_data['viviendaalquiladaentidad1']
            viviendaalquiladametros1 = form.cleaned_data['viviendaalquiladametros1']
            viviendaalquiladaporciento1 = form.cleaned_data['viviendaalquiladaporciento1']
            viviendaalquiladadireccion1 = form.cleaned_data['viviendaalquiladadireccion1']
            viviendaalquiladapoblacion1 = form.cleaned_data['viviendaalquiladapoblacion1']
            viviendaalquiladaprovincia1 = form.cleaned_data['viviendaalquiladaprovincia1']
            viviendaalquiladacodigopostal1 = form.cleaned_data['viviendaalquiladacodigopostal1']
            viviendaalquiladacobraalquiler1 = form.cleaned_data['viviendaalquiladacobraalquiler1']
            viviendaalquiladavalor2 = form.cleaned_data['viviendaalquiladavalor2']
            viviendaalquiladavalorhipoteca2 = form.cleaned_data['viviendaalquiladavalorhipoteca2']
            viviendaalquiladaestapagada2 = form.cleaned_data['viviendaalquiladaestapagada2']
            viviendaalquiladalibredecargos2 = form.cleaned_data['viviendaalquiladalibredecargos2']
            viviendaalquiladacuotamensual2 = form.cleaned_data['viviendaalquiladacuotamensual2']
            viviendaalquiladaanos2 = form.cleaned_data['viviendaalquiladaanos2']
            viviendaalquiladaentidad2 = form.cleaned_data['viviendaalquiladaentidad2']
            viviendaalquiladametros2 = form.cleaned_data['viviendaalquiladametros2']
            viviendaalquiladaporciento2 = form.cleaned_data['viviendaalquiladaporciento2']
            viviendaalquiladadireccion2 = form.cleaned_data['viviendaalquiladadireccion2']
            viviendaalquiladapoblacion2 = form.cleaned_data['viviendaalquiladapoblacion2']
            viviendaalquiladaprovincia2 = form.cleaned_data['viviendaalquiladaprovincia2']
            viviendaalquiladacodigopostal2 = form.cleaned_data['viviendaalquiladacodigopostal2']
            viviendaalquiladacobraalquiler2 = form.cleaned_data['viviendaalquiladacobraalquiler2']
            viviendaalquiladavalor3 = form.cleaned_data['viviendaalquiladavalor3']
            viviendaalquiladavalorhipoteca3 = form.cleaned_data['viviendaalquiladavalorhipoteca3']
            viviendaalquiladaestapagada3 = form.cleaned_data['viviendaalquiladaestapagada3']
            viviendaalquiladalibredecargos3 = form.cleaned_data['viviendaalquiladalibredecargos3']
            viviendaalquiladacuotamensual3 = form.cleaned_data['viviendaalquiladacuotamensual3']
            viviendaalquiladaanos3 = form.cleaned_data['viviendaalquiladaanos3']
            viviendaalquiladaentidad3 = form.cleaned_data['viviendaalquiladaentidad3']
            viviendaalquiladametros3 = form.cleaned_data['viviendaalquiladametros3']
            viviendaalquiladaporciento3 = form.cleaned_data['viviendaalquiladaporciento3']
            viviendaalquiladadireccion3 = form.cleaned_data['viviendaalquiladadireccion3']
            viviendaalquiladapoblacion3 = form.cleaned_data['viviendaalquiladapoblacion3']
            viviendaalquiladaprovincia3 = form.cleaned_data['viviendaalquiladaprovincia3']
            viviendaalquiladacodigopostal3 = form.cleaned_data['viviendaalquiladacodigopostal3']
            viviendaalquiladacobraalquiler3 = form.cleaned_data['viviendaalquiladacobraalquiler3']
            alquilerpaga1 = form.cleaned_data['alquilerpaga1']
            alquilermetros1 = form.cleaned_data['alquilermetros1']
            alquilerdireccion1 = form.cleaned_data['alquilerdireccion1']
            alquilerpoblacion1 = form.cleaned_data['alquilerpoblacion1']
            alquilerprovincia1 = form.cleaned_data['alquilerprovincia1']
            alquilercodigopostal1 = form.cleaned_data['alquilercodigopostal1']
            alquilerpaga2 = form.cleaned_data['alquilerpaga2']
            alquilermetros2 = form.cleaned_data['alquilermetros2']
            alquilerdireccion2 = form.cleaned_data['alquilerdireccion2']
            alquilerpoblacion2 = form.cleaned_data['alquilerpoblacion2']
            alquilerprovincia2 = form.cleaned_data['alquilerprovincia2']
            alquilercodigopostal2 = form.cleaned_data['alquilercodigopostal2']
            alquilerpaga3 = form.cleaned_data['alquilerpaga3']
            alquilermetros3 = form.cleaned_data['alquilermetros3']
            alquilerdireccion3 = form.cleaned_data['alquilerdireccion3']
            alquilerpoblacion3 = form.cleaned_data['alquilerpoblacion3']
            alquilerprovincia3 = form.cleaned_data['alquilerprovincia3']
            alquilercodigopostal3 = form.cleaned_data['alquilercodigopostal3']
            direccionpersonal = form.cleaned_data['direccionpersonal']
            poblacionpersonal = form.cleaned_data['poblacionpersonal']
            provinciapersonal = form.cleaned_data['provinciapersonal']
            codigopostalpersonal = form.cleaned_data['codigopostalpersonal']
            anotacionesviviendas = form.cleaned_data['anotacionesviviendas']
            creditotipo1 = form.cleaned_data['creditotipo1']
            creditotantoporciento1 = form.cleaned_data['creditotantoporciento1']
            creditoimporte1 = form.cleaned_data['creditoimporte1']
            creditocuota1 = form.cleaned_data['creditocuota1']
            creditoentidad1 = form.cleaned_data['creditoentidad1']
            creditotipo2 = form.cleaned_data['creditotipo2']
            creditotantoporciento2 = form.cleaned_data['creditotantoporciento2']
            creditoimporte2 = form.cleaned_data['creditoimporte2']
            creditocuota2 = form.cleaned_data['creditocuota2']
            creditoentidad2 = form.cleaned_data['creditoentidad2']
            creditotipo3 = form.cleaned_data['creditotipo3']
            creditotantoporciento3 = form.cleaned_data['creditotantoporciento3']
            creditoimporte3 = form.cleaned_data['creditoimporte3']
            creditocuota3 = form.cleaned_data['creditocuota3']
            creditoentidad3 = form.cleaned_data['creditoentidad3']
            tarjetacuota1 = form.cleaned_data['tarjetacuota1']
            tarjetaimporte1 = form.cleaned_data['tarjetaimporte1']
            tarjetaentidad1 = form.cleaned_data['tarjetaentidad1']
            tarjetacuota2 = form.cleaned_data['tarjetacuota2']
            tarjetaimporte2 = form.cleaned_data['tarjetaimporte2']
            tarjetaentidad2 = form.cleaned_data['tarjetaentidad2']
            tarjetacuota3 = form.cleaned_data['tarjetacuota3']
            tarjetaimporte3 = form.cleaned_data['tarjetaimporte3']
            tarjetaentidad3 = form.cleaned_data['tarjetaentidad3']
            recivosimporte1 = form.cleaned_data['recivosimporte1']
            recivosimporte2 = form.cleaned_data['recivosimporte2']
            recivosimporte3 = form.cleaned_data['recivosimporte3']
            morosoimporte1 = form.cleaned_data['morosoimporte1']
            morosoquien1 = form.cleaned_data['morosoquien1']
            morosoimporte2 = form.cleaned_data['morosoimporte2']
            morosoquien2 = form.cleaned_data['morosoquien2']
            morosoimporte3 = form.cleaned_data['morosoimporte3']
            morosoquien3 = form.cleaned_data['morosoquien3']
            anotacionesfinancieras = form.cleaned_data['anotacionesfinancieras']
            anotacionesavalista = form.cleaned_data['anotacionesavalista']
            metodopago = form.cleaned_data['metodopago']
            anotacionesdestinado = form.cleaned_data['anotacionesdestinado']
            justificante = form.cleaned_data['justificante']
            autorizacion = form.cleaned_data['autorizacion']
            medio = form.cleaned_data['medio']
            numexp = form.cleaned_data['numexp']
            datayhora = form.cleaned_data['datayhora']
            avalistaame = form.cleaned_data['avalistaame']
            avalistani = form.cleaned_data['avalistani']
            avalistaireccion = form.cleaned_data['avalistaireccion']
            avalistamail = form.cleaned_data['avalistamail']
            avalistaelefono = form.cleaned_data['avalistaelefono']
            avalistaovil = form.cleaned_data['avalistaovil']
            avalistaechanacimiento = form.cleaned_data['avalistaechanacimiento']
            avalistaacionalidad = form.cleaned_data['avalistaacionalidad']
            avalistastadocivil = form.cleaned_data['avalistastadocivil']
            avalistaipocasado = form.cleaned_data['avalistaipocasado']
            avalistaumerohijos = form.cleaned_data['avalistaumerohijos']
            avalistaayoresdeedad = form.cleaned_data['avalistaayoresdeedad']
            avalistauantosacargo = form.cleaned_data['avalistauantosacargo']
            avalistangresohijos = form.cleaned_data['avalistangresohijos']
            avalistaotizacion = form.cleaned_data['avalistaotizacion']
            avalistaipotrabajo = form.cleaned_data['avalistaipotrabajo']
            avalistainalizacontrato = form.cleaned_data['avalistainalizacontrato']
            avalistaombreempresa1 = form.cleaned_data['avalistaombreempresa1']
            avalistaargoempresa1 = form.cleaned_data['avalistaargoempresa1']
            avalistactividadempresa1 = form.cleaned_data['avalistactividadempresa1']
            avalistangresosempresa1 = form.cleaned_data['avalistangresosempresa1']
            avalistaagasempresa1 = form.cleaned_data['avalistaagasempresa1']
            avalistatrosingresosempresa1 = form.cleaned_data['avalistatrosingresosempresa1']
            avalistantiguedadempresa1 = form.cleaned_data['avalistantiguedadempresa1']
            avalistaombreempresa2 = form.cleaned_data['avalistaombreempresa2']
            avalistaargoempresa2 = form.cleaned_data['avalistaargoempresa2']
            avalistactividadempresa2 = form.cleaned_data['avalistactividadempresa2']
            avalistangresosempresa2 = form.cleaned_data['avalistangresosempresa2']
            avalistaagasempresa2 = form.cleaned_data['avalistaagasempresa2']
            avalistatrosingresosempresa2 = form.cleaned_data['avalistatrosingresosempresa2']
            avalistantiguedadempresa2 = form.cleaned_data['avalistantiguedadempresa2']
            avalistaombreempresa3 = form.cleaned_data['avalistaombreempresa3']
            avalistaargoempresa3 = form.cleaned_data['avalistaargoempresa3']
            avalistactividadempresa3 = form.cleaned_data['avalistactividadempresa3']
            avalistangresosempresa3 = form.cleaned_data['avalistangresosempresa3']
            avalistaagasempresa3 = form.cleaned_data['avalistaagasempresa3']
            avalistatrosingresosempresa3 = form.cleaned_data['avalistatrosingresosempresa3']
            avalistantiguedadempresa3 = form.cleaned_data['avalistantiguedadempresa3']
            avalistamportejuvilacion = form.cleaned_data['avalistamportejuvilacion']
            avalistaumerodepagasjuvilacion = form.cleaned_data['avalistaumerodepagasjuvilacion']
            avalistaniciojuvilacion = form.cleaned_data['avalistaniciojuvilacion']
            avalistainjuvilacion = form.cleaned_data['avalistainjuvilacion']
            avalistaarodesdecuando = form.cleaned_data['avalistaarodesdecuando']
            avalistaarocuantocobra = form.cleaned_data['avalistaarocuantocobra']
            avalistatrosingresos = form.cleaned_data['avalistatrosingresos']
            avalistatrosgastos = form.cleaned_data['avalistatrosgastos']
            avalistatrosingresostexto = form.cleaned_data['avalistatrosingresostexto']
            avalistatrosgastostexto = form.cleaned_data['avalistatrosgastostexto']
            avalistaiviendavalor1 = form.cleaned_data['avalistaiviendavalor1']
            avalistaiviendavalorhipoteca1 = form.cleaned_data['avalistaiviendavalorhipoteca1']
            avalistaiviendaestapagada1 = form.cleaned_data['avalistaiviendaestapagada1']
            avalistaiviendalibredecargos1 = form.cleaned_data['avalistaiviendalibredecargos1']
            avalistaiviendacuotamensual1 = form.cleaned_data['avalistaiviendacuotamensual1']
            avalistaiviendaanos1 = form.cleaned_data['avalistaiviendaanos1']
            avalistaiviendaentidad1 = form.cleaned_data['avalistaiviendaentidad1']
            avalistaiviendametros1 = form.cleaned_data['avalistaiviendametros1']
            avalistaiviendaporciento1 = form.cleaned_data['avalistaiviendaporciento1']
            avalistaiviendadireccion1 = form.cleaned_data['avalistaiviendadireccion1']
            avalistaiviendapoblacion1 = form.cleaned_data['avalistaiviendapoblacion1']
            avalistaiviendaprovincia1 = form.cleaned_data['avalistaiviendaprovincia1']
            avalistaiviendacodigopostal1 = form.cleaned_data['avalistaiviendacodigopostal1']
            avalistaiviendavalor2 = form.cleaned_data['avalistaiviendavalor2']
            avalistaiviendavalorhipoteca2 = form.cleaned_data['avalistaiviendavalorhipoteca2']
            avalistaiviendaestapagada2 = form.cleaned_data['avalistaiviendaestapagada2']
            avalistaiviendalibredecargos2 = form.cleaned_data['avalistaiviendalibredecargos2']
            avalistaiviendacuotamensual2 = form.cleaned_data['avalistaiviendacuotamensual2']
            avalistaiviendaanos2 = form.cleaned_data['avalistaiviendaanos2']
            avalistaiviendaentidad2 = form.cleaned_data['avalistaiviendaentidad2']
            avalistaiviendametros2 = form.cleaned_data['avalistaiviendametros2']
            avalistaiviendaporciento2 = form.cleaned_data['avalistaiviendaporciento2']
            avalistaiviendadireccion2 = form.cleaned_data['avalistaiviendadireccion2']
            avalistaiviendapoblacion2 = form.cleaned_data['avalistaiviendapoblacion2']
            avalistaiviendaprovincia2 = form.cleaned_data['avalistaiviendaprovincia2']
            avalistaiviendacodigopostal2 = form.cleaned_data['avalistaiviendacodigopostal2']
            avalistaiviendavalor3 = form.cleaned_data['avalistaiviendavalor3']
            avalistaiviendavalorhipoteca3 = form.cleaned_data['avalistaiviendavalorhipoteca3']
            avalistaiviendaestapagada3 = form.cleaned_data['avalistaiviendaestapagada3']
            avalistaiviendalibredecargos3 = form.cleaned_data['avalistaiviendalibredecargos3']
            avalistaiviendacuotamensual3 = form.cleaned_data['avalistaiviendacuotamensual3']
            avalistaiviendaanos3 = form.cleaned_data['avalistaiviendaanos3']
            avalistaiviendaentidad3 = form.cleaned_data['avalistaiviendaentidad3']
            avalistaiviendametros3 = form.cleaned_data['avalistaiviendametros3']
            avalistaiviendaporciento3 = form.cleaned_data['avalistaiviendaporciento3']
            avalistaiviendadireccion3 = form.cleaned_data['avalistaiviendadireccion3']
            avalistaiviendapoblacion3 = form.cleaned_data['avalistaiviendapoblacion3']
            avalistaiviendaprovincia3 = form.cleaned_data['avalistaiviendaprovincia3']
            avalistaiviendacodigopostal3 = form.cleaned_data['avalistaiviendacodigopostal3']
            avalistaiviendaalquiladavalor1 = form.cleaned_data['avalistaiviendaalquiladavalor1']
            avalistaiviendaalquiladavalorhipoteca1 = form.cleaned_data['avalistaiviendaalquiladavalorhipoteca1']
            avalistaiviendaalquiladaestapagada1 = form.cleaned_data['avalistaiviendaalquiladaestapagada1']
            avalistaiviendaalquiladalibredecargos1 = form.cleaned_data['avalistaiviendaalquiladalibredecargos1']
            avalistaiviendaalquiladacuotamensual1 = form.cleaned_data['avalistaiviendaalquiladacuotamensual1']
            avalistaiviendaalquiladaanos1 = form.cleaned_data['avalistaiviendaalquiladaanos1']
            avalistaiviendaalquiladaentidad1 = form.cleaned_data['avalistaiviendaalquiladaentidad1']
            avalistaiviendaalquiladametros1 = form.cleaned_data['avalistaiviendaalquiladametros1']
            avalistaiviendaalquiladaporciento1 = form.cleaned_data['avalistaiviendaalquiladaporciento1']
            avalistaiviendaalquiladadireccion1 = form.cleaned_data['avalistaiviendaalquiladadireccion1']
            avalistaiviendaalquiladapoblacion1 = form.cleaned_data['avalistaiviendaalquiladapoblacion1']
            avalistaiviendaalquiladaprovincia1 = form.cleaned_data['avalistaiviendaalquiladaprovincia1']
            avalistaiviendaalquiladacodigopostal1 = form.cleaned_data['avalistaiviendaalquiladacodigopostal1']
            avalistaiviendaalquiladacobraalquiler1 = form.cleaned_data['avalistaiviendaalquiladacobraalquiler1']
            avalistaiviendaalquiladavalor2 = form.cleaned_data['avalistaiviendaalquiladavalor2']
            avalistaiviendaalquiladavalorhipoteca2 = form.cleaned_data['avalistaiviendaalquiladavalorhipoteca2']
            avalistaiviendaalquiladaestapagada2 = form.cleaned_data['avalistaiviendaalquiladaestapagada2']
            avalistaiviendaalquiladalibredecargos2 = form.cleaned_data['avalistaiviendaalquiladalibredecargos2']
            avalistaiviendaalquiladacuotamensual2 = form.cleaned_data['avalistaiviendaalquiladacuotamensual2']
            avalistaiviendaalquiladaanos2 = form.cleaned_data['avalistaiviendaalquiladaanos2']
            avalistaiviendaalquiladaentidad2 = form.cleaned_data['avalistaiviendaalquiladaentidad2']
            avalistaiviendaalquiladametros2 = form.cleaned_data['avalistaiviendaalquiladametros2']
            avalistaiviendaalquiladaporciento2 = form.cleaned_data['avalistaiviendaalquiladaporciento2']
            avalistaiviendaalquiladadireccion2 = form.cleaned_data['avalistaiviendaalquiladadireccion2']
            avalistaiviendaalquiladapoblacion2 = form.cleaned_data['avalistaiviendaalquiladapoblacion2']
            avalistaiviendaalquiladaprovincia2 = form.cleaned_data['avalistaiviendaalquiladaprovincia2']
            avalistaiviendaalquiladacodigopostal2 = form.cleaned_data['avalistaiviendaalquiladacodigopostal2']
            avalistaiviendaalquiladacobraalquiler2 = form.cleaned_data['avalistaiviendaalquiladacobraalquiler2']
            avalistaiviendaalquiladavalor3 = form.cleaned_data['avalistaiviendaalquiladavalor3']
            avalistaiviendaalquiladavalorhipoteca3 = form.cleaned_data['avalistaiviendaalquiladavalorhipoteca3']
            avalistaiviendaalquiladaestapagada3 = form.cleaned_data['avalistaiviendaalquiladaestapagada3']
            avalistaiviendaalquiladalibredecargos3 = form.cleaned_data['avalistaiviendaalquiladalibredecargos3']
            avalistaiviendaalquiladacuotamensual3 = form.cleaned_data['avalistaiviendaalquiladacuotamensual3']
            avalistaiviendaalquiladaanos3 = form.cleaned_data['avalistaiviendaalquiladaanos3']
            avalistaiviendaalquiladaentidad3 = form.cleaned_data['avalistaiviendaalquiladaentidad3']
            avalistaiviendaalquiladametros3 = form.cleaned_data['avalistaiviendaalquiladametros3']
            avalistaiviendaalquiladaporciento3 = form.cleaned_data['avalistaiviendaalquiladaporciento3']
            avalistaiviendaalquiladadireccion3 = form.cleaned_data['avalistaiviendaalquiladadireccion3']
            avalistaiviendaalquiladapoblacion3 = form.cleaned_data['avalistaiviendaalquiladapoblacion3']
            avalistaiviendaalquiladaprovincia3 = form.cleaned_data['avalistaiviendaalquiladaprovincia3']
            avalistaiviendaalquiladacodigopostal3 = form.cleaned_data['avalistaiviendaalquiladacodigopostal3']
            avalistaiviendaalquiladacobraalquiler3 = form.cleaned_data['avalistaiviendaalquiladacobraalquiler3']
            avalistalquilerpaga1 = form.cleaned_data['avalistalquilerpaga1']
            avalistalquilermetros1 = form.cleaned_data['avalistalquilermetros1']
            avalistalquilerdireccion1 = form.cleaned_data['avalistalquilerdireccion1']
            avalistalquilerpoblacion1 = form.cleaned_data['avalistalquilerpoblacion1']
            avalistalquilerprovincia1 = form.cleaned_data['avalistalquilerprovincia1']
            avalistalquilercodigopostal1 = form.cleaned_data['avalistalquilercodigopostal1']
            avalistalquilerpaga2 = form.cleaned_data['avalistalquilerpaga2']
            avalistalquilermetros2 = form.cleaned_data['avalistalquilermetros2']
            avalistalquilerdireccion2 = form.cleaned_data['avalistalquilerdireccion2']
            avalistalquilerpoblacion2 = form.cleaned_data['avalistalquilerpoblacion2']
            avalistalquilerprovincia2 = form.cleaned_data['avalistalquilerprovincia2']
            avalistalquilercodigopostal2 = form.cleaned_data['avalistalquilercodigopostal2']
            avalistalquilerpaga3 = form.cleaned_data['avalistalquilerpaga3']
            avalistalquilermetros3 = form.cleaned_data['avalistalquilermetros3']
            avalistalquilerdireccion3 = form.cleaned_data['avalistalquilerdireccion3']
            avalistalquilerpoblacion3 = form.cleaned_data['avalistalquilerpoblacion3']
            avalistalquilerprovincia3 = form.cleaned_data['avalistalquilerprovincia3']
            avalistalquilercodigopostal3 = form.cleaned_data['avalistalquilercodigopostal3']
            avalistaireccionpersonal = form.cleaned_data['avalistaireccionpersonal']
            avalistaoblacionpersonal = form.cleaned_data['avalistaoblacionpersonal']
            avalistarovinciapersonal = form.cleaned_data['avalistarovinciapersonal']
            avalistaodigopostalpersonal = form.cleaned_data['avalistaodigopostalpersonal']
            avalistareditotipo1 = form.cleaned_data['avalistareditotipo1']
            avalistareditotantoporciento1 = form.cleaned_data['avalistareditotantoporciento1']
            avalistareditoimporte1 = form.cleaned_data['avalistareditoimporte1']
            avalistareditocuota1 = form.cleaned_data['avalistareditocuota1']
            avalistareditoentidad1 = form.cleaned_data['avalistareditoentidad1']
            avalistareditotipo2 = form.cleaned_data['avalistareditotipo2']
            avalistareditotantoporciento2 = form.cleaned_data['avalistareditotantoporciento2']
            avalistareditoimporte2 = form.cleaned_data['avalistareditoimporte2']
            avalistareditocuota2 = form.cleaned_data['avalistareditocuota2']
            avalistareditoentidad2 = form.cleaned_data['avalistareditoentidad2']
            avalistareditotipo3 = form.cleaned_data['avalistareditotipo3']
            avalistareditotantoporciento3 = form.cleaned_data['avalistareditotantoporciento3']
            avalistareditoimporte3 = form.cleaned_data['avalistareditoimporte3']
            avalistareditocuota3 = form.cleaned_data['avalistareditocuota3']
            avalistareditoentidad3 = form.cleaned_data['avalistareditoentidad3']
            avalistaarjetacuota1 = form.cleaned_data['avalistaarjetacuota1']
            avalistaarjetaimporte1 = form.cleaned_data['avalistaarjetaimporte1']
            avalistaarjetaentidad1 = form.cleaned_data['avalistaarjetaentidad1']
            avalistaarjetacuota2 = form.cleaned_data['avalistaarjetacuota2']
            avalistaarjetaimporte2 = form.cleaned_data['avalistaarjetaimporte2']
            avalistaarjetaentidad2 = form.cleaned_data['avalistaarjetaentidad2']
            avalistaarjetacuota3 = form.cleaned_data['avalistaarjetacuota3']
            avalistaarjetaimporte3 = form.cleaned_data['avalistaarjetaimporte3']
            avalistaarjetaentidad3 = form.cleaned_data['avalistaarjetaentidad3']
            avalistaecivosimporte1 = form.cleaned_data['avalistaecivosimporte1']
            avalistaecivosimporte2 = form.cleaned_data['avalistaecivosimporte2']
            avalistaecivosimporte3 = form.cleaned_data['avalistaecivosimporte3']
            avalistaorosoimporte1 = form.cleaned_data['avalistaorosoimporte1']
            avalistaorosoquien1 = form.cleaned_data['avalistaorosoquien1']
            avalistaorosoimporte2 = form.cleaned_data['avalistaorosoimporte2']
            avalistaorosoquien2 = form.cleaned_data['avalistaorosoquien2']
            avalistaorosoimporte3 = form.cleaned_data['avalistaorosoimporte3']
            avalistaorosoquien3 = form.cleaned_data['avalistaorosoquien3']

            expedient = models.expediente.objects.create(numexp=numexp, tipo="Coche", fecha_hora=datayhora)
            persona = models.persona.objects.create(numexp=numexp, nombre=name, dni=dni, direccion=direccion,
                                                    email=email, telefono=telefono, movil=movil,
                                                    fechanacimiento=fechanacimiento,
                                                    nacionalidad=nacionalidad, estadocivil=estadocivil,
                                                    tipocasado=tipocasado, numerodehijos=numerohijos,
                                                    sihijosmayores18=mayoresdeedad, sihijoscuantoscargo=cuantosacargo,
                                                    sihijosingreso=ingresohijos, justificante=justificante,
                                                    autoriza=autorizacion, medio=medio, metodopago=metodopago)
            personaanexos = models.personaanexos.objects.create(numexp=numexp, seguridadsocial=cotizacion,
                                                                siajenatipo=tipotrabajo,
                                                                siajenatemporal=finalizacontrato,
                                                                otrosingresos=otrosingresos,
                                                                otrosingresostexto=otrosingresostexto,
                                                                otrosgastos=otrosgastos,
                                                                otrosgastostexto=otrosgastostexto)
            paro = models.paro.objectos.create(numexp=numexp, desdecuando=parodesdecuando, cobra=parocuantocobra)
            juvilacion = models.juvilacion.objetos.create(numexp, importe=importejuvilacion,
                                                          pagas=numerodepagasjuvilacion, fechainicio=iniciojuvilacion,
                                                          fechafin=finjuvilacion)
            anotaciones = models.anotaciones.objects.create(numexp=numexp, personales=anotacionespersonales,
                                                            empresa=anotacionesingresos, vivienda=anotacionesviviendas,
                                                            financieros=anotacionesfinancieras,
                                                            destinado=anotacionesdestinado,
                                                            avalista=anotacionesavalista)

            if viviendadireccion1:
                vivienda = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion1,
                                                          poblacion=viviendapoblacion1, provincia=viviendaprovincia1,
                                                          codigopostal=viviendacodigopostal1,
                                                          valorvivienda=viviendavalor1,
                                                          valorhipoteca=viviendavalorhipoteca1,
                                                          estapagada=viviendaestapagada1, sinopagadaanos=viviendaanos1,
                                                          sinopagadaentidad=viviendaentidad1,
                                                          sinopagadapagahipoteca=viviendacuotamensual1,
                                                          librecargos=viviendalibredecargos1, metros=viviendametros1,
                                                          porciento=viviendaporciento1)

            if viviendadireccion2:
                vivienda2 = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion2,
                                                           poblacion=viviendapoblacion2, provincia=viviendaprovincia2,
                                                           codigopostal=viviendacodigopostal2,
                                                           valorvivienda=viviendavalor2,
                                                           valorhipoteca=viviendavalorhipoteca2,
                                                           estapagada=viviendaestapagada2, sinopagadaanos=viviendaanos2,
                                                           sinopagadaentidad=viviendaentidad2,
                                                           sinopagadapagahipoteca=viviendacuotamensual2,
                                                           librecargos=viviendalibredecargos2, metros=viviendametros2,
                                                           porciento=viviendaporciento2)

            if viviendadireccion3:
                vivienda3 = models.vivienda.objects.create(numexp=numexp, direccion=viviendadireccion3,
                                                           poblacion=viviendapoblacion3, provincia=viviendaprovincia3,
                                                           codigopostal=viviendacodigopostal3,
                                                           valorvivienda=viviendavalor3,
                                                           valorhipoteca=viviendavalorhipoteca3,
                                                           estapagada=viviendaestapagada3, sinopagadaanos=viviendaanos3,
                                                           sinopagadaentidad=viviendaentidad3,
                                                           sinopagadapagahipoteca=viviendacuotamensual3,
                                                           librecargos=viviendalibredecargos3, metros=viviendametros3,
                                                           porciento=viviendaporciento3)

            if viviendaalquiladadireccion1:
                viviendaalquilada = models.vivienda.objects.create(numexp=numexp, direccion=viviendaalquiladadireccion1,
                                                                   poblacion=viviendaalquiladapoblacion1,
                                                                   provincia=viviendaalquiladaprovincia1,
                                                                   codigopostal=viviendaalquiladacodigopostal1,
                                                                   valorvivienda=viviendaalquiladavalor1,
                                                                   valorhipoteca=viviendaalquiladavalorhipoteca1,
                                                                   estapagada=viviendaalquiladaestapagada1,
                                                                   sinopagadaanos=viviendaalquiladaanos1,
                                                                   sinopagadaentidad=viviendaalquiladaentidad1,
                                                                   librecargos=viviendaalquiladalibredecargos1,
                                                                   metros=viviendaalquiladametros1,
                                                                   porciento=viviendaalquiladaporciento1,
                                                                   valoralquilada=viviendaalquiladacobraalquiler1,
                                                                   sinopagadapagahipoteca=viviendaalquiladacuotamensual1)

            if viviendaalquiladadireccion2:
                viviendaalquilada2 = models.vivienda.objects.create(numexp=numexp,
                                                                    direccion=viviendaalquiladadireccion2,
                                                                    poblacion=viviendaalquiladapoblacion2,
                                                                    provincia=viviendaalquiladaprovincia2,
                                                                    codigopostal=viviendaalquiladacodigopostal2,
                                                                    valorvivienda=viviendaalquiladavalor2,
                                                                    valorhipoteca=viviendaalquiladavalorhipoteca2,
                                                                    estapagada=viviendaalquiladaestapagada2,
                                                                    sinopagadaanos=viviendaalquiladaanos2,
                                                                    sinopagadaentidad=viviendaalquiladaentidad2,
                                                                    librecargos=viviendaalquiladalibredecargos2,
                                                                    metros=viviendaalquiladametros2,
                                                                    porciento=viviendaalquiladaporciento2,
                                                                    valoralquilada=viviendaalquiladacobraalquiler2,
                                                                    sinopagadapagahipoteca=viviendaalquiladacuotamensual2)

            if viviendaalquiladadireccion3:
                viviendaalquilada3 = models.vivienda.objects.create(numexp=numexp,
                                                                    direccion=viviendaalquiladadireccion3,
                                                                    poblacion=viviendaalquiladapoblacion3,
                                                                    provincia=viviendaalquiladaprovincia3,
                                                                    codigopostal=viviendaalquiladacodigopostal3,
                                                                    valorvivienda=viviendaalquiladavalor3,
                                                                    valorhipoteca=viviendaalquiladavalorhipoteca3,
                                                                    estapagada=viviendaalquiladaestapagada3,
                                                                    sinopagadaanos=viviendaalquiladaanos3,
                                                                    sinopagadaentidad=viviendaalquiladaentidad3,
                                                                    librecargos=viviendaalquiladalibredecargos3,
                                                                    metros=viviendaalquiladametros3,
                                                                    porciento=viviendaalquiladaporciento3,
                                                                    valoralquilada=viviendaalquiladacobraalquiler3,
                                                                    sinopagadapagahipoteca=viviendaalquiladacuotamensual3)

            if alquilerdireccion1:
                alquiler = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion1,
                                                          poblacion=alquilerpoblacion1, provincia=alquilerprovincia1,
                                                          codigopostal=alquilercodigopostal1, metros=alquilermetros1,
                                                          pagaalquiler=alquilerpaga1)

            if alquilerdireccion2:
                alquiler2 = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion2,
                                                           poblacion=alquilerpoblacion2, provincia=alquilerprovincia2,
                                                           codigopostal=alquilercodigopostal2, metros=alquilermetros2,
                                                           pagaalquiler=alquilerpaga2)

            if alquilerdireccion3:
                alquiler3 = models.vivienda.objects.create(numexp=numexp, direccion=alquilerdireccion3,
                                                           poblacion=alquilerpoblacion3, provincia=alquilerprovincia3,
                                                           codigopostal=alquilercodigopostal3, metros=alquilermetros3,
                                                           pagaalquiler=alquilerpaga3)

            if direccionpersonal:
                vivienda = models.vivienda.objects.create(numexp=numexp, direccion=direccionpersonal,
                                                          poblacion=poblacionpersonal, provincia=provinciapersonal,
                                                          codigopostal=codigopostalpersonal)

            if nombreempresa1:
                empresa = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa1, cargo=cargoempresa1,
                                                        actividad=actividadempresa1, ingresos=ingresosempresa1,
                                                        pagas=pagasempresa1, otrosingresos=otrosingresosempresa1,
                                                        antiguedad=antiguedadempresa1)

            if nombreempresa2:
                empresa2 = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa2, cargo=cargoempresa2,
                                                         actividad=actividadempresa2, ingresos=ingresosempresa2,
                                                         pagas=pagasempresa2, otrosingresos=otrosingresosempresa2,
                                                         antiguedad=antiguedadempresa2)

            if nombreempresa3:
                empresa3 = models.empresa.objects.create(numexp=numexp, nombre=nombreempresa3, cargo=cargoempresa3,
                                                         actividad=actividadempresa3, ingresos=ingresosempresa3,
                                                         pagas=pagasempresa3, otrosingresos=otrosingresosempresa3,
                                                         antiguedad=antiguedadempresa3)

            if creditotipo1:
                debecredito1 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo1,
                                                                 porcientoavalista=creditotantoporciento1,
                                                                 importe=creditoimporte1, cuota=creditocuota1,
                                                                 entidad=creditoentidad1)
            if creditotipo2:
                debecredito2 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo2,
                                                                 porcientoavalista=creditotantoporciento2,
                                                                 importe=creditoimporte2, cuota=creditocuota2,
                                                                 entidad=creditoentidad2)
            if creditotipo3:
                debecredito3 = models.debecredito.objetos.create(numexp=numexp, tipo=creditotipo3,
                                                                 porcientoavalista=creditotantoporciento3,
                                                                 importe=creditoimporte3, cuota=creditocuota3,
                                                                 entidad=creditoentidad3)
            if tarjetacuota1:
                debetarjeta1 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota1,
                                                                 importe=tarjetaimporte1,
                                                                 entidad=tarjetaentidad1)
            if tarjetacuota2:
                debetarjeta2 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota2,
                                                                 importe=tarjetaimporte2,
                                                                 entidad=tarjetaentidad2)
            if tarjetacuota3:
                debetarjeta3 = models.debetarjeta.objetos.create(numexp=numexp, cuota=tarjetacuota3,
                                                                 importe=tarjetaimporte3,
                                                                 entidad=tarjetaentidad3)
            if recivosimporte1:
                deberecivo1s = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte1)
            if recivosimporte2:
                deberecivos2 = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte2)
            if recivosimporte3:
                deberecivos3 = models.deberecivos.objetos.create(numexp=numexp, importe=recivosimporte3)
            if morosoimporte1:
                debemoroso1 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte1,
                                                               quien=morosoquien1)
            if morosoimporte2:
                debemoroso2 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte2,
                                                               quien=morosoquien2)
            if morosoimporte3:
                debemoroso3 = models.debemoroso.objects.create(numexp=numexp, importe=morosoimporte3,
                                                               quien=morosoquien3)

            avalpersona = models.persona.objects.create(numexp=numexp, nombre=avalistaame, avalista=True,
                                                        dni=avalistani,
                                                        direccion=avalistaireccion, email=avalistamail,
                                                        telefono=avalistaelefono, movil=avalistaovil,
                                                        fechanacimiento=avalistaechanacimiento,
                                                        nacionalidad=avalistaacionalidad,
                                                        estadocivil=avalistastadocivil,
                                                        tipocasado=avalistaipocasado, numerodehijos=avalistaumerohijos,
                                                        sihijosmayores18=avalistaayoresdeedad,
                                                        sihijoscuantoscargo=avalistauantosacargo,
                                                        sihijosingreso=avalistangresohijos)
            avalpersonaanexos = models.personaanexos.objects.create(numexp=numexp, avalista=True,
                                                                    seguridadsocial=avalistaotizacion,
                                                                    siajenatipo=avalistaipotrabajo,
                                                                    siajenatemporal=avalistainalizacontrato,
                                                                    otrosingresos=avalistatrosingresos,
                                                                    otrosingresostexto=avalistatrosingresostexto,
                                                                    otrosgastos=avalistatrosgastos,
                                                                    otrosgastostexto=avalistatrosgastostexto)
            avalparo = models.paro.objectos.create(numexp=numexp, avalista=True, desdecuando=avalistaarodesdecuando,
                                                   cobra=avalistaarocuantocobra)
            avaljuvilacion = models.juvilacion.objetos.create(numexp, avalista=True, importe=avalistamportejuvilacion,
                                                              pagas=avalistaumerodepagasjuvilacion,
                                                              fechainicio=avalistaniciojuvilacion,
                                                              fechafin=avalistainjuvilacion)

            if avalistaiviendadireccion1:
                avalvivienda = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                              direccion=avalistaiviendadireccion1,
                                                              poblacion=avalistaiviendapoblacion1,
                                                              provincia=avalistaiviendaprovincia1,
                                                              codigopostal=avalistaiviendacodigopostal1,
                                                              valorvivienda=avalistaiviendavalor1,
                                                              valorhipoteca=avalistaiviendavalorhipoteca1,
                                                              estapagada=avalistaiviendaestapagada1,
                                                              sinopagadaanos=avalistaiviendaanos1,
                                                              sinopagadaentidad=avalistaiviendaentidad1,
                                                              sinopagadapagahipoteca=avalistaiviendacuotamensual1,
                                                              librecargos=avalistaiviendalibredecargos1,
                                                              metros=avalistaiviendametros1,
                                                              porciento=avalistaiviendaporciento1)

            if avalistaiviendadireccion2:
                avalvivienda2 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                               direccion=avalistaiviendadireccion2,
                                                               poblacion=avalistaiviendapoblacion2,
                                                               provincia=avalistaiviendaprovincia2,
                                                               codigopostal=avalistaiviendacodigopostal2,
                                                               valorvivienda=avalistaiviendavalor2,
                                                               valorhipoteca=avalistaiviendavalorhipoteca2,
                                                               estapagada=avalistaiviendaestapagada2,
                                                               sinopagadaanos=avalistaiviendaanos2,
                                                               sinopagadaentidad=avalistaiviendaentidad2,
                                                               sinopagadapagahipoteca=avalistaiviendacuotamensual2,
                                                               librecargos=avalistaiviendalibredecargos2,
                                                               metros=avalistaiviendametros2,
                                                               porciento=avalistaiviendaporciento2)

            if avalistaiviendadireccion3:
                avalvivienda3 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                               direccion=avalistaiviendadireccion3,
                                                               poblacion=avalistaiviendapoblacion3,
                                                               provincia=avalistaiviendaprovincia3,
                                                               codigopostal=avalistaiviendacodigopostal3,
                                                               valorvivienda=avalistaiviendavalor3,
                                                               valorhipoteca=avalistaiviendavalorhipoteca3,
                                                               estapagada=avalistaiviendaestapagada3,
                                                               sinopagadaanos=avalistaiviendaanos3,
                                                               sinopagadaentidad=avalistaiviendaentidad3,
                                                               sinopagadapagahipoteca=avalistaiviendacuotamensual3,
                                                               librecargos=avalistaiviendalibredecargos3,
                                                               metros=avalistaiviendametros3,
                                                               porciento=avalistaiviendaporciento3)

            if avalistaiviendaalquiladadireccion1:
                avalviviendaalquilada = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                                       direccion=avalistaiviendaalquiladadireccion1,
                                                                       poblacion=avalistaiviendaalquiladapoblacion1,
                                                                       provincia=avalistaiviendaalquiladaprovincia1,
                                                                       codigopostal=avalistaiviendaalquiladacodigopostal1,
                                                                       valorvivienda=avalistaiviendaalquiladavalor1,
                                                                       valorhipoteca=avalistaiviendaalquiladavalorhipoteca1,
                                                                       estapagada=avalistaiviendaalquiladaestapagada1,
                                                                       sinopagadaanos=avalistaiviendaalquiladaanos1,
                                                                       sinopagadaentidad=avalistaiviendaalquiladaentidad1,
                                                                       librecargos=avalistaiviendaalquiladalibredecargos1,
                                                                       metros=avalistaiviendaalquiladametros1,
                                                                       porciento=avalistaiviendaalquiladaporciento1,
                                                                       valoralquilada=avalistaiviendaalquiladacobraalquiler1,
                                                                       sinopagadapagahipoteca=avalistaiviendaalquiladacuotamensual1)

            if avalistaiviendaalquiladadireccion2:
                avalviviendaalquilada2 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                                        direccion=avalistaiviendaalquiladadireccion2,
                                                                        poblacion=avalistaiviendaalquiladapoblacion2,
                                                                        provincia=avalistaiviendaalquiladaprovincia2,
                                                                        codigopostal=avalistaiviendaalquiladacodigopostal2,
                                                                        valorvivienda=avalistaiviendaalquiladavalor2,
                                                                        valorhipoteca=avalistaiviendaalquiladavalorhipoteca2,
                                                                        estapagada=avalistaiviendaalquiladaestapagada2,
                                                                        sinopagadaanos=avalistaiviendaalquiladaanos2,
                                                                        sinopagadaentidad=avalistaiviendaalquiladaentidad2,
                                                                        librecargos=avalistaiviendaalquiladalibredecargos2,
                                                                        metros=avalistaiviendaalquiladametros2,
                                                                        porciento=avalistaiviendaalquiladaporciento2,
                                                                        valoralquilada=avalistaiviendaalquiladacobraalquiler2,
                                                                        sinopagadapagahipoteca=avalistaiviendaalquiladacuotamensual2)

            if avalistaiviendaalquiladadireccion3:
                avalviviendaalquilada3 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                                        direccion=avalistaiviendaalquiladadireccion3,
                                                                        poblacion=avalistaiviendaalquiladapoblacion3,
                                                                        provincia=avalistaiviendaalquiladaprovincia3,
                                                                        codigopostal=avalistaiviendaalquiladacodigopostal3,
                                                                        valorvivienda=avalistaiviendaalquiladavalor3,
                                                                        valorhipoteca=avalistaiviendaalquiladavalorhipoteca3,
                                                                        estapagada=avalistaiviendaalquiladaestapagada3,
                                                                        sinopagadaanos=avalistaiviendaalquiladaanos3,
                                                                        sinopagadaentidad=avalistaiviendaalquiladaentidad3,
                                                                        librecargos=avalistaiviendaalquiladalibredecargos3,
                                                                        metros=avalistaiviendaalquiladametros3,
                                                                        porciento=avalistaiviendaalquiladaporciento3,
                                                                        valoralquilada=avalistaiviendaalquiladacobraalquiler3,
                                                                        sinopagadapagahipoteca=avalistaiviendaalquiladacuotamensual3)

            if avalistalquilerdireccion1:
                avalalquiler = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                              direccion=avalistalquilerdireccion1,
                                                              poblacion=avalistalquilerpoblacion1,
                                                              provincia=avalistalquilerprovincia1,
                                                              codigopostal=avalistalquilercodigopostal1,
                                                              metros=avalistalquilermetros1,
                                                              pagaalquiler=avalistalquilerpaga1)

            if avalistalquilerdireccion2:
                avalalquiler2 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                               direccion=avalistalquilerdireccion2,
                                                               poblacion=avalistalquilerpoblacion2,
                                                               provincia=avalistalquilerprovincia2,
                                                               codigopostal=avalistalquilercodigopostal2,
                                                               metros=avalistalquilermetros2,
                                                               pagaalquiler=avalistalquilerpaga2)

            if avalistalquilerdireccion3:
                avalalquiler3 = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                               direccion=avalistalquilerdireccion3,
                                                               poblacion=avalistalquilerpoblacion3,
                                                               provincia=avalistalquilerprovincia3,
                                                               codigopostal=avalistalquilercodigopostal3,
                                                               metros=avalistalquilermetros3,
                                                               pagaalquiler=avalistalquilerpaga3)

            if avalistaireccionpersonal:
                avalvivienda = models.vivienda.objects.create(numexp=numexp, avalista=True,
                                                              direccion=avalistaireccionpersonal,
                                                              poblacion=avalistaoblacionpersonal,
                                                              provincia=avalistarovinciapersonal,
                                                              codigopostal=avalistaodigopostalpersonal)

            if avalistaombreempresa1:
                avalempresa = models.empresa.objects.create(numexp=numexp, avalista=True,
                                                            nombre=avalistaombreempresa1, cargo=avalistaargoempresa1,
                                                            actividad=avalistactividadempresa1,
                                                            ingresos=avalistangresosempresa1,
                                                            pagas=avalistaagasempresa1,
                                                            otrosingresos=avalistatrosingresosempresa1,
                                                            antiguedad=avalistantiguedadempresa1)

            if avalistaombreempresa2:
                avalempresa2 = models.empresa.objects.create(numexp=numexp, avalista=True,
                                                             nombre=avalistaombreempresa2, cargo=avalistaargoempresa2,
                                                             actividad=avalistactividadempresa2,
                                                             ingresos=avalistangresosempresa2,
                                                             pagas=avalistaagasempresa2,
                                                             otrosingresos=avalistatrosingresosempresa2,
                                                             antiguedad=avalistantiguedadempresa2)

            if avalistaombreempresa3:
                avalempresa3 = models.empresa.objects.create(numexp=numexp, avalista=True,
                                                             nombre=avalistaombreempresa3, cargo=avalistaargoempresa3,
                                                             actividad=avalistactividadempresa3,
                                                             ingresos=avalistangresosempresa3,
                                                             pagas=avalistaagasempresa3,
                                                             otrosingresos=avalistatrosingresosempresa3,
                                                             antiguedad=avalistantiguedadempresa3)

            if avalistareditotipo1:
                avaldebecredito1 = models.debecredito.objetos.create(numexp=numexp, avalista=True,
                                                                     tipo=avalistareditotipo1,
                                                                     porcientoavalista=avalistareditotantoporciento1,
                                                                     importe=avalistareditoimporte1,
                                                                     cuota=avalistareditocuota1,
                                                                     entidad=avalistareditoentidad1)
            if avalistareditotipo2:
                avaldebecredito2 = models.debecredito.objetos.create(numexp=numexp, avalista=True,
                                                                     tipo=avalistareditotipo2,
                                                                     porcientoavalista=avalistareditotantoporciento2,
                                                                     importe=avalistareditoimporte2,
                                                                     cuota=avalistareditocuota2,
                                                                     entidad=avalistareditoentidad2)
            if avalistareditotipo3:
                avaldebecredito3 = models.debecredito.objetos.create(numexp=numexp, avalista=True,
                                                                     tipo=avalistareditotipo3,
                                                                     porcientoavalista=avalistareditotantoporciento3,
                                                                     importe=avalistareditoimporte3,
                                                                     cuota=avalistareditocuota3,
                                                                     entidad=avalistareditoentidad3)
            if avalistaarjetacuota1:
                avaldebetarjeta1 = models.debetarjeta.objetos.create(numexp=numexp, avalista=True,
                                                                     cuota=avalistaarjetacuota1,
                                                                     importe=avalistaarjetaimporte1,
                                                                     entidad=avalistaarjetaentidad1)
            if avalistaarjetacuota2:
                avaldebetarjeta2 = models.debetarjeta.objetos.create(numexp=numexp, avalista=True,
                                                                     cuota=avalistaarjetacuota2,
                                                                     importe=avalistaarjetaimporte2,
                                                                     entidad=avalistaarjetaentidad2)
            if avalistaarjetacuota3:
                avaldebetarjeta3 = models.debetarjeta.objetos.create(numexp=numexp, avalista=True,
                                                                     cuota=avalistaarjetacuota3,
                                                                     importe=avalistaarjetaimporte3,
                                                                     entidad=avalistaarjetaentidad3)
            if avalistaecivosimporte1:
                avaldeberecivo1s = models.deberecivos.objetos.create(numexp=numexp, avalista=True,
                                                                     importe=avalistaecivosimporte1)
            if avalistaecivosimporte2:
                avaldeberecivos2 = models.deberecivos.objetos.create(numexp=numexp, avalista=True,
                                                                     importe=avalistaecivosimporte2)
            if avalistaecivosimporte3:
                avaldeberecivos3 = models.deberecivos.objetos.create(numexp=numexp, avalista=True,
                                                                     importe=avalistaecivosimporte3)
            if avalistaorosoimporte1:
                avaldebemoroso1 = models.debemoroso.objects.create(numexp=numexp, avalista=True,
                                                                   importe=avalistaorosoimporte1,
                                                                   quien=avalistaorosoquien1)
            if avalistaorosoimporte2:
                avaldebemoroso2 = models.debemoroso.objects.create(numexp=numexp, avalista=True,
                                                                   importe=avalistaorosoimporte2,
                                                                   quien=avalistaorosoquien2)
            if avalistaorosoimporte3:
                avaldebemoroso3 = models.debemoroso.objects.create(numexp=numexp, avalista=True,
                                                                   importe=avalistaorosoimporte3,
                                                                   quien=avalistaorosoquien3)

            return HttpResponseRedirect('/hipotecario/')
        else:
            print form.errors
    else:
        form = forms.formHipotecario()
        lastNum = models.expediente.objects.all().order_by("numexp").last()
        if not lastNum:
            lastNum = 40000
        else:
            lastNum += 1
        form.fields["numexp"].initial = lastNum
        form.fields["datayhora"].initial = datetime.now()
        context.update({"form": form})
        return render(request, 'form_hipotec.html', context)
