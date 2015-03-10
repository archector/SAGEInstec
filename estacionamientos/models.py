# -*- coding: utf-8 -*-

from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm
from decimal import Decimal

class Tarifa(models.Model):
	tipoTarifa = models.CharField(max_length = 50, blank = True,primary_key=True)
	def __str__(self):			  # __unicode__ on Python 2
		return self.tipoTarifa

class Estacionamiento(models.Model):
	# propietario=models.ForeignKey(Propietario)
	Propietario = models.CharField(max_length = 50, help_text = "Nombre Propio")
	Nombre = models.CharField(max_length = 50)
	Direccion = models.TextField(max_length = 120)

	Telefono_1 = models.CharField(blank = True, null = True, max_length = 30)
	Telefono_2 = models.CharField(blank = True, null = True, max_length = 30)
	Telefono_3 = models.CharField(blank = True, null = True, max_length = 30)

	Email_1 = models.EmailField(blank = True, null = True)
	Email_2 = models.EmailField(blank = True, null = True)

	Rif = models.CharField(max_length = 12)

	Tarifa = models.ForeignKey(Tarifa, default = None, blank = True, null = True)
	monto_tarifa = models.DecimalField(max_digits = 20, decimal_places=2,blank = True, null = True)
	Apertura = models.TimeField(blank = True, null = True)
	Cierre = models.TimeField(blank = True, null = True)
	Reservas_Inicio = models.TimeField(blank = True, null = True)
	Reservas_Cierre = models.TimeField(blank = True, null = True)
	NroPuesto = models.IntegerField(blank = True, null = True)
	Ingresos = models.DecimalField(max_digits=10, decimal_places=2,default = None, blank=True, null=True)
	
	
	def __str__(self):			  # __unicode__ on Python 2
		return self.Nombre


class ReservasModel(models.Model):
	
	Estacionamiento = models.ForeignKey(Estacionamiento)
	Puesto = models.IntegerField()
	InicioReserva = models.DateTimeField(default = None)
	FinalReserva = models.DateTimeField(default = None)
	Costo = models.DecimalField(max_digits= 20,decimal_places=2, default = None, blank=True, null=True)
	
	def __str__(self):			  # __unicode__ on Python 2
		return str(self.id) 
	
	
class RecibosModel(models.Model):
	
	NumeroTransaccion = models.CharField(max_length = 20, default = None, blank=True, null=True)
	Nombre = models.CharField(max_length = 20, default = None, blank=True, null=True)
	Apellido = models.CharField(max_length = 20, default = None, blank=True, null=True)
	Cedula = models.CharField(max_length = 20, default = None, blank=True, null=True)
	NumeroTarjeta = models.CharField(max_length = 16, default = None, blank=True, null=True)
	FechaPago =models.DateTimeField(default = None)
	InicioReserva = models.DateTimeField(default = None)
	FinalReserva = models.DateTimeField(default = None)
	Costo = models.DecimalField(max_digits=10, decimal_places=2,default = None, blank=True, null=True)
	RifEstacionamiento=models.CharField(max_length = 20, default = None, blank=True, null=True)
	NombreEstacionamiento=models.CharField(max_length = 20, default = None, blank=True, null=True)
	TelEstacionamiento=models.CharField(max_length = 30, default = None, blank=True, null=True)

	def __str__(self):			  # __unicode__ on Python 2
		return self.NumeroTransaccion
