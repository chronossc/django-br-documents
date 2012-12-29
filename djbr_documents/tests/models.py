# -*- coding: utf-8 -*-

from django.db import models
from djbr_documents.models import CPFField

class CPFModel(models.Model):
    cpf = CPFField()
