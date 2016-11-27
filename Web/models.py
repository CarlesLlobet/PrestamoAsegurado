from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Empreses(models.Model):
    nom_empresa = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    actividad = models.CharField(max_length=50)
    ingresos = models.IntegerField()
    pagas_anuales = models.IntegerField()
    otros_ingresos = models.IntegerField()
    creation_date = models.DateField()

