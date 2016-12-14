# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate


class formLogin(forms.Form):
    def __init__(self, *args, **kwargs):
        super(formLogin, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super(formLogin, self).clean()
        usr = cleaned_data['username']
        passwd = cleaned_data['password']

        user = authenticate(username=usr, password=passwd)
        if user is None:
            raise forms.ValidationError(
                _(u'Usuari o contraseña incorrectes'))
