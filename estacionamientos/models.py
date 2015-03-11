# -*- coding: utf-8 -*-

from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm
from decimal import Decimal
from math import ceil, floor
from datetime import datetime, timedelta, time

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
	Pico_Inicio = models.TimeField(blank = True, null = True)
	Pico_Final = models.TimeField(blank = True, null = True)
	monto_tarifa_pico = models.DecimalField(max_digits = 20, decimal_places=2,blank = True, null = True, default = 0)
	NroPuesto = models.IntegerField(blank = True, null = True)
	Ingresos = models.DecimalField(max_digits=10, decimal_places=2,default = None, blank=True, null=True)
	
	
	def __str__(self):			  # __unicode__ on Python 2
		return self.Nombre
	
	def calcularCobro(self,hin,hout):
		if self.Tarifa.tipoTarifa == 'minutos':
			return self.esquemaTarifarioMinutos(hin,hout)
		elif self.Tarifa.tipoTarifa == 'horas':
			return self.esquemaTarifarioHoras(hin, hout)
		elif self.Tarifa.tipoTarifa == 'horaFraccion':
			return self.esquemaTarifarioHoraFraccion(hin, hout)
		elif self.Tarifa.tipoTarifa == 'difHoras':
			return self.esquemaTarifarioPagoDiferenciadoHora(hin, hout)


	def esquemaTarifarioHoras(self,hin,hout):
		#horain = hin.hour + hin.minute/60
		#horaout = hout.hour + hout.minute/60
		#horas_a_pagar = horaout - horain
		horas_a_pagar= (hout - hin).total_seconds()/3600
		horas_a_pagar = ceil(horas_a_pagar)
		cobro = 0
		while horas_a_pagar> 0:
			cobro = cobro + self.monto_tarifa
			horas_a_pagar = horas_a_pagar - 1
		return cobro
	
	
	def esquemaTarifarioMinutos(self,hin,hout):
		horas_a_pagar = hout - hin
		print(horas_a_pagar)
		print((horas_a_pagar).days*24)
		horas_a_pagar = (horas_a_pagar).days*24 + (horas_a_pagar.seconds/3600)
		minutos_a_pagar = horas_a_pagar*60
		cobro = 0
		print (minutos_a_pagar)
		while minutos_a_pagar> 0:
			cobro = cobro + self.monto_tarifa/60
			minutos_a_pagar = minutos_a_pagar - 1
		cobro=("{:.2f}".format(cobro))
		cobro = Decimal(cobro)
		return cobro
	
	def esquemaTarifarioHoraFraccion(self, hin,hout):
		horas_a_pagar = hout - hin
		horas_a_pagar = (horas_a_pagar).days*24 + horas_a_pagar.seconds/3600
		horas_a_pagar = floor(horas_a_pagar)
		#horas_a_pagar = horas_a_pagar.days*24 + (horas_a_pagar.seconds)/3600
		if (hin.minute - hout.minute) == 0:
			fraccion =0
		elif (hin.minute < hout.minute):
			fraccion = hout.minute - hin.minute
		elif hin.minute > hout.minute:
			fraccion = 60 - (hin.minute - hout.minute)
			
		cobro = 0
		while horas_a_pagar > 0:
			cobro = cobro + self.monto_tarifa
			horas_a_pagar = horas_a_pagar - 1
		if 0<fraccion <= 30:
			cobro = cobro + self.monto_tarifa/2
		if 30<fraccion<=59:
			cobro = cobro + self.monto_tarifa
		
		cobro=("{:.2f}".format(cobro))
		cobro = Decimal(cobro)	
		return cobro
	
	def esquemaTarifarioPagoDiferenciadoHora(self,hin,hout):
		horas_a_pagar = hout - hin
		horas_a_pagar = (horas_a_pagar).days*24 + horas_a_pagar.seconds/3600
		minutos_a_pagar = horas_a_pagar*60
		minutos_a_pagar = floor(minutos_a_pagar)
		cobro = 0
		cobroPico = 0
		hora_aux = hin
		while minutos_a_pagar> 0:
			if ((hora_aux.time() >= self.Pico_Inicio) and (hora_aux.time() < self.Pico_Final)):
				cobroPico = cobroPico + self.monto_tarifa_pico/60
				minutos_a_pagar = minutos_a_pagar - 1
				hora_aux = hora_aux + timedelta(0,60)
			else:
				cobro = cobro + self.monto_tarifa/60
				minutos_a_pagar = minutos_a_pagar - 1
				hora_aux = hora_aux + timedelta(0,60)
		cobro = cobro + cobroPico
		cobro=("{:.2f}".format(cobro))
		cobro = Decimal(cobro)
		return cobro


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
