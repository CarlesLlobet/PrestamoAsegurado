from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


EstatsCivils = (
    ('Soltero', 'Soltero'),
    ('Viudo', 'Viudo'),
    ('Divorciado', 'Divorciado'),
    ('Pareja de hecho', 'Pareja de hecho'),
    ('Casado', 'Casado')
)

TipoCasado = (
    ('Separacion de bienes', 'Separacion de bienes'),
    ('Bienes gananciales', 'Bienes gananciales')
)

Cotiza = (
    ('Propia', 'Propia'),
    ('Ajena', 'Ajena')
)

TipWork = (
    ('Fijo', 'Fijo'),
    ('Indefinido', 'Indefinido'),
    ('Temporal', 'Temporal')
)

CredTip = (
    ('Titular', 'Titular'),
    ('Avalista', 'Avalista')
)

RecibirMoney = (
    ('Cuenta Bancaria', 'Cuenta Bancaria'),
    ('Hal-Cash', 'Hal-Cash')
)

Medios = (
    ('Television', 'Television'),
    ('Prensa', 'Prensa'),
    ('Radio', 'Radio'),
    ('Web', 'Web'),
    ('Publicidad Estatica', 'Publicidad Estatica'),
    ('Otros', 'Otros')
)

class expediente(models.Model):
    numexp = models.IntegerField()
    tipo = models.CharField(max_length=20)
    fecha_hora = models.DateTimeField(default=datetime.now)

class persona(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    telefono = models.IntegerField(null=True)
    movil = models.IntegerField()
    fechanacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    estadocivil = models.CharField(max_length=20, choices=EstatsCivils, null=True)
    tipocasado = models.CharField(max_length=20, choices=TipoCasado, null=True)
    numerodehijos = models.IntegerField(null=True)
    sihijosmayores18 = models.BooleanField(default=False)
    sihijoscuantoscargo = models.IntegerField(null=True)
    sihijosingreso = models.IntegerField(null=True)
    justificante = models.BooleanField(default=False)
    autoriza = models.BooleanField(default=False)
    medio = models.CharField(max_length=20, choices=Medios, null=True)
    metodopago = models.CharField(max_length=200, choices=RecibirMoney, null=True)


class personaanexos(models.Model):
    numexp = models.IntegerField(null=True)
    avalista = models.BooleanField(default=False)
    seguridadsocial = models.CharField(max_length=20, choices=Cotiza, null=True)
    siajenatipo = models.CharField(max_length=20, choices=TipWork, null=True)
    siajenatemporal = models.DateField(null=True)
    otrosingresos = models.IntegerField(null=True)
    otrosingresostexto = models.CharField(max_length=100, null=True)
    otrosgastos = models.IntegerField(null=True)
    otrosgastostexto = models.CharField(max_length=100, null=True)
    importeselect1 = models.IntegerField(null=True)
    importeselect2 = models.IntegerField(null=True)
    importeselect3 = models.IntegerField(null=True)


class empresa(models.Model):
    numexp = models.IntegerField(null=True)
    avalista = models.BooleanField(default=False)
    nombre = models.CharField(max_length=50, null=True)
    cargo = models.CharField(max_length=50, null=True)
    actividad = models.CharField(max_length=50, null=True)
    ingresos = models.IntegerField(null=True)
    pagas = models.IntegerField(null=True)
    otrosingresos = models.IntegerField(null=True)
    antiguedad = models.CharField(max_length=50, null=True)


class paro(models.Model):
    numexp = models.IntegerField(null=True)
    avalista = models.BooleanField(default=False)
    desdecuando = models.DateField(null=True)
    cobra = models.IntegerField(null=True)


class juvilacion(models.Model):
    numexp = models.IntegerField(null=True)
    avalista = models.BooleanField(default=False)
    importe = models.IntegerField(null=True)
    pagas = models.IntegerField(null=True)
    fechainicio = models.DateField(null=True)
    fechafin = models.DateField(null=True)


class vivienda(models.Model):
    numexp = models.IntegerField(null=True)
    avalista = models.BooleanField(default=False)
    direccion = models.CharField(max_length=50, null=True)
    poblacion = models.CharField(max_length=50, null=True)
    provincia = models.CharField(max_length=50, null=True)
    codigopostal = models.IntegerField(null=True)
    valorvivienda = models.IntegerField(null=True)
    valorhipoteca = models.IntegerField(null=True)
    estapagada = models.BooleanField(default=False)
    sinopagadaanos = models.CharField(max_length=10, null=True)
    sinopagadaentidad = models.CharField(max_length=50, null=True)
    sinopagadapagahipoteca = models.IntegerField(null=True)
    librecargos = models.BooleanField(default=False)
    metros = models.IntegerField(null=True)
    porciento = models.IntegerField(null=True)
    valoralquilada = models.IntegerField(null=True)
    pagaalquiler = models.IntegerField(null=True)


class debecredito(models.Model):
    numexp = models.IntegerField(null=True)
    avalista = models.BooleanField(default=False)
    tipo = models.CharField(max_length=20, choices=CredTip, null=True)
    porcientoavalista = models.IntegerField(null=True)
    importe = models.IntegerField(null=True)
    cuota = models.IntegerField(null=True)
    entidad = models.CharField(max_length=50, null=True)


class debetarjeta(models.Model):
    numexp = models.IntegerField(null=True)
    avalista = models.BooleanField(default=False)
    cuota = models.IntegerField(null=True)
    importe = models.IntegerField(null=True)
    entidad = models.CharField(max_length=50, null=True)


class deberecivos(models.Model):
    numexp = models.IntegerField(null=True)
    avalista = models.BooleanField(default=False)
    importe = models.IntegerField(null=True)


class debemoroso(models.Model):
    numexp = models.IntegerField(null=True)
    avalista = models.BooleanField(default=False)
    importe = models.IntegerField(null=True)
    quien = models.CharField(max_length=50, null=True)


class anotaciones(models.Model):
    numexp = models.IntegerField()
    personales = models.CharField(max_length=500, null=True)
    empresa = models.CharField(max_length=500, null=True)
    vivienda = models.CharField(max_length=500, null=True)
    financieros = models.CharField(max_length=500, null=True)
    avalista = models.CharField(max_length=500, null=True)
    destinado = models.CharField(max_length=500, null=True)
    generales = models.CharField(max_length=500, null=True)

class coches(models.Model):
    numexp = models.IntegerField()
    motor = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    antiguedad = models.DateField()
    matricula = models.CharField(max_length=20)
    estadodelvehiculo = models.CharField(max_length=50)
    coche = models.CharField(max_length=500, null=True)