from __future__ import unicode_literals

from django.db import models


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
    tipo = models.CharField(max_length=10)
    fecha_hora = models.DateTimeField()


class persona(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.IntegerField()
    movil = models.IntegerField()
    fechanacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    estadocivil = models.CharField(max_length=20, choices=EstatsCivils)
    tipocasado = models.CharField(max_length=20, choices=TipoCasado)
    numerodehijos = models.IntegerField()
    sihijosmayores18 = models.BooleanField()
    sihijoscuantoscargo = models.IntegerField()
    sihijosingreso = models.IntegerField()
    justificante = models.BooleanField()
    autoriza = models.BooleanField()
    medio = models.CharField(max_length=20, choices=Medios)
    tieneavalista = models.BooleanField(null=True)
    metodopago = models.CharField(max_length=200, choices=RecibirMoney)


class personaanexos(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    seguridadsocial = models.CharField(max_length=20, choices=Cotiza)
    siajenatipo = models.CharField(max_length=20, choices=TipWork)
    siajenatemporal = models.DateField()
    otrosingresos = models.IntegerField()
    otrosingresostexto = models.CharField(max_length=100)
    otrosgastos = models.IntegerField()
    otrosgastostexto = models.CharField(max_length=100)


class empresa(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    actividad = models.CharField(max_length=50)
    ingresos = models.IntegerField()
    pagas = models.IntegerField()
    otrosingresos = models.IntegerField()
    antiguedad = models.CharField(max_length=50)


class paro(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    desdecuando = models.DateField()
    cobra = models.IntegerField()


class juvilacion(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    importe = models.IntegerField()
    pagas = models.IntegerField()
    fechainicio = models.DateField()
    fechafin = models.DateField()


class vivienda(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    direccion = models.CharField(max_length=50)
    poblacion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    codigopostal = models.IntegerField()
    valorvivienda = models.IntegerField(null=True)
    valorhipoteca = models.IntegerField(null=True)
    estapagada = models.BooleanField(null=True)
    sinopagadaanos = models.CharField(max_length=10, null=True)
    sinopagadaentidad = models.CharField(max_length=50, null=True)
    sinopagadapagahipoteca = models.IntegerField(null=True)
    librecargos = models.BooleanField(null=True)
    metros = models.IntegerField(null=True)
    porciento = models.IntegerField(null=True)
    valoralquilada = models.IntegerField(null=True)
    pagaalquiler = models.IntegerField(null=True)


class debecredito(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    tipo = models.CharField(max_length=20, choices=CredTip)
    porcientoavalista = models.IntegerField()
    importe = models.IntegerField()
    cuota = models.IntegerField()
    entidad = models.CharField(max_length=50)


class debetarjeta(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    cuota = models.IntegerField()
    importe = models.IntegerField()
    entidad = models.CharField(max_length=50)


class deberecivos(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    importe = models.IntegerField()


class debemoroso(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    importe = models.IntegerField()
    quien = models.CharField(max_length=50)


class anotaciones(models.Model):
    numexp = models.IntegerField()
    personales = models.CharField(max_length=500)
    empresa = models.CharField(max_length=500)
    vivienda = models.CharField(max_length=500)
    financieros = models.CharField(max_length=500)
    avalista = models.CharField(max_length=500, null=True)
    destinado = models.CharField(max_length=500)


class coches(models.Model):
    numexp = models.IntegerField()
    motor = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    antiguedad = models.DateField()
    matricula = models.CharField(max_length=20)
    estadodelvehiculo = models.CharField(max_length=50)
    coche = models.CharField(max_length=500)