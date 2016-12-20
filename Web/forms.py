# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

my_default_errors = {
    'required': _(u'Completa este campo'),
}

class formLogin(forms.Form):
    def __init__(self, *args, **kwargs):
        super(formLogin, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages=my_default_errors)
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}), error_messages=my_default_errors)

    def clean(self):
        cleaned_data = super(formLogin, self).clean()
