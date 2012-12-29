# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError
from br_documents import CPF, InvalidCPF


class CPFField(models.Field):

    verbose_name = 'CPF'
    description = "A CPF instance."

    __metaclass__ = models.SubfieldBase

    def __init__(self, enable_masked_widget=True, *a, **kw):
        kw['max_length'] = 11
        self.enable_masked_widget = enable_masked_widget
        super(CPFField, self).__init__(*a, **kw)

    def get_internal_type(self):
        return 'CharField'

    def to_python(self, value):
        # converts a string to CPF instance
        if not value:
            return value
        try:
            cpf = CPF(value)
        except InvalidCPF as err:
            raise ValidationError(err)
        else:
            return cpf

    def get_prep_value(self, value):
        # converts value to CPF string, with validation
        if not value:
            return value
        try:
            cpf = CPF(value)
        except InvalidCPF as err:
            raise ValidationError(err)
        else:
            return str(cpf)

    def get_prep_lookup(self, lookup_type, value):
        # supports for now, exact, iexact and in lookups
        if lookup_type in ('exact', 'iexact'):
            return self.get_prep_value(value)
        elif lookup_type == 'in':
            return [self.get_prep_value(v) for v in value]
        else:
            # TODO: support contains, icontains, startswith, istartswith,
            #       endswith and iendswith
            raise TypeError("Lookup type %r not supported." % lookup_type)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)

    def formfield(self, **kw):
        # return custon widget or not
        if self.enable_masked_widget:
            from djbr_documents.forms import CPFField as CPFFormField
            defaults = {'form_class': CPFFormField}
        else:
            from django import forms
            defaults = {'form_class': forms.CharField}
        defaults.update(kw)
        return super(CPFField, self).formfield(**defaults)


try:
    # Introspection rules for south, read more at:
    # http://south.aeracode.org/wiki/MyFieldsDontWork
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^djbr_documents\.models\.fields\.(.+?)(?:Field|ForeignKey)$'])
except ImportError:
    pass
