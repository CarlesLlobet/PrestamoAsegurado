# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv4_address, EmailValidator, validate_email
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
    ('Soltero', 'MySQL'),
    ('Casado', 'Oracle')
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
                          error_messages=my_default_errors_DNI, validators=validarDNI())

    direccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                           error_messages=my_default_errors_direccion)

    email = forms.EmailField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                           error_messages=my_default_errors_email)

    telefono = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    movil = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}), error_message=my_default_errors_movil)

    fechanacimiento = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(
        options={"format": "YYYY-MM-DD", "pickSeconds": False}), error_messages=my_default_errors_fechanacimiento)

    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                           error_messages=my_default_errors_nacionalidad)

    estadocivil = forms.ChoiceField(widget=forms.Select(choices=EstatsCivils))

    tipocasado = forms.ChoiceField(widget=forms.Select(choices=)))

    numerohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    mayoresdeedad = forms.BooleanField(initial=False, required=False)

    cuantosacargo = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    ingresohijos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    anotacionespersonales = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),error_messages=my_default_errors_DNI)

    cotizacion = forms.ChoiceField(widget=forms.Select(choices=))

    tipotrabajo = forms.ChoiceField(widget=forms.Select(choices=))

    finalizacontrato = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickSeconds": False}), error_messages=my_default_errors_fechanacimiento)

    nombreempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    cargoempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    actividadempresa1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    ingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    pagasempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    otrosingresosempresa1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    antiguedadempresa1

    importejuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    numerodepagasjuvilacion = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    iniciojuvilacion = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(         options={"format": "YYYY-MM-DD", "pickSeconds": False}), error_messages=my_default_errors_fechanacimiento)

    finjuvilacion = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(         options={"format": "YYYY-MM-DD", "pickSeconds": False}), error_messages=my_default_errors_fechanacimiento)

    parodesdecuando = forms.DateTimeField(label='execute_date', required=False, widget=DateTimePicker(         options={"format": "YYYY-MM-DD", "pickSeconds": False}), error_messages=my_default_errors_fechanacimiento)

    parocuantocobra = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    otrosingresos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    otrosgastos = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    otrosingresostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),)

    otrosgastostexto = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),)

    anotacionesingresos = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    viviendavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaestapagada1 = forms.BooleanField(initial=False, required=False)

    viviendalibredecargos1 = forms.BooleanField(initial=False, required=False)

    viviendacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    viviendametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendadireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    viviendapoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    viviendaprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    viviendacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladavalor1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladavalorhipoteca1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaestapagada1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    viviendaalquiladalibredecargos1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    viviendaalquiladacuotamensual1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaanos1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    viviendaalquiladametros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladaporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladadireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    viviendaalquiladapoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    viviendaalquiladaprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    viviendaalquiladacodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    viviendaalquiladacobraalquiler = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilerpaga1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilermetros1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    alquilerdireccion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    alquilerpoblacion1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    alquilerprovincia1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    alquilercodigopostal1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    anotacionesviviendas = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    direccion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    poblacion = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    provincia = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    codigopostal = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    creditotipo1 = forms.ChoiceField(widget=forms.Select(choices=))

    creditotantoporciento1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    creditoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))

    creditocuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),)

    creditoentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    tarjetacuota1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),)

    tarjetaimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),)

    tarjetaentidad1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    recivosimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),)

    morosoimporte1 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),)

    morosoquien1 = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    anotacionesfinancieras = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    motor = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),)

    marca = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),)

    modelo = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),)

    antiguedad = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),)

    matricula = forms.CharField(widget=forms.TextInput(attrs={"max_length": 10, "class": "form-control"}),)

    estadovehiculo = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    anotacionescoche = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    recibirdinero = forms.ChoiceField(widget=forms.Select(choices=))

    anotacionesdestinado = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)

    justificante = forms.BooleanField(initial=False, required=False)

    autorizacion = forms.BooleanField(initial=False, required=False)

    medio = forms.ChoiceField(widget=forms.Select(choices=))

    anotacionesdestinado = forms.CharField(widget=forms.TextInput(attrs={"max_length": 500, "class": "form-control"}),)





    # Exemples
    periodicity_checkbox = forms.BooleanField(initial=False, required=False)(label='periodicity', initial=False, required=False)

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
