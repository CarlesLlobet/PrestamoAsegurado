# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _
from bootstrap3_datetime.widgets import DateTimePicker

my_default_errors_Name = {
    'required': _(u'Completa este campo'),
    'max_length': _(u'Este campo no puede pasar de 100 carácteres')
}
my_default_errors_DNI = {
    'required': _(u'Completa este campo'),
    'max_length': _(u'Este campo no puede pasar de 10 carácteres'),
    'invalido': _(u'Este DNI no es válido')
}
my_default_errors_direccion = {
    'required': _(u'Completa este campo'),
    'max_length': _(u'Este campo no puede pasar de 100 carácteres')
}
my_default_errors_email = {
    'required': _(u'Completa este campo'),
    'invalid': _(u'Esto no es un correo valido. Ej: info@prestamoasegurado.com'),
}
my_default_errors_movil = {
    'required': _(u'Completa este campo'),
}
my_default_errors_fechanacimiento = {
    'required': _(u'Completa este campo'),
}
my_default_errors_nacionalidad = {
    'required': _(u'Completa este campo'),
    'max_length': _(u'Este campo no puede pasar de 100 carácteres')
}

EstatsCivils = (
    ('Soltero', 'Soltero'),
    ('Viudo', 'Viudo'),
    ('Divorciado', 'Divorciado'),
    ('Pareja de hecho', 'Pareja de hecho'),
    ('Casado', 'Casado')
)

TipoCasado = (
    ('Separacion de bienes', 'Separacion de bienes'),
    ('Bienes gananciales', 'Bienes gananciales')
)

Cotiza = (
    ('Propia', 'Propia'),
    ('Ajena', 'Ajena')
)

TipWork = (
    ('Fijo', 'Fijo'),
    ('Indefinido', 'Indefinido'),
    ('Temporal', 'Temporal')
)

CredTip = (
    ('Titular', 'Titular'),
    ('Avalista', 'Avalista')
)

RecibirMoney = (
    ('Cuenta Bancaria', 'Cuenta Bancaria'),
    ('Hal-Cash', 'Hal-Cash')
)

Medios = (
    ('Television', 'Television'),
    ('Prensa', 'Prensa'),
    ('Radio', 'Radio'),
    ('Web', 'Web'),
    ('Publicidad Estatica', 'Publicidad Estatica'),
    ('Otros', 'Otros')
)


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
                          error_messages=my_default_errors_DNI, validators=[validarDNI])

    direccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                error_messages=my_default_errors_direccion)

    email = forms.EmailField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                             error_messages=my_default_errors_email, validators=[validate_email])

    telefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    movil = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                               error_messages=my_default_errors_movil)

    fechanacimiento = forms.DateTimeField(required=False, widget=DateTimePicker(
        options={"format": "YYYY-MM-DD", "pickSeconds": False}), error_messages=my_default_errors_fechanacimiento)

    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                   error_messages=my_default_errors_nacionalidad)

    estadocivil = forms.ChoiceField(widget=forms.Select(choices=EstatsCivils))

    tipocasado = forms.ChoiceField(widget=forms.Select(choices=TipoCasado))

    numerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    mayoresdeedad = forms.BooleanField(initial=False, required=False)

    cuantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    ingresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    anotacionespersonales = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}))

    cotizacion = forms.ChoiceField(widget=forms.Select(choices=Cotiza))

    tipotrabajo = forms.ChoiceField(widget=forms.Select(choices=TipWork))

    finalizacontrato = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(
        options={"format": "YYYY-MM-DD", "pickSeconds": False}), error_messages=my_default_errors_fechanacimiento)

    nombreempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    cargoempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    actividadempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    ingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    pagasempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    otrosingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    antiguedadempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    nombreempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    cargoempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    actividadempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    ingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    pagasempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    otrosingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    antiguedadempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    nombreempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    cargoempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    actividadempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    ingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    pagasempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    otrosingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    antiguedadempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    importejuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    numerodepagasjuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    iniciojuvilacion = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(
        options={"format": "YYYY-MM-DD", "pickSeconds": False}), error_messages=my_default_errors_fechanacimiento)

    finjuvilacion = forms.DateTimeField(label='execute_date', required=False,
                                        widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickSeconds": False}),
                                        error_messages=my_default_errors_fechanacimiento)

    parodesdecuando = forms.DateTimeField(label='execute_date', required=False,
                                          widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickSeconds": False}),
                                          error_messages=my_default_errors_fechanacimiento)

    parocuantocobra = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    otrosingresos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    otrosgastos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    otrosingresostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), )

    otrosgastostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), )

    anotacionesingresos = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaestapagada1 = forms.BooleanField(initial=False, required=False)

    viviendalibredecargos1 = forms.BooleanField(initial=False, required=False)

    viviendacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendadireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendapoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaestapagada2 = forms.BooleanField(initial=False, required=False)

    viviendalibredecargos2 = forms.BooleanField(initial=False, required=False)

    viviendacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendadireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendapoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaestapagada3 = forms.BooleanField(initial=False, required=False)

    viviendalibredecargos3 = forms.BooleanField(initial=False, required=False)

    viviendacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendadireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendapoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaestapagada1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladalibredecargos1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladacobraalquiler1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaestapagada2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladalibredecargos2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladadireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladapoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladaprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladacobraalquiler2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaestapagada3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladalibredecargos3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladadireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladapoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladaprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    viviendaalquiladacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladacobraalquiler3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilerpaga1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilermetros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilerdireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    alquilerpoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    alquilerprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    alquilercodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilerpaga2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilermetros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilerdireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    alquilerpoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    alquilerprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    alquilercodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilerpaga3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilermetros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilerdireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    alquilerpoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    alquilerprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    alquilercodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    anotacionesviviendas = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    direccionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    poblacionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    provinciapersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    codigopostalpersonal = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    creditotipo1 = forms.ChoiceField(widget=forms.Select(choices=CredTip))

    creditotantoporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    creditoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    creditocuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    creditoentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    creditotipo2 = forms.ChoiceField(widget=forms.Select(choices=CredTip))

    creditotantoporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    creditoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    creditocuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    creditoentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    creditotipo3 = forms.ChoiceField(widget=forms.Select(choices=CredTip))

    creditotantoporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    creditoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    creditocuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    creditoentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    tarjetacuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    tarjetaimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    tarjetaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    tarjetacuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    tarjetaimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    tarjetaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    tarjetacuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    tarjetaimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    tarjetaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    recivosimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    recivosimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    recivosimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    morosoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    morosoquien1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    morosoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    morosoquien2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    morosoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    morosoquien3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    anotacionesfinancieras = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    motor = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), )

    marca = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), )

    modelo = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), )

    antiguedad = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )

    matricula = forms.CharField(widget=forms.TextInput(attrs={"max_length": 10, "class": "form-control"}), )

    estadovehiculo = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    anotacionescoche = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    metodopago = forms.ChoiceField(widget=forms.Select(choices=RecibirMoney))

    anotacionesdestinado = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    justificante = forms.BooleanField(initial=False, required=False)

    autorizacion = forms.BooleanField(initial=False, required=False)

    medio = forms.ChoiceField(widget=forms.Select(choices=Medios))

    numexp = forms.CharField(disabled=True)

    datayhora = forms.DateTimeField(disabled=True)

    def clean(self):
        cleaned_data = super(formCoche, self).clean()
