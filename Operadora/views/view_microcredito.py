from .views import *


def group_check(user):
    return user.groups.filter(name__in=['Operadoras'])


@login_required(login_url="/")
@user_passes_test(group_check)
def microcredito(request, numexp):
    context = {}
    if request.method == 'POST':
        form = forms.formMicrocredito(request.POST)
        if form.is_valid():
            importeselect1 = form.cleaned_data["importeselect1"]
            importeselect2 = form.cleaned_data["importeselect2"]
            importeselect3 = form.cleaned_data["importeselect3"]
            name = form.cleaned_data["name"]
            dni = form.cleaned_data["dni"]
            direccion = form.cleaned_data["direccion"]
            email = form.cleaned_data["email"]
            telefono = form.cleaned_data["telefono"]
            movil = form.cleaned_data["movil"]
            fechanacimiento = form.cleaned_data["fechanacimiento"]
            nacionalidad = form.cleaned_data["nacionalidad"]
            estadocivil = form.cleaned_data["estadocivil"]
            tipocasado = form.cleaned_data["tipocasado"]
            numerohijos = form.cleaned_data["numerohijos"]
            mayoresdeedad = form.cleaned_data["mayoresdeedad"]
            cuantosacargo = form.cleaned_data["cuantosacargo"]
            ingresohijos = form.cleaned_data["ingresohijos"]
            anotacionespersonales = form.cleaned_data["anotacionespersonales"]
            cotizacion = form.cleaned_data["cotizacion"]
            tipotrabajo = form.cleaned_data["tipotrabajo"]
            finalizacontrato = form.cleaned_data["finalizacontrato"]
            nombreempresa1 = form.cleaned_data["nombreempresa1"]
            cargoempresa1 = form.cleaned_data["cargoempresa1"]
            actividadempresa1 = form.cleaned_data["actividadempresa1"]
            ingresosempresa1 = form.cleaned_data["ingresosempresa1"]
            pagasempresa1 = form.cleaned_data["pagasempresa1"]
            otrosingresosempresa1 = form.cleaned_data["otrosingresosempresa1"]
            antiguedadempresa1 = form.cleaned_data["antiguedadempresa1"]
            nombreempresa2 = form.cleaned_data["nombreempresa2"]
            cargoempresa2 = form.cleaned_data["cargoempresa2"]
            actividadempresa2 = form.cleaned_data["actividadempresa2"]
            ingresosempresa2 = form.cleaned_data["ingresosempresa2"]
            pagasempresa2 = form.cleaned_data["pagasempresa2"]
            otrosingresosempresa2 = form.cleaned_data["otrosingresosempresa2"]
            antiguedadempresa2 = form.cleaned_data["antiguedadempresa2"]
            nombreempresa3 = form.cleaned_data["nombreempresa3"]
            cargoempresa3 = form.cleaned_data["cargoempresa3"]
            actividadempresa3 = form.cleaned_data["actividadempresa3"]
            ingresosempresa3 = form.cleaned_data["ingresosempresa3"]
            pagasempresa3 = form.cleaned_data["pagasempresa3"]
            otrosingresosempresa3 = form.cleaned_data["otrosingresosempresa3"]
            antiguedadempresa3 = form.cleaned_data["antiguedadempresa3"]
            importejuvilacion = form.cleaned_data["importejuvilacion"]
            numerodepagasjuvilacion = form.cleaned_data["numerodepagasjuvilacion"]
            iniciojuvilacion = form.cleaned_data["iniciojuvilacion"]
            finjuvilacion = form.cleaned_data["finjuvilacion"]
            parodesdecuando = form.cleaned_data["parodesdecuando"]
            parocuantocobra = form.cleaned_data["parocuantocobra"]
            otrosingresos = form.cleaned_data["otrosingresos"]
            otrosgastos = form.cleaned_data["otrosgastos"]
            otrosingresostexto = form.cleaned_data["otrosingresostexto"]
            otrosgastostexto = form.cleaned_data["otrosgastostexto"]
            anotacionesingresos = form.cleaned_data["anotacionesingresos"]
            viviendavalor1 = form.cleaned_data["viviendavalor1"]
            viviendavalorhipoteca1 = form.cleaned_data["viviendavalorhipoteca1"]
            viviendaestapagada1 = form.cleaned_data["viviendaestapagada1"]
            viviendalibredecargos1 = form.cleaned_data["viviendalibredecargos1"]
            viviendacuotamensual1 = form.cleaned_data["viviendacuotamensual1"]
            viviendaanos1 = form.cleaned_data["viviendaanos1"]
            viviendaentidad1 = form.cleaned_data["viviendaentidad1"]
            viviendametros1 = form.cleaned_data["viviendametros1"]
            viviendaporciento1 = form.cleaned_data["viviendaporciento1"]
            viviendadireccion1 = form.cleaned_data["viviendadireccion1"]
            viviendapoblacion1 = form.cleaned_data["viviendapoblacion1"]
            viviendaprovincia1 = form.cleaned_data["viviendaprovincia1"]
            viviendacodigopostal1 = form.cleaned_data["viviendacodigopostal1"]
            viviendavalor2 = form.cleaned_data["viviendavalor2"]
            viviendavalorhipoteca2 = form.cleaned_data["viviendavalorhipoteca2"]
            viviendaestapagada2 = form.cleaned_data["viviendaestapagada2"]
            viviendalibredecargos2 = form.cleaned_data["viviendalibredecargos2"]
            viviendacuotamensual2 = form.cleaned_data["viviendacuotamensual2"]
            viviendaanos2 = form.cleaned_data["viviendaanos2"]
            viviendaentidad2 = form.cleaned_data["viviendaentidad2"]
            viviendametros2 = form.cleaned_data["viviendametros2"]
            viviendaporciento2 = form.cleaned_data["viviendaporciento2"]
            viviendadireccion2 = form.cleaned_data["viviendadireccion2"]
            viviendapoblacion2 = form.cleaned_data["viviendapoblacion2"]
            viviendaprovincia2 = form.cleaned_data["viviendaprovincia2"]
            viviendacodigopostal2 = form.cleaned_data["viviendacodigopostal2"]
            viviendavalor3 = form.cleaned_data["viviendavalor3"]
            viviendavalorhipoteca3 = form.cleaned_data["viviendavalorhipoteca3"]
            viviendaestapagada3 = form.cleaned_data["viviendaestapagada3"]
            viviendalibredecargos3 = form.cleaned_data["viviendalibredecargos3"]
            viviendacuotamensual3 = form.cleaned_data["viviendacuotamensual3"]
            viviendaanos3 = form.cleaned_data["viviendaanos3"]
            viviendaentidad3 = form.cleaned_data["viviendaentidad3"]
            viviendametros3 = form.cleaned_data["viviendametros3"]
            viviendaporciento3 = form.cleaned_data["viviendaporciento3"]
            viviendadireccion3 = form.cleaned_data["viviendadireccion3"]
            viviendapoblacion3 = form.cleaned_data["viviendapoblacion3"]
            viviendaprovincia3 = form.cleaned_data["viviendaprovincia3"]
            viviendacodigopostal3 = form.cleaned_data["viviendacodigopostal3"]
            viviendaalquiladavalor1 = form.cleaned_data["viviendaalquiladavalor1"]
            viviendaalquiladavalorhipoteca1 = form.cleaned_data["viviendaalquiladavalorhipoteca1"]
            viviendaalquiladaestapagada1 = form.cleaned_data["viviendaalquiladaestapagada1"]
            viviendaalquiladalibredecargos1 = form.cleaned_data["viviendaalquiladalibredecargos1"]
            viviendaalquiladacuotamensual1 = form.cleaned_data["viviendaalquiladacuotamensual1"]
            viviendaalquiladaanos1 = form.cleaned_data["viviendaalquiladaanos1"]
            viviendaalquiladaentidad1 = form.cleaned_data["viviendaalquiladaentidad1"]
            viviendaalquiladametros1 = form.cleaned_data["viviendaalquiladametros1"]
            viviendaalquiladaporciento1 = form.cleaned_data["viviendaalquiladaporciento1"]
            viviendaalquiladadireccion1 = form.cleaned_data["viviendaalquiladadireccion1"]
            viviendaalquiladapoblacion1 = form.cleaned_data["viviendaalquiladapoblacion1"]
            viviendaalquiladaprovincia1 = form.cleaned_data["viviendaalquiladaprovincia1"]
            viviendaalquiladacodigopostal1 = form.cleaned_data["viviendaalquiladacodigopostal1"]
            viviendaalquiladacobraalquiler1 = form.cleaned_data["viviendaalquiladacobraalquiler1"]
            viviendaalquiladavalor2 = form.cleaned_data["viviendaalquiladavalor2"]
            viviendaalquiladavalorhipoteca2 = form.cleaned_data["viviendaalquiladavalorhipoteca2"]
            viviendaalquiladaestapagada2 = form.cleaned_data["viviendaalquiladaestapagada2"]
            viviendaalquiladalibredecargos2 = form.cleaned_data["viviendaalquiladalibredecargos2"]
            viviendaalquiladacuotamensual2 = form.cleaned_data["viviendaalquiladacuotamensual2"]
            viviendaalquiladaanos2 = form.cleaned_data["viviendaalquiladaanos2"]
            viviendaalquiladaentidad2 = form.cleaned_data["viviendaalquiladaentidad2"]
            viviendaalquiladametros2 = form.cleaned_data["viviendaalquiladametros2"]
            viviendaalquiladaporciento2 = form.cleaned_data["viviendaalquiladaporciento2"]
            viviendaalquiladadireccion2 = form.cleaned_data["viviendaalquiladadireccion2"]
            viviendaalquiladapoblacion2 = form.cleaned_data["viviendaalquiladapoblacion2"]
            viviendaalquiladaprovincia2 = form.cleaned_data["viviendaalquiladaprovincia2"]
            viviendaalquiladacodigopostal2 = form.cleaned_data["viviendaalquiladacodigopostal2"]
            viviendaalquiladacobraalquiler2 = form.cleaned_data["viviendaalquiladacobraalquiler2"]
            viviendaalquiladavalor3 = form.cleaned_data["viviendaalquiladavalor3"]
            viviendaalquiladavalorhipoteca3 = form.cleaned_data["viviendaalquiladavalorhipoteca3"]
            viviendaalquiladaestapagada3 = form.cleaned_data["viviendaalquiladaestapagada3"]
            viviendaalquiladalibredecargos3 = form.cleaned_data["viviendaalquiladalibredecargos3"]
            viviendaalquiladacuotamensual3 = form.cleaned_data["viviendaalquiladacuotamensual3"]
            viviendaalquiladaanos3 = form.cleaned_data["viviendaalquiladaanos3"]
            viviendaalquiladaentidad3 = form.cleaned_data["viviendaalquiladaentidad3"]
            viviendaalquiladametros3 = form.cleaned_data["viviendaalquiladametros3"]
            viviendaalquiladaporciento3 = form.cleaned_data["viviendaalquiladaporciento3"]
            viviendaalquiladadireccion3 = form.cleaned_data["viviendaalquiladadireccion3"]
            viviendaalquiladapoblacion3 = form.cleaned_data["viviendaalquiladapoblacion3"]
            viviendaalquiladaprovincia3 = form.cleaned_data["viviendaalquiladaprovincia3"]
            viviendaalquiladacodigopostal3 = form.cleaned_data["viviendaalquiladacodigopostal3"]
            viviendaalquiladacobraalquiler3 = form.cleaned_data["viviendaalquiladacobraalquiler3"]
            alquilerpaga1 = form.cleaned_data["alquilerpaga1"]
            alquilermetros1 = form.cleaned_data["alquilermetros1"]
            alquilerdireccion1 = form.cleaned_data["alquilerdireccion1"]
            alquilerpoblacion1 = form.cleaned_data["alquilerpoblacion1"]
            alquilerprovincia1 = form.cleaned_data["alquilerprovincia1"]
            alquilercodigopostal1 = form.cleaned_data["alquilercodigopostal1"]
            alquilerpaga2 = form.cleaned_data["alquilerpaga2"]
            alquilermetros2 = form.cleaned_data["alquilermetros2"]
            alquilerdireccion2 = form.cleaned_data["alquilerdireccion2"]
            alquilerpoblacion2 = form.cleaned_data["alquilerpoblacion2"]
            alquilerprovincia2 = form.cleaned_data["alquilerprovincia2"]
            alquilercodigopostal2 = form.cleaned_data["alquilercodigopostal2"]
            alquilerpaga3 = form.cleaned_data["alquilerpaga3"]
            alquilermetros3 = form.cleaned_data["alquilermetros3"]
            alquilerdireccion3 = form.cleaned_data["alquilerdireccion3"]
            alquilerpoblacion3 = form.cleaned_data["alquilerpoblacion3"]
            alquilerprovincia3 = form.cleaned_data["alquilerprovincia3"]
            alquilercodigopostal3 = form.cleaned_data["alquilercodigopostal3"]
            direccionpersonal = form.cleaned_data["direccionpersonal"]
            poblacionpersonal = form.cleaned_data["poblacionpersonal"]
            provinciapersonal = form.cleaned_data["provinciapersonal"]
            codigopostalpersonal = form.cleaned_data["codigopostalpersonal"]
            anotacionesviviendas = form.cleaned_data["anotacionesviviendas"]
            creditotipo1 = form.cleaned_data["creditotipo1"]
            creditotantoporciento1 = form.cleaned_data["creditotantoporciento1"]
            creditoimporte1 = form.cleaned_data["creditoimporte1"]
            creditocuota1 = form.cleaned_data["creditocuota1"]
            creditoentidad1 = form.cleaned_data["creditoentidad1"]
            creditotipo2 = form.cleaned_data["creditotipo2"]
            creditotantoporciento2 = form.cleaned_data["creditotantoporciento2"]
            creditoimporte2 = form.cleaned_data["creditoimporte2"]
            creditocuota2 = form.cleaned_data["creditocuota2"]
            creditoentidad2 = form.cleaned_data["creditoentidad2"]
            creditotipo3 = form.cleaned_data["creditotipo3"]
            creditotantoporciento3 = form.cleaned_data["creditotantoporciento3"]
            creditoimporte3 = form.cleaned_data["creditoimporte3"]
            creditocuota3 = form.cleaned_data["creditocuota3"]
            creditoentidad3 = form.cleaned_data["creditoentidad3"]
            tarjetacuota1 = form.cleaned_data["tarjetacuota1"]
            tarjetaimporte1 = form.cleaned_data["tarjetaimporte1"]
            tarjetaentidad1 = form.cleaned_data["tarjetaentidad1"]
            tarjetacuota2 = form.cleaned_data["tarjetacuota2"]
            tarjetaimporte2 = form.cleaned_data["tarjetaimporte2"]
            tarjetaentidad2 = form.cleaned_data["tarjetaentidad2"]
            tarjetacuota3 = form.cleaned_data["tarjetacuota3"]
            tarjetaimporte3 = form.cleaned_data["tarjetaimporte3"]
            tarjetaentidad3 = form.cleaned_data["tarjetaentidad3"]
            recivosimporte1 = form.cleaned_data["recivosimporte1"]
            recivosimporte2 = form.cleaned_data["recivosimporte2"]
            recivosimporte3 = form.cleaned_data["recivosimporte3"]
            morosoimporte1 = form.cleaned_data["morosoimporte1"]
            morosoquien1 = form.cleaned_data["morosoquien1"]
            morosoimporte2 = form.cleaned_data["morosoimporte2"]
            morosoquien2 = form.cleaned_data["morosoquien2"]
            morosoimporte3 = form.cleaned_data["morosoimporte3"]
            morosoquien3 = form.cleaned_data["morosoquien3"]
            anotacionesfinancieras = form.cleaned_data["anotacionesfinancieras"]
            motor = form.cleaned_data["motor"]
            marca = form.cleaned_data["marca"]
            modelo = form.cleaned_data["modelo"]
            antiguedad = form.cleaned_data["antiguedad"]
            matricula = form.cleaned_data["matricula"]
            estadovehiculo = form.cleaned_data["estadovehiculo"]
            anotacionescoche = form.cleaned_data["anotacionescoche"]
            metodopago = form.cleaned_data["metodopago"]
            anotacionesdestinado = form.cleaned_data["anotacionesdestinado"]
            justificante = form.cleaned_data["justificante"]
            autorizacion = form.cleaned_data["autorizacion"]
            medio = form.cleaned_data["medio"]
            anotacionesgenerales = form.cleaned_data["anotacionesgenerales"]

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
                                                                otrosgastostexto=otrosgastostexto,
                                                                importeselect1=importeselect1,
                                                                importeselect2=importeselect2,
                                                                importeselect3=importeselect3)
            paro = models.paro.objectos.create(numexp=numexp, desdecuando=parodesdecuando, cobra=parocuantocobra)
            juvilacion = models.juvilacion.objetos.create(numexp, importe=importejuvilacion,
                                                          pagas=numerodepagasjuvilacion, fechainicio=iniciojuvilacion,
                                                          fechafin=finjuvilacion)
            anotaciones = models.anotaciones.objects.create(numexp=numexp, personales=anotacionespersonales,
                                                            empresa=anotacionesingresos, vivienda=anotacionesviviendas,
                                                            financieros=anotacionesfinancieras,
                                                            destinado=anotacionesdestinado,
                                                            generales=anotacionesgenerales)
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
            return HttpResponseRedirect('/formularios/microcredito/')

    else:
        form = forms.formMicrocredito()
        datayhora = datetime.now()
        expedient = models.expediente.objects.create(numexp=numexp, tipo="Microcredito", fecha_hora=datayhora)
        context.update({"form": form})
        context.update({"numexp": numexp})
    return render(request, 'form_microcre.html', context)

