from __future__ import unicode_literals

from django.db import models


class expediente(models.Model):
    numexp = models.IntegerField()
    tipo = models.CharField(max_length=10)
    fecha = models.DateField()
    hora = models.DateTimeField()


class persona(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.IntegerField()
    movil = models.IntegerField()
    fechanacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    estadocivil = models.CharField(max_length=20)
    tipocasado = models.CharField(max_length=20)
    numerodehijos = models.IntegerField()
    sihijosmayores18 = models.BooleanField()
    sihijosingreso = models.IntegerField()
    justificante = models.BooleanField()
    autoriza = models.BooleanField()
    medio = models.CharField(max_length=20)
    tieneavalista = models.BooleanField()


class personaanexos(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    tipo = models.CharField(max_length=20)
    seguridadsocial = models.CharField(max_length=20)
    siajenatipo = models.CharField(max_length=20)
    siajenatemporal = models.DateField()
    otrosingresos = models.IntegerField()
    otrosingresostexto = models.CharField(max_length=100)
    otrosgastos = models.IntegerField()
    otrosgastostexto = models.CharField(max_length=100)
    tipovivienda = models.CharField(max_length=50)


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
    tipo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    poblacion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    codigopostal = models.IntegerField()
    valorvivienda = models.IntegerField()
    valorhipoteca = models.IntegerField()
    estapagada = models.BooleanField()
    sinopagadaanos = models.CharField(max_length=10)
    sinopagadaentidad = models.CharField(max_length=50)
    sinopagadalibrecargos = models.BooleanField()
    metros = models.IntegerField()
    porciento = models.IntegerField()
    valoralquilada = models.IntegerField()
    pagaalquiler = models.IntegerField()


class debecredito(models.Model):
    numexp = models.IntegerField()
    avalista = models.BooleanField(default=False)
    tipo = models.CharField(max_length=20)
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
    avalista = models.CharField(max_length=500)
    destinado = models.CharField(max_length=500)


class coches(models.Model):
    numexp = models.IntegerField()
    motor = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    antiguedad = models.DateField()
    matricula = models.CharField(max_length=20)
    estadodelvehiculo = models.CharField(max_length=50)
