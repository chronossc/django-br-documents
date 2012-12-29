# -*- coding: utf-8 -*-

from django import forms
from br_documents import CPF, InvalidCPF
from widgets import CPFWidget

class CPFField(forms.CharField):

    widget = CPFWidget()

    def clean(self, value):
        try:
            cpf = CPF(value)
        except InvalidCPF as err:
            raise forms.ValidationError(err)
        else:
            return str(cpf)
