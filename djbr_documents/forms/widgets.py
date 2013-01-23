# -*- coding: utf-8 -*-

from django import forms

class CPFWidget(forms.TextInput):

    default_attrs = {'data-cpf-mask': '999.999.999-99'}

    class Media:
        js = ('djbr_documents/jquery.maskedinput-1.3.min.js',
              'djbr_documents/cpfmask.js')

    def __init__(self, *a, **kw):
        super(CPFWidget, self).__init__(*a, **kw)
        self.attrs.update(self.default_attrs)

    def render(self, *a, **kw):
        return super(CPFWidget, self).render(*a, **kw)
