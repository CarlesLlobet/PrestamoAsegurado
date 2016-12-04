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
            viviendaalquiladacobraalquiler = form.cleaned_data['viviendaalquiladacobraalquiler']
            alquilerpaga1 = form.cleaned_data['alquilerpaga1']
            alquilermetros1 = form.cleaned_data['alquilermetros1']
            alquilerdireccion1 = form.cleaned_data['alquilerdireccion1']
            alquilerpoblacion1 = form.cleaned_data['alquilerpoblacion1']
            alquilerprovincia1 = form.cleaned_data['alquilerprovincia1']
            alquilercodigopostal1 = form.cleaned_data['alquilercodigopostal1']
            anotacionesviviendas = form.cleaned_data['anotacionesviviendas']
            direccion = form.cleaned_data['direccion']
            poblacion = form.cleaned_data['poblacion']
            provincia = form.cleaned_data['provincia']
            codigopostal = form.cleaned_data['codigopostal']
            creditotipo1 = form.cleaned_data['creditotipo1']
            creditotantoporciento1 = form.cleaned_data['creditotantoporciento1']
            creditoimporte1 = form.cleaned_data['creditoimporte1']
            creditocuota1 = form.cleaned_data['creditocuota1']
            creditoentidad1 = form.cleaned_data['creditoentidad1']
            tarjetacuota1 = form.cleaned_data['tarjetacuota1']
            tarjetaimporte1 = form.cleaned_data['tarjetaimporte1']
            tarjetaentidad1 = form.cleaned_data['tarjetaentidad1']
            recivosimporte1 = form.cleaned_data['recivosimporte1']
            morosoimporte1 = form.cleaned_data['morosoimporte1']
            morosoquien1 = form.cleaned_data['morosoquien1']
            anotacionesfinancieras = form.cleaned_data['anotacionesfinancieras']
            motor = form.cleaned_data['motor']
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            antiguedad = form.cleaned_data['antiguedad']
            matricula = form.cleaned_data['matricula']
            estadovehiculo = form.cleaned_data['estadovehiculo']
            anotacionescoche = form.cleaned_data['anotacionescoche']
            recibirdinero = form.cleaned_data['recibirdinero']
            anotacionesdestinado = form.cleaned_data['anotacionesdestinado']
            justificante = form.cleaned_data['justificante']
            autorizacion = form.cleaned_data['autorizacion']
            medio = form.cleaned_data['medio']
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
