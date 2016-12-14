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
my_default_errors_username = {
    'required': _(u'Completa este campo'),
}
my_default_errors_password = {
    'required': _(u'Completa este campo'),
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


class formBuscar(forms.Form):
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

    numexp = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    dni = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                          error_messages=my_default_errors_DNI, validators=[validarDNI])


class formExp(forms.Form):
    def __init__(self, *args, **kwargs):
        super(formCoche, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                               error_messages=my_default_errors_username)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"max_length": 100, "class": "form-control"}),
                               error_messages=my_default_errors_password)


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

    fechanacimiento = forms.DateTimeField(widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False}),
                                          error_messages=my_default_errors_fechanacimiento)

    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                   error_messages=my_default_errors_nacionalidad)

    estadocivil = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=EstatsCivils)

    tipocasado = forms.ChoiceField(widget=forms.Select(choices=TipoCasado))

    numerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)

    mayoresdeedad = forms.BooleanField(initial=False, required=False)

    cuantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    ingresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    anotacionespersonales = forms.CharField(widget=forms.Textarea(attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos personales...", "class": "form-control"}))

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


class formMicrocredito(forms.Form):
    def __init__(self, *args, **kwargs):
        super(formMicrocredito, self).__init__(*args, **kwargs)

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

    metodopago = forms.ChoiceField(widget=forms.Select(choices=RecibirMoney))

    anotacionesdestinado = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    justificante = forms.BooleanField(initial=False, required=False)

    autorizacion = forms.BooleanField(initial=False, required=False)

    medio = forms.ChoiceField(widget=forms.Select(choices=Medios))

    numexp = forms.CharField(disabled=True)

    datayhora = forms.DateTimeField(disabled=True)

    def clean(self):
        cleaned_data = super(formMicrocredito, self).clean()


class formPersonal(forms.Form):
    def __init__(self, *args, **kwargs):
        super(formPersonal, self).__init__(*args, **kwargs)

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

    estadocivil = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=EstatsCivils)

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

    avalistaame = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                  error_messages=my_default_errors_Name)
    avalistani = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                 error_messages=my_default_errors_DNI, validators=[validarDNI])
    avalistaireccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                       error_messages=my_default_errors_direccion)
    avalistamail = forms.EmailField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                    error_messages=my_default_errors_email, validators=[validate_email])
    avalistaelefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaovil = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                      error_messages=my_default_errors_movil)
    avalistaechanacimiento = forms.DateTimeField(required=False, widget=DateTimePicker(
        options={"format": "YYYY-MM-DD", "pickSeconds": False}),
                                                 error_messages=my_default_errors_fechanacimiento)
    avalistaacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                          error_messages=my_default_errors_nacionalidad)
    avalistastadocivil = forms.ChoiceField(widget=forms.Select(choices=EstatsCivils))
    avalistaipocasado = forms.ChoiceField(widget=forms.Select(choices=TipoCasado))
    avalistaumerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaayoresdeedad = forms.BooleanField(initial=False, required=False)
    avalistauantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistangresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistanotacionespersonales = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}))
    avalistaotizacion = forms.ChoiceField(widget=forms.Select(choices=Cotiza))
    avalistaipotrabajo = forms.ChoiceField(widget=forms.Select(choices=TipWork))
    avalistainalizacontrato = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(
        options={"format": "YYYY-MM-DD", "pickSeconds": False}),
                                                  error_messages=my_default_errors_fechanacimiento)
    avalistaombreempresa1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaargoempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistactividadempresa1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistangresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaagasempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistantiguedadempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaombreempresa2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaargoempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistactividadempresa2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistangresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaagasempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistantiguedadempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaombreempresa3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaargoempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistactividadempresa3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistangresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaagasempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistantiguedadempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistamportejuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaumerodepagasjuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaniciojuvilacion = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(
        options={"format": "YYYY-MM-DD", "pickSeconds": False}),
                                                  error_messages=my_default_errors_fechanacimiento)
    avalistainjuvilacion = forms.DateTimeField(label='execute_date', required=False,
                                               widget=DateTimePicker(
                                                   options={"format": "YYYY-MM-DD", "pickSeconds": False}))
    avalistaarodesdecuando = forms.DateTimeField(label='execute_date', required=False,
                                                 widget=DateTimePicker(
                                                     options={"format": "YYYY-MM-DD", "pickSeconds": False}))
    avalistaarocuantocobra = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosingresos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosgastos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosingresostexto = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), )
    avalistatrosgastostexto = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), )
    avalistanotacionesingresos = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaestapagada1 = forms.BooleanField(initial=False, required=False)
    avalistaiviendalibredecargos1 = forms.BooleanField(initial=False, required=False)
    avalistaiviendacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaestapagada2 = forms.BooleanField(initial=False, required=False)
    avalistaiviendalibredecargos2 = forms.BooleanField(initial=False, required=False)
    avalistaiviendacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendadireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendapoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaestapagada3 = forms.BooleanField(initial=False, required=False)
    avalistaiviendalibredecargos3 = forms.BooleanField(initial=False, required=False)
    avalistaiviendacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendadireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendapoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaestapagada1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladalibredecargos1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladacobraalquiler1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaestapagada2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladalibredecargos2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladadireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladapoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladaprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladacobraalquiler2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaestapagada3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladalibredecargos3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladadireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladapoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladaprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladacobraalquiler3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerpaga1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilermetros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerdireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerpoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilercodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerpaga2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilermetros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerdireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerpoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilercodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerpaga3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilermetros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerdireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerpoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilercodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistanotacionesviviendas = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaireccionpersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaoblacionpersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistarovinciapersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaodigopostalpersonal = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditotipo1 = forms.ChoiceField(widget=forms.Select(choices=CredTip))
    avalistareditotantoporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditocuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistareditoentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistareditotipo2 = forms.ChoiceField(widget=forms.Select(choices=CredTip))
    avalistareditotantoporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditocuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistareditoentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistareditotipo3 = forms.ChoiceField(widget=forms.Select(choices=CredTip))
    avalistareditotantoporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditocuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistareditoentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaarjetacuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaarjetacuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaarjetacuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaecivosimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaecivosimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaecivosimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaorosoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaorosoquien1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaorosoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaorosoquien2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaorosoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaorosoquien3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    def clean(self):
        cleaned_data = super(formPersonal, self).clean()


