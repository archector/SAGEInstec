# -*- coding: utf-8 -*-
# Archivo con funciones de control para SAGE
import datetime
import functools
from math import ceil,floor
from decimal import *
CANT_MINUTOS_SIETE_DIAS=10080
CANT_HORAS_SIETE_DIAS = 168
CANT_SEGUNDOS_HORA = 3600
#FECHA_FIJA= datetime.datetime(2015,2,25,0,0).replace(tzinfo=None)
FECHA_FIJA = datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day,0,0) + datetime.timedelta(days=1)





# Las Tuplas de cada puesto deben tener los horarios de inicio y de cierre para que
# pueda funcionar [(7:00,7:00), (19:00,19:00)]


# Suponiendo que cada estacionamiento tiene una estructura "matricial" lista de listas
# donde si m es una matriz, m[i,j] las i corresponden a los puestos y las j corresponden a tuplas
# con el horario inicio y fin de las reservas
# [[(horaIn,horaOut),(horaIn,horaOut)],[],....]

# chequeo de horarios de extended
def HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin, PicoInicio, PicoFin):

	if HoraInicio >= HoraFin:
		return (False, 'El horario de apertura debe ser menor al horario de cierre')
	if ReservaInicio >= ReservaFin:
		return (False, 'El horario de inicio de reserva debe ser menor al horario de cierre')
	if ReservaInicio < HoraInicio:
		return (False, 'El horario de inicio de reserva debe ser mayor o igual al horario de apertura del estacionamiento')
	if ReservaInicio > HoraFin:
		return (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento')
	if ReservaFin < HoraInicio:
		return (False, 'El horario de apertura de estacionamiento debe ser menor al horario de finalización de reservas')
	if ReservaFin > HoraFin:
		return (False, 'El horario de cierre de estacionamiento debe ser mayor o igual al horario de finalización de reservas')
	if PicoInicio and PicoFin:
		if PicoInicio < HoraInicio:
			return (False, 'El horario de inicio del pico debe ser mayor o igual al horario de apertura del estacionamiento')
		elif PicoInicio > HoraFin:
			return (False, 'El horario de inicio del pico debe ser menor o igual al horario de cierre del estacionamiento')
		elif PicoFin > HoraFin:
			return (False, 'El horario de fin del pico debe ser menor o igual al horario de cierre del estacionamiento')
		elif PicoFin < HoraInicio:
			return (False, 'El horario de fin del pico debe ser mayor o igual al horario de apertura del estacionamiento')
		elif PicoFin <= PicoInicio:
			return (False, 'El horario de fin del pico debe ser mayor que el horario de inicio del pico')
			
	return (True, '')


def validarHorarioReserva(ReservaInicio, ReservaFin, HorarioApertura, HorarioCierre):
	
	if (ReservaFin.replace(tzinfo=None)<FECHA_FIJA) or ReservaInicio.replace(tzinfo=None)<FECHA_FIJA:
		return (False, 'La fecha de reserva no puede estar fuera del rango')
	if (ReservaFin.replace(tzinfo=None) < ReservaInicio.replace(tzinfo=None)):
		return (False, 'La fecha Inical de Reserva debe ser menor a la fecha Final de Reserva')
	'''valida si la reserva sobrepasa los 7 dias desde la fecha fija'''
	if (ReservaFin.replace(tzinfo=None)-FECHA_FIJA).total_seconds()/60 > CANT_MINUTOS_SIETE_DIAS:
		return (False, 'La fecha de reserva no puede ser mayor a 7 dias')
	'''Valida si la reserva tiene al menos 1 hora'''
	if (ReservaFin.hour - ReservaInicio.hour < 1) and (ReservaFin.day - ReservaInicio.day == 0):
		return (False, 'El tiempo de reserva debe ser al menos de 1 hora')
	if (ReservaFin.hour*60 + ReservaFin.minute > HorarioCierre.hour*60 +HorarioCierre.minute) and (ReservaFin.day - ReservaInicio.day ==0):
		return (False, 'El horario de fin de reserva debe estar en un horario válido')
	if ReservaInicio.hour*60 + ReservaInicio.minute < HorarioApertura.hour*60 +HorarioApertura.minute and (ReservaFin.day - ReservaInicio.day==0):
		return (False, 'El horario de cierre de reserva debe estar en un horario válido')
	if not(HorarioCierre==datetime.time(0,0)) and not(HorarioCierre==datetime.time(23,59)) and ((ReservaFin.day - ReservaInicio.day >0 ) or (not(ReservaFin.month ==ReservaInicio.month))):
		return (False, 'No puede reservar por mas de un dia, ya que el estacionamiento no trabaja 24 horas')
	
	return (True, '')



'''Algoritmo de Marzullo'''    
def algoritmo_Marzullo(intervalos,horaReserva,capacidad):
	tabla = []
	ini2 = horaReserva[0].replace(tzinfo=None)-FECHA_FIJA
	fin2 = horaReserva[1].replace(tzinfo=None)-FECHA_FIJA
	ini2 =ini2.total_seconds()/60
	fin2 =fin2.total_seconds()/60

	for ini,fin in intervalos:
		ini =ini.replace(tzinfo=None) - FECHA_FIJA
		fin =fin.replace(tzinfo=None) - FECHA_FIJA 
		ini =ini.total_seconds()/60
		fin =fin.total_seconds()/60  
		if (ini < fin2 and fin > ini2):
			tabla.append((ini,-1))
			tabla.append((fin,+1))
		
	def comparar(x, y):
		comp = (x[0]>y[0]) - (x[0]<y[0])
		if comp == 0:
			comp = -((x[1]>y[1]) - (x[1]<y[1])) # regla para el mismo offset y type opuesto
		return comp
	tabla.sort(key = functools.cmp_to_key(comparar))
		
	best,cnt,beststart,bestend= 0,0,0,0
	for i in range(len(tabla) - 1):
		cnt = cnt - tabla[i][1]
		if best < cnt:
			best = cnt
			beststart = tabla[i][0]
			bestend   = tabla[i+1][0]
	#beststart = datetime.time(beststart)
	#bestend = datetime.time(bestend)
	return ( best < capacidad,best)