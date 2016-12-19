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

importeselect1 = {
    ('Seleccionar', 'Seleccionar'),

}

importeselect2 = {
    ('Seleccionar', 'Seleccionar'),

}

EstatsCivils = (
    ('', 'Seleccionar'),
    ('Soltero', 'Soltero'),
    ('Viudo', 'Viudo'),
    ('Divorciado', 'Divorciado'),
    ('Pareja de hecho', 'Pareja de hecho'),
    ('Casado', 'Casado')
)

TipoCasado = (
    ('', 'Seleccionar'),
    ('Separacion de bienes', 'Separacion de bienes'),
    ('Bienes gananciales', 'Bienes gananciales')
)

Cotiza = (
    ('', 'Seleccionar'),
    ('Propia', 'Propia'),
    ('Ajena', 'Ajena')
)

TipWork = (
    ('', 'Seleccionar'),
    ('Fijo', 'Fijo'),
    ('Indefinido', 'Indefinido'),
    ('Temporal', 'Temporal')
)

CredTip = (
    ('', 'Seleccionar'),
    ('Titular', 'Titular'),
    ('Avalista', 'Avalista')
)

RecibirMoney = (
    ('', 'Seleccionar'),
    ('Cuenta Bancaria', 'Cuenta Bancaria'),
    ('Hal-Cash', 'Hal-Cash')
)

Medios = (
    ('', 'Seleccionar'),
    ('Television', 'Television'),
    ('Prensa', 'Prensa'),
    ('Radio', 'Radio'),
    ('Web', 'Web'),
    ('Publicidad Estatica', 'Publicidad Estatica'),
    ('Otros', 'Otros')
)


