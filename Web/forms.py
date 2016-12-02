# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv4_address, EmailValidator, validate_email
from django.utils.translation import ugettext_lazy as _

my_default_errors_Name = {
    'required': _(u'Completa este campo'),
    'max_length': _(u'Este campo no puede pasar de 100 carácteres')
}
my_default_errors_DNI = {
    'required': _(u'Completa este campo'),
    'max_length': _(u'Este campo no puede pasar de 10 carácteres'),
    'invalido': _(u'Este DNI no es válido')
}


class formCoche(forms.Form):
    def __init__(self, *args, **kwargs):
        super(formCoche, self).__init__(*args, **kwargs)

    def validarDNI(value):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
        numeros = "1234567890"
        dni = value.upper()
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            if not len(dni) == len([n for n in dni if n in numeros]) \
                    and tabla[int(dni) % 23] == dig_control:
                raise ValidationError(_(my_default_errors_DNI['invalido']))

    name = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                           error_messages=my_default_errors_Name)

    dni = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                          error_messages=my_default_errors_DNI, validators=validarDNI())

    direccion

    email

    telefono

    movil

    fechanacimiento

    nacionalidad

    estadocivil

    tipocasado

    numerohijos

    mayoresdeedad

    cuantosacargo

    ingresohijos

    anotacionespersonales

    cotizacion

    tipotrabajo

    finalizacontrato

    nombreempresa1

    cargoempresa1

    actividadempresa1

    ingresosempresa1

    pagasempresa1

    otrosingresosempresa1

    antiguedadempresa1

    importejuvilacion

    numerodepagasjuvilacion

    iniciojuvilacion

    finjuvilacion

    parodesdecuando

    parocuantocobra

    otrosingresos

    otrosgastos

    otrosingresostexto

    otrosgastostexto

    anotacionesingresos

    viviendavalor1

    viviendavalorhipoteca1

    viviendaestapagada1

    viviendalibredecargos1

    viviendacuotamensual1

    viviendaanos1

    viviendaentidad1

    viviendametros1

    viviendaporciento1

    viviendadireccion1

    viviendapoblacion1

    viviendaprovincia1

    viviendacodigopostal1

    viviendaalquiladavalor1

    viviendaalquiladavalorhipoteca1

    viviendaalquiladaestapagada1

    viviendaalquiladalibredecargos1

    viviendaalquiladacuotamensual1

    viviendaalquiladaanos1

    viviendaalquiladaentidad1

    viviendaalquiladametros1

    viviendaalquiladaporciento1

    viviendaalquiladadireccion1

    viviendaalquiladapoblacion1

    viviendaalquiladaprovincia1

    viviendaalquiladacodigopostal1

    viviendaalquiladacobraalquiler

    alquilerpaga1

    alquilermetros1

    alquilerdireccion1

    alquilerpoblacion1

    alquilerprovincia1

    alquilercodigopostal1

    anotacionesviviendas

    direccion

    poblacion

    provincia

    codigopostal

    creditotipo1

    creditotantoporciento1

    creditoimporte1

    creditocuota1

    creditoentidad1

    tarjetacuota1

    tarjetaimporte1

    tarjetaentidad1

    recivosimporte1

    morosoimporte1

    morosoquien1

    anotacionesfinancieras

    motor

    marca

    modelo

    antiguedad

    matricula

    estadovehiculo

    anotacionescoche

    recibirdinero

    anotacionesdestinado

    justificante

    autorizacion

    medio

    anotacionesdestinado





    # Exemples
    periodicity_checkbox = forms.BooleanField(label='periodicity', initial=False, required=False)
    periodicity = forms.ChoiceField(widget=forms.Select(attrs={"label": 'Periodicitat:'}), choices=Periodicities,
                                    )

    execute_date = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(
        options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False}))

    def clean(self):
        cleaned_data = super(formCoche, self).clean()
        url = cleaned_data.get("url")
        user = cleaned_data.get("user")
        password = cleaned_data.get("password")
        ip = cleaned_data.get("ip")
        port = cleaned_data.get("port")
        db_name = cleaned_data.get("db_name")
        verbosity = cleaned_data.get("verbosity")
        level = cleaned_data.get("level")
        risk = cleaned_data.get("risk")
        depth = cleaned_data.get("depth")

        print port
        raise forms.ValidationError(
            _("Siusplau especifica com a minim 1 target, o per URL o per connexio directa a Base de Dades"))
        if url == "" and user == "" and (password != "" or ip != "" or port != None or db_name != ""):
            self.add_error('user', (_("Especifica un nom d'usuari")))
        if url == "" and password == "" and (user != "" or ip != "" or port != None or db_name != ""):
            self.add_error('password', (_("Especifica una contrasenya")))
        if url == "" and ip == "" and (password != "" or user != "" or port != None or db_name != ""):
            self.add_error('ip', (_("Especifica una direccio IP")))
        if url == "" and port == None and (password != "" or ip != "" or user != "" or db_name != ""):
            self.add_error('port', (_("Especifica un port")))
        if url == "" and db_name == "" and (password != "" or ip != "" or port != None or user != ""):
            self.add_error('db_name', (_("Especifica un nom de base de dades")))
        if verbosity < 0 or verbosity > 6 or level < 1 or level > 5 or risk < 1 or risk > 3 or depth < 0 or depth > 10:
            print str(verbosity)
            ", "
            str(level)
            ", "
            str(risk)
            ", "
            str(depth)
            raise forms.ValidationError(
                _("Els camps level, verbosity, risk, i depth no poden tenir valors fora del rang del slider"))
