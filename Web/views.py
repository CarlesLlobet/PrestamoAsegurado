import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context

from Web import forms
from Web import models


def index(request):
    return render(request, 'index.html')


def asnef(request):
    return render(request, 'asnef.html')


def coche(request):
    context = Context({})

    if request.method == 'POST':
        form = forms.formCoche(request.POST)
        if form.is_valid():
            #TODO: Ficar quin camp s'ha d'agafar dins de cada camp, exemple a name
            name = form.cleaned_data['name']
            dni = form.cleaned_data['']
            direccion = form.cleaned_data['']
            email = form.cleaned_data['']
            telefono = form.cleaned_data['']
            movil = form.cleaned_data['']
            fechanacimiento = form.cleaned_data['']
            nacionalidad = form.cleaned_data['']
            estadocivil = form.cleaned_data['']
            tipocasado = form.cleaned_data['']
            numerohijos = form.cleaned_data['']
            mayoresdeedad = form.cleaned_data['']
            cuantosacargo = form.cleaned_data['']
            ingresohijos = form.cleaned_data['']
            anotacionespersonales = form.cleaned_data['']
            cotizacion = form.cleaned_data['']
            tipotrabajo = form.cleaned_data['']
            finalizacontrato = form.cleaned_data['']
            nombreempresa1 = form.cleaned_data['']
            cargoempresa1 = form.cleaned_data['']
            actividadempresa1 = form.cleaned_data['']
            ingresosempresa1 = form.cleaned_data['']
            pagasempresa1 = form.cleaned_data['']
            otrosingresosempresa1 = form.cleaned_data['']
            antiguedadempresa1 = form.cleaned_data['']
            importejuvilacion = form.cleaned_data['']
            numerodepagasjuvilacion = form.cleaned_data['']
            iniciojuvilacion = form.cleaned_data['']
            finjuvilacion = form.cleaned_data['']
            parodesdecuando = form.cleaned_data['']
            parocuantocobra = form.cleaned_data['']
            otrosingresos = form.cleaned_data['']
            otrosgastos = form.cleaned_data['']
            otrosingresostexto = form.cleaned_data['']
            otrosgastostexto = form.cleaned_data['']
            anotacionesingresos = form.cleaned_data['']
            viviendavalor1 = form.cleaned_data['']
            viviendavalorhipoteca1 = form.cleaned_data['']
            viviendaestapagada1 = form.cleaned_data['']
            viviendalibredecargos1 = form.cleaned_data['']
            viviendacuotamensual1 = form.cleaned_data['']
            viviendaanos1 = form.cleaned_data['']
            viviendaentidad1 = form.cleaned_data['']
            viviendametros1 = form.cleaned_data['']
            viviendaporciento1 = form.cleaned_data['']
            viviendadireccion1 = form.cleaned_data['']
            viviendapoblacion1 = form.cleaned_data['']
            viviendaprovincia1 = form.cleaned_data['']
            viviendacodigopostal1 = form.cleaned_data['']
            viviendaalquiladavalor1 = form.cleaned_data['']
            viviendaalquiladavalorhipoteca1 = form.cleaned_data['']
            viviendaalquiladaestapagada1 = form.cleaned_data['']
            viviendaalquiladalibredecargos1 = form.cleaned_data['']
            viviendaalquiladacuotamensual1 = form.cleaned_data['']
            viviendaalquiladaanos1 = form.cleaned_data['']
            viviendaalquiladaentidad1 = form.cleaned_data['']
            viviendaalquiladametros1 = form.cleaned_data['']
            viviendaalquiladaporciento1 = form.cleaned_data['']
            viviendaalquiladadireccion1 = form.cleaned_data['']
            viviendaalquiladapoblacion1 = form.cleaned_data['']
            viviendaalquiladaprovincia1 = form.cleaned_data['']
            viviendaalquiladacodigopostal1 = form.cleaned_data['']
            viviendaalquiladacobraalquiler = form.cleaned_data['']
            alquilerpaga1 = form.cleaned_data['']
            alquilermetros1 = form.cleaned_data['']
            alquilerdireccion1 = form.cleaned_data['']
            alquilerpoblacion1 = form.cleaned_data['']
            alquilerprovincia1 = form.cleaned_data['']
            alquilercodigopostal1 = form.cleaned_data['']
            anotacionesviviendas = form.cleaned_data['']
            direccion = form.cleaned_data['']
            poblacion = form.cleaned_data['']
            provincia = form.cleaned_data['']
            codigopostal = form.cleaned_data['']
            creditotipo1 = form.cleaned_data['']
            creditotantoporciento1 = form.cleaned_data['']
            creditoimporte1 = form.cleaned_data['']
            creditocuota1 = form.cleaned_data['']
            creditoentidad1 = form.cleaned_data['']
            tarjetacuota1 = form.cleaned_data['']
            tarjetaimporte1 = form.cleaned_data['']
            tarjetaentidad1 = form.cleaned_data['']
            recivosimporte1 = form.cleaned_data['']
            morosoimporte1 = form.cleaned_data['']
            morosoquien1 = form.cleaned_data['']
            anotacionesfinancieras = form.cleaned_data['']
            motor = form.cleaned_data['']
            marca = form.cleaned_data['']
            modelo = form.cleaned_data['']
            antiguedad = form.cleaned_data['']
            matricula = form.cleaned_data['']
            estadovehiculo = form.cleaned_data['']
            anotacionescoche = form.cleaned_data['']
            recibirdinero = form.cleaned_data['']
            anotacionesdestinado = form.cleaned_data['']
            justificante = form.cleaned_data['']
            autorizacion = form.cleaned_data['']
            medio = form.cleaned_data['']
            anotacionesdestinado = form.cleaned_data['']
            numexp = form.cleaned_data['numexp']

            #TODO: Ara que tenim tota la info, s'han de crear les instancies que toquin a la bd. Exemple a sota

            expedient = models.expediente.objects.create(numexp=numexp, tipo="coche", fecha_hora=datetime.now())
            return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = forms.formCoche()
        context.update({"form": form})
        lastNum = models.expediente.objects.all().order_by("numexp").reverse[0].values("numexp")
        fecha = datetime.now()
        if not lastNum:
            lastNum = 40000
        else:
            lastNum = 1
        form.fields["numexp"].initial = lastNum
        context.update({"data": fecha.year+"-"+fecha.month+"-"+fecha.day})
        context.update({"hora": fecha.hour+":"+fecha.minute+":"+fecha.second})
        return render(request, 'coche.html', context)


def hipotecario(request):
    context = Context({})
    return render(request, 'hipotecario.html', context)


def microcredito(request):
    context = Context({})
    return render(request, 'microcredito.html', context)


def personal(request):
    context = Context({})
    return render(request, 'personal.html', context)
