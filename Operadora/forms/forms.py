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
my_default_errors_numexp = {
    'required': _(u'Completa este campo'),
}
my_default_errors_data = {
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