class formBuscar(forms.Form):
    def __init__(self, *args, **kwargs):
        super(formBuscar, self).__init__(*args, **kwargs)

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

    numexp = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)

    dni = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                          error_messages=my_default_errors_DNI, validators=[validarDNI], required=False)

    def clean(self):
        cleaned_data = super(formBuscar, self).clean()
        dni = cleaned_data['dni']
        numexp = cleaned_data['numexp']

        if dni == "" and numexp == "":
            raise forms.ValidationError(
                _(u'Siusplau especifica un DNI o Número d\'Expedient a buscar'))


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

    # PERSONALES
    name = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                           error_messages=my_default_errors_Name)
    dni = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                          error_messages=my_default_errors_DNI, validators=[validarDNI])
    direccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                error_messages=my_default_errors_direccion)
    email = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                            error_messages=my_default_errors_email, validators=[validate_email])
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    movil = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                               error_messages=my_default_errors_movil)
    fechanacimiento = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        error_messages=my_default_errors_fechanacimiento)
    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                   error_messages=my_default_errors_nacionalidad)
    estadocivil = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=EstatsCivils, required=False)
    tipocasado = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=TipoCasado, required=False)
    numerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    mayoresdeedad = forms.BooleanField(initial=False, required=False)
    cuantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    ingresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    anotacionespersonales = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos personales...",
               "class": "form-control"}), required=False)
    # EMPRESA
    cotizacion = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=Cotiza, required=False)
    tipotrabajo = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=TipWork, required=False)
    finalizacontrato = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    nombreempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    nombreempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    nombreempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    importejuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    numerodepagasjuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    iniciojuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    finjuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    parodesdecuando = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    parocuantocobra = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosgastos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                         required=False)
    otrosgastostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                       required=False)
    anotacionesingresos = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los ingresos...",
               "class": "form-control"}), required=False)
    # VIVIENDA 1
    viviendavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada1 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos1 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada2 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos2 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada3 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos3 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # VIVIENDA2
    viviendaalquiladavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    # VIVIENDA3
    alquilerpaga1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerpaga2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerpaga3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # VIVIENDA4
    direccionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    poblacionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    provinciapersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    codigopostalpersonal = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    anotacionesviviendas = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para las viviendas...",
               "class": "form-control"}), required=False)
    # CREDITOS
    creditotipo1 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    creditotipo2 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    creditotipo3 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    # TARJETAS
    tarjetacuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    tarjetacuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    tarjetacuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    # RECIVOS
    recivosimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    recivosimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    recivosimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # MOROSOS
    morosoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    morosoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    morosoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    anotacionesfinancieras = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos financieros...",
               "class": "form-control"}), required=False)
    # COCHE
    motor = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}))
    marca = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}))
    modelo = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}))
    antiguedad = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}))
    matricula = forms.CharField(widget=forms.TextInput(attrs={"max_length": 10, "class": "form-control"}))
    estadovehiculo = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}))
    anotacionescoche = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos del coche...",
               "class": "form-control"}), required=False)
    metodopago = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=RecibirMoney, required=False)
    anotacionesdestinado = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para que va destinada la solicitud...",
               "class": "form-control"}), required=False)
    justificante = forms.BooleanField(initial=False, required=False)
    autorizacion = forms.BooleanField(initial=False, required=False)
    medio = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                              choices=Medios, required=False)
    anotacionesgenerales = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Observaciones generales...",
               "class": "form-control"}), required=False)
    # NECESARIOS
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

    # IMPORTES
    importeselect1 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                       choices=importeselect1, required=False)
    importeselect2 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                       choices=importeselect2, required=False)
    importeselect3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # PERSONALES
    name = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                           error_messages=my_default_errors_Name)
    dni = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                          error_messages=my_default_errors_DNI, validators=[validarDNI])
    direccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                error_messages=my_default_errors_direccion)
    email = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                            error_messages=my_default_errors_email, validators=[validate_email])
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    movil = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                               error_messages=my_default_errors_movil)
    fechanacimiento = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        error_messages=my_default_errors_fechanacimiento)
    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                   error_messages=my_default_errors_nacionalidad)
    estadocivil = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=EstatsCivils, required=False)
    tipocasado = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=TipoCasado, required=False)
    numerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    mayoresdeedad = forms.BooleanField(initial=False, required=False)
    cuantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    ingresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    anotacionespersonales = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos personales...",
               "class": "form-control"}), required=False)
    # EMPRESA
    cotizacion = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=Cotiza, required=False)
    tipotrabajo = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=TipWork, required=False)
    finalizacontrato = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    nombreempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    nombreempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    nombreempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    importejuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    numerodepagasjuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    iniciojuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    finjuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    parodesdecuando = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    parocuantocobra = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosgastos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                         required=False)
    otrosgastostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                       required=False)
    anotacionesingresos = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los ingresos...",
               "class": "form-control"}), required=False)
    # VIVIENDA 1
    viviendavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada1 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos1 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada2 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos2 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada3 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos3 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # VIVIENDA2
    viviendaalquiladavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    # VIVIENDA3
    alquilerpaga1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerpaga2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerpaga3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # VIVIENDA4
    direccionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    poblacionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    provinciapersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    codigopostalpersonal = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    anotacionesviviendas = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para las viviendas...",
               "class": "form-control"}), required=False)
    # CREDITOS
    creditotipo1 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    creditotipo2 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    creditotipo3 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    # TARJETAS
    tarjetacuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    tarjetacuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    tarjetacuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    # RECIVOS
    recivosimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    recivosimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    recivosimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # MOROSOS
    morosoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    morosoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    morosoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    anotacionesfinancieras = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos financieros...",
               "class": "form-control"}), required=False)
    # NECESARIOS
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

    # PERSONALES
    name = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                           error_messages=my_default_errors_Name)
    dni = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                          error_messages=my_default_errors_DNI, validators=[validarDNI])
    direccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                error_messages=my_default_errors_direccion)
    email = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                            error_messages=my_default_errors_email, validators=[validate_email])
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    movil = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                               error_messages=my_default_errors_movil)
    fechanacimiento = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        error_messages=my_default_errors_fechanacimiento)
    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                   error_messages=my_default_errors_nacionalidad)
    estadocivil = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=EstatsCivils, required=False)
    tipocasado = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=TipoCasado, required=False)
    numerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    mayoresdeedad = forms.BooleanField(initial=False, required=False)
    cuantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    ingresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    anotacionespersonales = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos personales...",
               "class": "form-control"}), required=False)
    # EMPRESA
    cotizacion = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=Cotiza, required=False)
    tipotrabajo = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=TipWork, required=False)
    finalizacontrato = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    nombreempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    nombreempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    nombreempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    importejuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    numerodepagasjuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    iniciojuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    finjuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    parodesdecuando = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    parocuantocobra = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosgastos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                         required=False)
    otrosgastostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                       required=False)
    anotacionesingresos = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los ingresos...",
               "class": "form-control"}), required=False)
    # VIVIENDA 1
    viviendavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada1 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos1 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada2 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos2 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada3 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos3 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # VIVIENDA2
    viviendaalquiladavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    # VIVIENDA3
    alquilerpaga1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerpaga2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerpaga3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # VIVIENDA4
    direccionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    poblacionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    provinciapersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    codigopostalpersonal = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    anotacionesviviendas = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para las viviendas...",
               "class": "form-control"}), required=False)
    # CREDITOS
    creditotipo1 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    creditotipo2 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    creditotipo3 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    # TARJETAS
    tarjetacuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    tarjetacuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    tarjetacuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    # RECIVOS
    recivosimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    recivosimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    recivosimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # MOROSOS
    morosoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    morosoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    morosoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    anotacionesfinancieras = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos financieros...",
               "class": "form-control"}), required=False)
    # PERSONALES AVALISTA
    avalistaame = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                  error_messages=my_default_errors_Name)
    avalistani = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                 error_messages=my_default_errors_DNI, validators=[validarDNI])
    avalistaireccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                       error_messages=my_default_errors_direccion)
    avalistamail = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                   error_messages=my_default_errors_email, validators=[validate_email])
    avalistaelefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaovil = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                      error_messages=my_default_errors_movil)
    avalistaechanacimiento = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        error_messages=my_default_errors_fechanacimiento)
    avalistaacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                          error_messages=my_default_errors_nacionalidad)
    avalistastadocivil = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=EstatsCivils,
                                           required=False)
    avalistaipocasado = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=TipoCasado,
                                          required=False)
    avalistaumerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaayoresdeedad = forms.BooleanField(initial=False, required=False)
    avalistauantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistangresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # EMPRESA AVALISTA
    avalistaotizacion = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=Cotiza,
                                          required=False)
    avalistaipotrabajo = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=TipWork,
                                           required=False)
    avalistainalizacontrato = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    avalistaombreempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                            required=False)
    avalistaargoempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                           required=False)
    avalistactividadempresa1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistangresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    avalistaagasempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistatrosingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                      required=False)
    avalistantiguedadempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                   required=False)
    avalistamportejuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    avalistaumerodepagasjuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    avalistaniciojuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    avalistainjuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    avalistaarodesdecuando = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    avalistaarocuantocobra = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistatrosingresos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistatrosgastos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistatrosingresostexto = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), required=False)
    avalistatrosgastostexto = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), required=False)
    # VIVIENDA 1 AVALISTA
    avalistaiviendavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaiviendavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                       required=False)
    avalistaiviendaestapagada1 = forms.BooleanField(initial=False, required=False)
    avalistaiviendalibredecargos1 = forms.BooleanField(initial=False, required=False)
    avalistaiviendacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                      required=False)
    avalistaiviendaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaiviendaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaiviendaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                   required=False)
    avalistaiviendadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                      required=False)
    # VIVIENDA2 AVALISTA
    avalistaiviendaalquiladavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    avalistaiviendaalquiladavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                                required=False)
    avalistaiviendaalquiladaestapagada1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladalibredecargos1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                               required=False)
    avalistaiviendaalquiladaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                       required=False)
    avalistaiviendaalquiladaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    avalistaiviendaalquiladaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                            required=False)
    avalistaiviendaalquiladadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                               required=False)
    avalistaiviendaalquiladacobraalquiler1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                                required=False)
    # VIVIENDA3 AVALISTA
    avalistalquilerpaga1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistalquilermetros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistalquilerdireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistalquilerpoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistalquilerprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistalquilercodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                      required=False)
    # VIVIENDA4 AVALISTA
    avalistaireccionpersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaoblacionpersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistarovinciapersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaodigopostalpersonal = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    # CREDITOS AVALISTA
    avalistareditotipo1 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=CredTip,
                                            required=False)
    avalistareditotantoporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                       required=False)
    avalistareditoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistareditocuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistareditoentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                             required=False)
    avalistareditotipo2 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=CredTip,
                                            required=False)
    avalistareditotantoporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                       required=False)
    avalistareditoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistareditocuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistareditoentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                             required=False)
    # TARJETAS AVALISTA
    avalistaarjetacuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaarjetaimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaarjetaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                             required=False)
    avalistaarjetacuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaarjetaimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaarjetaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                             required=False)
    # RECIVOS AVALISTA
    avalistaecivosimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaecivosimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # MOROSOS AVALISTA
    avalistaorosoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaorosoquien1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                          required=False)
    avalistaorosoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaorosoquien2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                          required=False)
    # NECESARIOS
    numexp = forms.CharField(disabled=True)
    datayhora = forms.DateTimeField(disabled=True)

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

    # PERSONALES
    name = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                           error_messages=my_default_errors_Name)
    dni = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                          error_messages=my_default_errors_DNI, validators=[validarDNI])
    direccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                error_messages=my_default_errors_direccion)
    email = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                            error_messages=my_default_errors_email, validators=[validate_email])
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    movil = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                               error_messages=my_default_errors_movil)
    fechanacimiento = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        error_messages=my_default_errors_fechanacimiento)
    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                   error_messages=my_default_errors_nacionalidad)
    estadocivil = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=EstatsCivils, required=False)
    tipocasado = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=TipoCasado, required=False)
    numerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    mayoresdeedad = forms.BooleanField(initial=False, required=False)
    cuantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    ingresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    anotacionespersonales = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos personales...",
               "class": "form-control"}), required=False)
    # EMPRESA
    cotizacion = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=Cotiza, required=False)
    tipotrabajo = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                    choices=TipWork, required=False)
    finalizacontrato = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    nombreempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    nombreempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    nombreempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                     required=False)
    cargoempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                    required=False)
    actividadempresa3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    ingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    pagasempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresosempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    antiguedadempresa3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    importejuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    numerodepagasjuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    iniciojuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    finjuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    parodesdecuando = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    parocuantocobra = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosgastos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    otrosingresostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                         required=False)
    otrosgastostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                       required=False)
    anotacionesingresos = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los ingresos...",
               "class": "form-control"}), required=False)
    # VIVIENDA 1
    viviendavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada1 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos1 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada2 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos2 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaestapagada3 = forms.BooleanField(initial=False, required=False)
    viviendalibredecargos3 = forms.BooleanField(initial=False, required=False)
    viviendacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                       required=False)
    viviendametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendadireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendapoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendaprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    viviendacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # VIVIENDA2
    viviendaalquiladavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladavalor2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia2 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladavalor3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    viviendaalquiladavalorhipoteca3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    viviendaalquiladaestapagada3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladalibredecargos3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacuotamensual3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladaanos3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    viviendaalquiladaentidad3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladametros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    viviendaalquiladaporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    viviendaalquiladadireccion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladapoblacion3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladaprovincia3 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    viviendaalquiladacodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    viviendaalquiladacobraalquiler3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    # VIVIENDA3
    alquilerpaga1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerpaga2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerpaga3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilermetros3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    alquilerdireccion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerpoblacion3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilerprovincia3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                         required=False)
    alquilercodigopostal3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # VIVIENDA4
    direccionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    poblacionpersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    provinciapersonal = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                        required=False)
    codigopostalpersonal = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    anotacionesviviendas = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para las viviendas...",
               "class": "form-control"}), required=False)
    # CREDITOS
    creditotipo1 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    creditotipo2 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    creditotipo3 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}),
                                     choices=CredTip, required=False)
    creditotantoporciento3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditocuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    creditoentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    # TARJETAS
    tarjetacuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    tarjetacuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    tarjetacuota3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    tarjetaentidad3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                      required=False)
    # RECIVOS
    recivosimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    recivosimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    recivosimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # MOROSOS
    morosoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    morosoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    morosoimporte3 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    morosoquien3 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                   required=False)
    anotacionesfinancieras = forms.CharField(widget=forms.Textarea(
        attrs={"max_length": 500, "rows": 5, "placeholder": "Anotaciones para los datos financieros...",
               "class": "form-control"}), required=False)
    # PERSONALES AVALISTA
    avalistaame = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                  error_messages=my_default_errors_Name)
    avalistani = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                 error_messages=my_default_errors_DNI, validators=[validarDNI])
    avalistaireccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                       error_messages=my_default_errors_direccion)
    avalistamail = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                   error_messages=my_default_errors_email, validators=[validate_email])
    avalistaelefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaovil = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                      error_messages=my_default_errors_movil)
    avalistaechanacimiento = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        error_messages=my_default_errors_fechanacimiento)
    avalistaacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                          error_messages=my_default_errors_nacionalidad)
    avalistastadocivil = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=EstatsCivils,
                                           required=False)
    avalistaipocasado = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=TipoCasado,
                                          required=False)
    avalistaumerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaayoresdeedad = forms.BooleanField(initial=False, required=False)
    avalistauantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistangresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # EMPRESA AVALISTA
    avalistaotizacion = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=Cotiza,
                                          required=False)
    avalistaipotrabajo = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=TipWork,
                                           required=False)
    avalistainalizacontrato = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    avalistaombreempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                            required=False)
    avalistaargoempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                           required=False)
    avalistactividadempresa1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistangresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                 required=False)
    avalistaagasempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistatrosingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                      required=False)
    avalistantiguedadempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                   required=False)
    avalistamportejuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                  required=False)
    avalistaumerodepagasjuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    avalistaniciojuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    avalistainjuvilacion = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    avalistaarodesdecuando = forms.DateTimeField(
        widget=DateTimePicker(attrs={"type": "date"}, options={"format": "YYYY-MM-DD", "pickTime": False}),
        required=False)
    avalistaarocuantocobra = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistatrosingresos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistatrosgastos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistatrosingresostexto = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), required=False)
    avalistatrosgastostexto = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}), required=False)
    # VIVIENDA 1 AVALISTA
    avalistaiviendavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaiviendavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                       required=False)
    avalistaiviendaestapagada1 = forms.BooleanField(initial=False, required=False)
    avalistaiviendalibredecargos1 = forms.BooleanField(initial=False, required=False)
    avalistaiviendacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                      required=False)
    avalistaiviendaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaiviendaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaiviendaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                   required=False)
    avalistaiviendadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                      required=False)
    # VIVIENDA2 AVALISTA
    avalistaiviendaalquiladavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                        required=False)
    avalistaiviendaalquiladavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                                required=False)
    avalistaiviendaalquiladaestapagada1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladalibredecargos1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                               required=False)
    avalistaiviendaalquiladaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                       required=False)
    avalistaiviendaalquiladaentidad1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                         required=False)
    avalistaiviendaalquiladaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                            required=False)
    avalistaiviendaalquiladadireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladapoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladaprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaiviendaalquiladacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                               required=False)
    avalistaiviendaalquiladacobraalquiler1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                                required=False)
    # VIVIENDA3 AVALISTA
    avalistalquilerpaga1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistalquilermetros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistalquilerdireccion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistalquilerpoblacion1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistalquilerprovincia1 = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistalquilercodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                      required=False)
    # VIVIENDA4 AVALISTA
    avalistaireccionpersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaoblacionpersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistarovinciapersonal = forms.CharField(
        widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}), required=False)
    avalistaodigopostalpersonal = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                     required=False)
    # CREDITOS AVALISTA
    avalistareditotipo1 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=CredTip,
                                            required=False)
    avalistareditotantoporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                       required=False)
    avalistareditoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistareditocuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistareditoentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                             required=False)
    avalistareditotipo2 = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=CredTip,
                                            required=False)
    avalistareditotantoporciento2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                                       required=False)
    avalistareditoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistareditocuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistareditoentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                             required=False)
    # TARJETAS AVALISTA
    avalistaarjetacuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaarjetaimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaarjetaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                             required=False)
    avalistaarjetacuota2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaarjetaimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaarjetaentidad2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                             required=False)
    # RECIVOS AVALISTA
    avalistaecivosimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaecivosimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    # MOROSOS AVALISTA
    avalistaorosoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaorosoquien1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                          required=False)
    avalistaorosoimporte2 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    avalistaorosoquien2 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),
                                          required=False)
    # NECESARIOS
    numexp = forms.CharField(disabled=True)
    datayhora = forms.DateTimeField(disabled=True)

    def clean(self):
        cleaned_data = super(formHipotecario, self).clean()