class formHipotecario(forms.Form):
    def __init__(self, *args, **kwargs):
        super(formHipotecario, self).__init__(*args, **kwargs)

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

    avalistaame = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                  error_messages=my_default_errors_Name)
    avalistani = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                 error_messages=my_default_errors_DNI, validators=[validarDNI])
    avalistaireccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                       error_messages=my_default_errors_direccion)
    avalistamail = forms.EmailField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                    error_messages=my_default_errors_email, validators=[validate_email])
    avalistaelefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaovil = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                      error_messages=my_default_errors_movil)
    avalistaechanacimiento = forms.DateTimeField(required=False, widget=DateTimePicker(
        options={"format": "YYYY-MM-DD", "pickSeconds": False}),
                                                 error_messages=my_default_errors_fechanacimiento)
    avalistaacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                          error_messages=my_default_errors_nacionalidad)
    avalistastadocivil = forms.ChoiceField(widget=forms.Select(choices=EstatsCivils))
    avalistaipocasado = forms.ChoiceField(widget=forms.Select(choices=TipoCasado))
    avalistaumerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaayoresdeedad = forms.BooleanField(initial=False, required=False)
    avalistauantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistangresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistanotacionespersonales = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}))
    avalistaotizacion = forms.ChoiceField(widget=forms.Select(choices=Cotiza))
    avalistaipotrabajo = forms.ChoiceField(widget=forms.Select(choices=TipWork))
    avalistainalizacontrato = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(
        options={"format": "YYYY-MM-DD", "pickSeconds": False}),
                                                  error_messages=my_default_errors_fechanacimiento)
    avalistaombreempresa1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaargoempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistactividadempresa1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistangresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaagasempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistantiguedadempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaombreempresa2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaargoempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistactividadempresa2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistangresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaagasempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistantiguedadempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaombreempresa3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaargoempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistactividadempresa3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistangresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaagasempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistantiguedadempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistamportejuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaumerodepagasjuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaniciojuvilacion = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(
        options={"format": "YYYY-MM-DD", "pickSeconds": False}),
                                                  error_messages=my_default_errors_fechanacimiento)
    avalistainjuvilacion = forms.DateTimeField(label='execute_date', required=False,
                                               widget=DateTimePicker(
                                                   options={"format": "YYYY-MM-DD", "pickSeconds": False}),
                                               error_messages=my_default_errors_fechanacimiento)
    avalistaarodesdecuando = forms.DateTimeField(label='execute_date', required=False,
                                                 widget=DateTimePicker(
                                                     options={"format": "YYYY-MM-DD", "pickSeconds": False}),
                                                 error_messages=my_default_errors_fechanacimiento)
    avalistaarocuantocobra = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosingresos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosgastos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistatrosingresostexto = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), )
    avalistatrosgastostexto = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), )
    avalistanotacionesingresos = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaestapagada1 = forms.BooleanField(initial=False, required=False)
    avalistaiviendalibredecargos1 = forms.BooleanField(initial=False, required=False)
    avalistaiviendacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaestapagada2 = forms.BooleanField(initial=False, required=False)
    avalistaiviendalibredecargos2 = forms.BooleanField(initial=False, required=False)
    avalistaiviendacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendadireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendapoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaestapagada3 = forms.BooleanField(initial=False, required=False)
    avalistaiviendalibredecargos3 = forms.BooleanField(initial=False, required=False)
    avalistaiviendacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendadireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendapoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaestapagada1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladalibredecargos1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladacobraalquiler1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaestapagada2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladalibredecargos2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladadireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladapoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladaprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladacobraalquiler2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaestapagada3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladalibredecargos3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladadireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladapoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladaprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaiviendaalquiladacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistaiviendaalquiladacobraalquiler3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerpaga1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilermetros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerdireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerpoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilercodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerpaga2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilermetros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerdireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerpoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilercodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerpaga3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilermetros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistalquilerdireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerpoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilerprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistalquilercodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistanotacionesviviendas = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaireccionpersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaoblacionpersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistarovinciapersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaodigopostalpersonal = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditotipo1 = forms.ChoiceField(widget=forms.Select(choices=CredTip))
    avalistareditotantoporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditocuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistareditoentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistareditotipo2 = forms.ChoiceField(widget=forms.Select(choices=CredTip))
    avalistareditotantoporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditocuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistareditoentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistareditotipo3 = forms.ChoiceField(widget=forms.Select(choices=CredTip))
    avalistareditotantoporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avalistareditocuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistareditoentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaarjetacuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaarjetacuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaarjetacuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaarjetaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaecivosimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaecivosimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaecivosimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaorosoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaorosoquien1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaorosoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaorosoquien2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )
    avalistaorosoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), )
    avalistaorosoquien3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), )

    def clean(self):
        cleaned_data = super(formHipotecario, self).clean()
