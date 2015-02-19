# Archivo con funciones de control para SAGE
import datetime
from datetime import datetime,timezone
import functools
from math import ceil
from decimal import *

# Las Tuplas de cada puesto deben tener los horarios de inicio y de cierre para que
# pueda funcionar [(7:00,7:00), (19:00,19:00)]


# Suponiendo que cada estacionamiento tiene una estructura "matricial" lista de listas
# donde si m es una matriz, m[i,j] las i corresponden a los puestos y las j corresponden a tuplas
# con el horario inicio y fin de las reservas
# [[(horaIn,horaOut),(horaIn,horaOut)],[],....]

# chequeo de horarios de extended
def HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin):

	if HoraInicio >= HoraFin:
		return (False, 'El horario de apertura debe ser menor al horario de cierre')
	if ReservaInicio >= ReservaFin:
		return (False, 'El horario de inicio de reserva debe ser menor al horario de cierre')
	if ReservaInicio < HoraInicio:
		return (False, 'El horario de inicio de reserva debe mayor o igual al horario de apertura del estacionamiento')
	if ReservaInicio > HoraFin:
		return (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento')
	if ReservaFin < HoraInicio:
		return (False, 'El horario de apertura de estacionamiento debe ser menor al horario de finalización de reservas')
	if ReservaFin > HoraFin:
		return (False, 'El horario de cierre de estacionamiento debe ser mayor o igual al horario de finalización de reservas')
	return (True, '')


def validarHorarioReserva(ReservaInicio, ReservaFin, HorarioApertura, HorarioCierre):
	
	horaActual = datetime.now(timezone.utc)
	intervaloIni =(ReservaInicio - horaActual).total_seconds()/3600
	intervaloFin =(ReservaFin - horaActual).total_seconds()/3600
	if intervaloIni > 168:
		return (False, 'La fecha para iniciar la reserva debe ser menor a 7 dias')
	if intervaloFin > 168:
		return (False, 'La fecha para culminar la reserva debe ser menor a 7 dias')
	if ReservaInicio >= ReservaFin:
		return (False, 'El horario de apertura debe ser menor al horario de cierre')
	if ReservaFin.hour - ReservaInicio.hour < 1:
		return (False, 'El tiempo de reserva debe ser al menos de 1 hora')
	if ReservaFin.time() > HorarioCierre:
		return (False, 'El horario de fin de reserva debe estar en un horario válido')
	if ReservaInicio.time() < HorarioApertura:
		return (False, 'El horario de cierre de reserva debe estar en un horario válido')
	return (True, '')


def esquemaTarifarioHoras(hin,hout,tarifa):
	horain = hin.hour + hin.minute/60
	horaout = hout.hour + hout.minute/60
	horas_a_pagar= horaout - horain
	horas_a_pagar = ceil(horas_a_pagar)
	cobro = 0
	while horas_a_pagar> 0:
		cobro = cobro + tarifa
		horas_a_pagar = horas_a_pagar - 1
	cobro=("{:.2f}".format(cobro))
	cobro = Decimal(cobro)
	return cobro


def esquemaTarifarioMinutos(hin,hout,tarifa):
	horain = hin.hour*60 + hin.minute
	horaout = hout.hour*60 + hout.minute
	horas_a_pagar= horaout - horain
	cobro = 0
	while horas_a_pagar> 0:
		cobro = cobro + tarifa/60
		horas_a_pagar = horas_a_pagar - 1
	cobro=("{:.2f}".format(cobro))
	cobro = Decimal(cobro)
	return cobro


'''Algoritmo de Marzullo'''    
def algoritmo_Marzullo(intervalos,horaReserva,capacidad):
	tabla = []
	ini2 =horaReserva[0].hour
	fin2 =horaReserva[1].hour

	for ini,fin in intervalos:
		ini =ini.hour
		fin =fin.hour 
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
