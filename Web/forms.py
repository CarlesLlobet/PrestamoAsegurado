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

    name = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                           error_messages=my_default_errors_Name)

    dni = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                           error_messages=my_default_errors_DNI)
    level = forms.IntegerField(label='level')
    risk = forms.IntegerField(label='risk')
    depth = forms.IntegerField(label='depth')
    mail = forms.BooleanField(label='mail', initial=False, required=False)
    mail_field = forms.CharField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}),
                                 required=False, validators=[validate_email])

    # Periodicitat
    periodicity_checkbox = forms.BooleanField(label='periodicity', initial=False, required=False)
    periodicity = forms.ChoiceField(widget=forms.Select(attrs={"label": 'Periodicitat:'}), choices=Periodicities,
                                    validators=[validate_periodicity])

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
