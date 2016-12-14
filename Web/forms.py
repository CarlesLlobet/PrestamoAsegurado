# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate


class formLogin(forms.Form):
    def __init__(self, *args, **kwargs):
        super(formLogin, self).__init__(*args, **kwargs)

    username = forms.UserField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}))
    password = forms.UserField(widget=forms.TextInput(attrs={"max_length": 100, "class": "form-control"}))

    def clean(self):
        cleaned_data = super(formLogin, self).clean()
        usr = cleaned_data['username']
        passwd = cleaned_data['passwd']

        user = authenticate(username = usr, password= passwd)
        if user is None:
            raise forms.ValidationError(
                _(u'Usuari o contraseña incorrectes'))
