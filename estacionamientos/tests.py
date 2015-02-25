	# -*- coding: utf-8 -*-

import datetime
from datetime import time, timezone, timedelta
from django.test import Client
from django.test import TestCase
import unittest
from estacionamientos.controller import *
from estacionamientos.forms import *
from estacionamientos.forms import *


###################################################################
#                    ESTACIONAMIENTO VISTA DISPONIBLE
###################################################################
class SimpleTest(unittest.TestCase):
	# normal
	def setUp(self):
		self.client = Client()

	# normal
	def test_primera(self):
		response = self.client.get('/estacionamientos/')
		self.assertEqual(response.status_code, 200)

###################################################################
#                    ALGORITMO MARZULLO
###################################################################
	'''Caso de agregar una reservacion con el estacionamiento vacio'''    
	def testAgregarConEstacionamientoVacio(self):
		n = []
		HoraInicio = time(hour = 6, minute = 0, second = 0)
		HoraFinal = time(hour = 18, minute = 0, second = 0)
		self.assertTrue(algoritmo_Marzullo(n,(HoraInicio,HoraFinal),10)[0])
		
	'''Caso de agregar una reservacion con el estacionamiento lleno'''    
	def testAgregarUnoConEstacionamientoLleno(self):
		n = []
		i=0
		HoraInicio = time(hour = 6, minute = 0, second = 0)
		HoraFinal = time(hour = 18, minute = 0, second = 0)
		while (i <10):
			n.append((HoraInicio,HoraFinal))
			i=i+1   
		self.assertFalse(algoritmo_Marzullo(n,(HoraInicio,HoraFinal),10)[0])
	
	'''Prueba dos intervalos con la misma cantidad de puestos reservados'''
	def testDosIntervalosMismaCantidadDePuestos(self):	
		Hora1 = time(hour = 8, minute = 0, second = 0)
		Hora2 = time(hour = 9, minute = 0, second = 0)
		Hora3 = time(hour = 10, minute = 0, second = 0)
		Hora4 = time(hour = 12, minute = 0, second = 0)
		self.assertTrue(algoritmo_Marzullo(((Hora1,Hora2),(Hora1,Hora4),(Hora3,Hora4)),(Hora3,Hora4),10)[0]) 
		
	'''Caso de llenar el estacionemiento'''    
	def testEstacionemientoLleno(self):
		n = []
		i=0
		HoraInicio = time(hour = 6, minute = 0, second = 0)
		HoraFinal = time(hour = 18, minute = 0, second = 0)
		while (i <9):
			n.append((HoraInicio,HoraFinal))
			i=i+1    
		self.assertTrue(algoritmo_Marzullo(n,(HoraInicio,HoraFinal),10)[0])
		
	'''Caso Horas reservadas Cruzadas'''
	def testHorasCruzadas(self):
		n = []
		i=0
		Hora1 = time(hour = 6, minute = 0, second = 0)
		Hora2 = time(hour = 7, minute = 0, second = 0)
		Hora3 = time(hour = 8, minute = 0, second = 0)
		Hora4 = time(hour = 9, minute = 0, second = 0)
		while (i <9):	
			n.append((Hora1,Hora2))
			i=i+1 
		i=0 
		while (i <9):
			n.append((Hora2,Hora3))
			i=i+1
		i=0
		while (i <9):
			n.append((Hora3,Hora4))
			i=i+1    
		self.assertTrue(algoritmo_Marzullo(n,(Hora1,Hora4),10)[0])
		
	'''Caso en que se reserva el mismo puesto mas de 10 veces a la misma hora'''    
	def testMaximoDeReservasDeUnPuesto(self):
		n = []
		i=0
		HoraInicio = time(hour = 8, minute = 0, second = 0)
		HoraFinal = time(hour = 9, minute = 0, second = 0)
		while (i <10):
			n.append((HoraInicio,HoraFinal))
			i=i+1  
		self.assertFalse(algoritmo_Marzullo(n,(HoraInicio,HoraFinal),10)[0])


	# def testReservaMultiplesDias(self):
	# 	n = []
	# 	i = 0
	# 	HoraInicio = datetime.now()
	# 	HoraFinal = datetime.now() + timedelta(days=1)
	# 	while (i<5):
	# 		n.append((HoraInicio,HoraFinal))
	# 		i=i+1
	# 	self.assertFalse(algoritmo_Marzullo(n,(HoraInicio,HoraFinal),11)[0])

		
	'''Prueba para Offset iguales y tipe opuestos'''
	def testOffsetIgualesTypeOpuestos(self):
		Hora1 = time(hour = 8, minute = 0, second = 0)
		Hora2 = time(hour = 9, minute = 0, second = 0)
		Hora3 = time(hour = 10, minute = 0, second = 0)
		Hora4 = time(hour = 11, minute = 0, second = 0)
		Hora5 = time(hour = 12, minute = 0, second = 0)
		Hora6 = time(hour = 13, minute = 0, second = 0)
		Hora7 = time(hour = 14, minute = 0, second = 0)
		Hora8 = time(hour = 15, minute = 0, second = 0)
		self.assertTrue(algoritmo_Marzullo(((Hora4,Hora8),(Hora1,Hora8),(Hora2,Hora4),(Hora3,Hora7),(Hora4,Hora7),(Hora2,Hora3),(Hora2,Hora6),(Hora5,Hora8),(Hora1,Hora4),(Hora7,Hora8)),(Hora7,Hora8),10)[0])
	
	'''Prueba Simple'''
	def testPruebaSimple(self):
		Hora1 = time(hour = 8, minute = 0, second = 0)
		Hora2 = time(hour = 10, minute = 0, second = 0)
		Hora3 = time(hour = 11, minute = 0, second = 0)
		Hora4 = time(hour = 12, minute = 0, second = 0)
		Hora5 = time(hour = 13, minute = 0, second = 0)
		self.assertTrue(algoritmo_Marzullo(((Hora1,Hora4),(Hora3,Hora5),(Hora2,Hora4)),(Hora2,Hora4),10)[0]) 

###################################################################
#                    ESTACIONAMIENTO_ALL FORM
###################################################################

class SimpleFormTestCase(TestCase):

	# malicia
	def test_CamposVacios(self):
		form_data = {}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_SoloUnCampoNecesario(self):
		form_data = {
			'propietario': 'Pedro'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_DosCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_TresCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_TodosLosCamposNecesarios(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_PropietarioInvalidoDigitos(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_PropietarioInvalidoSimbolos(self):
		form_data = {
			'propietario': 'Pedro!',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_RIFtamanoinvalido(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V1234567'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_RIFformatoinvalido(self):
		form_data = {
			'propietario': 'Pedro132',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'Kaa123456789'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_AgregarTLFs(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_FormatoInvalidoTLF(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02119322878'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_TamanoInvalidoTLF(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '0219322878'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_AgregarCorreos(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878',
			'email_1': 'adminsitrador@admin.com',
			'email_2': 'usua_rio@users.com'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_CorreoInvalido(self):
		form_data = {
			'propietario': 'Pedro',
			'nombre': 'Orinoco',
			'direccion': 'Caracas',
			'rif': 'V123456789',
			'telefono_1': '02129322878',
			'telefono_2': '04149322878',
			'telefono_3': '04129322878',
			'email_1': 'adminsitrador@a@dmin.com'
		}
		form = EstacionamientoForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

###################################################################
# ESTACIONAMIENTO_EXTENDED_FORM
###################################################################

	# malicia
	def test_EstacionamientoExtendedForm_UnCampo(self):
		form_data = { 'puestos': 2}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_DosCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': time(6, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_TresCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': time(6, 0),
								'horarioout': time(19, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_CuatroCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': time(6, 0),
								'horarioout': time(19, 0),
								'horario_reserin': time(7, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_EstacionamientoExtendedForm_CincoCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': time(6, 0),
								'horarioout': time(19, 0),
								'horario_reserin': time(7, 0),
								'horario_reserout': time(14, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	#############################ACTUALIZADO#####################################
	def test_EstacionamientoExtendedForm_TodosCamposBien(self):
		tarifa = Tarifa(
					tipoTarifa = 'wuu')
		tarifa.save()
		form_data = { 'puestos': 2,
								'horarioin': time(6, 0),
								'horarioout': time(19, 0),
								'horario_reserin': time(7, 0),
								'horario_reserout': time(14, 0),
								'tarifa' : tarifa,
								'monto_tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# caso borde
	#############################ACTUALIZADO#####################################
	def test_EstacionamientoExtendedForm_Puestos0(self):
		tarifa = Tarifa(
					tipoTarifa = 'wuu')
		tarifa.save()
		form_data = { 'puestos': 0,
								'horarioin': time(6, 0),
								'horarioout': time(19, 0),
								'horario_reserin': time(7, 0),
								'horario_reserout': time(14, 0),
								'tarifa' : tarifa,
								'monto_tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# caso borde
	#############################ACTUALIZADO#####################################
	def test_EstacionamientoExtendedForm_HoraInicioIgualHoraCierre(self):
		tarifa = Tarifa(
					tipoTarifa = 'wuu')
		tarifa.save()
		form_data = { 'puestos': 2,
								'horarioin': time(6, 0),
								'horarioout': time(6, 0),
								'horario_reserin': time(7, 0),
								'horario_reserout': time(14, 0),
								'tarifa' : tarifa,
								'monto_tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# caso borde
	#############################ACTUALIZADO#####################################
	def test_EstacionamientoExtendedForm_HoraIniReserIgualHoraFinReser(self):
		tarifa = Tarifa(
						tipoTarifa = 'wuu')
		tarifa.save()
		form_data = { 'puestos': 2,
								'horarioin': time(6, 0),
								'horarioout': time(19, 0),
								'horario_reserin': time(7, 0),
								'horario_reserout': time(7, 0),
								'tarifa' : tarifa,
								'monto_tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		#tarifa.delete()
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_EstacionamientoExtendedForm_StringEnPuesto(self):
		tarifa = Tarifa(
						tipoTarifa = 'wuu')
		tarifa.save()
		form_data = { 'puestos': 'hola',
								'horarioin': time(6, 0),
								'horarioout': time(19, 0),
								'horario_reserin': time(7, 0),
								'horario_reserout': time(14, 0),
								'tarifa' : tarifa,
								'monto_tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_StringHoraInicio(self):
		form_data = { 'puestos': 2,
								'horarioin': 'holaa',
								'horarioout': time(19, 0),
								'horario_reserin': time(7, 0),
								'horario_reserout': time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NumeroNegativoHoraInicio(self):
		form_data = { 'puestos': 2,
								'horarioin':-1,
								'horarioout': time(19, 0),
								'horario_reserin': time(7, 0),
								'horario_reserout': time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NoneEntarifa(self):
		form_data = { 'puestos': 2,
								'horarioin': time(6, 0),
								'horarioout': time(19, 0),
								'horario_reserin': time(7, 0),
								'horario_reserout': time(14, 0),
								'tarifa': None}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NoneEnHorarioReserva(self):
		form_data = { 'puestos': 2,
								'horarioin': 'holaa',
								'horarioout': time(19, 0),
								'horario_reserin': None,
								'horario_reserout': time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_listaEnHoraReserva(self):
		form_data = { 'puestos': 2,
								'horarioin': time(6, 0),
								'horarioout': time(19, 0),
								'horario_reserin': time(7, 0),
								'horario_reserout': [time(14, 0)],
								'tarifa': 12}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

######################################################################
# ESTACIONAMIENTO_EXTENDED pruebas controlador
###################################################################

	# normal
	def test_HorariosValidos(self):
		HoraInicio = time(hour = 12, minute = 0, second = 0)
		HoraFin = time(hour = 18, minute = 0, second = 0)
		ReservaInicio = time(hour = 12, minute = 0, second = 0)
		ReservaFin = time(hour = 18, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# malicia
	def test_HorariosInvalido_HoraCierre_Menor_HoraApertura(self):
		HoraInicio = time(hour = 12, minute = 0, second = 0)
		HoraFin = time(hour = 11, minute = 0, second = 0)
		ReservaInicio = time(hour = 12, minute = 0, second = 0)
		ReservaFin = time(hour = 18, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierre_Igual_HoraApertura(self):
		HoraInicio = time(hour = 12, minute = 0, second = 0)
		HoraFin = time(hour = 12, minute = 0, second = 0)
		ReservaInicio = time(hour = 12, minute = 0, second = 0)
		ReservaFin = time(hour = 18, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierreReserva_Menor_HoraAperturaReserva(self):
		HoraInicio = time(hour = 12, minute = 0, second = 0)
		HoraFin = time(hour = 18, minute = 0, second = 0)
		ReservaInicio = time(hour = 12, minute = 0, second = 0)
		ReservaFin = time(hour = 11, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierreReserva_Igual_HoraAperturaReserva(self):
		HoraInicio = time(hour = 12, minute = 0, second = 0)
		HoraFin = time(hour = 18, minute = 0, second = 0)
		ReservaInicio = time(hour = 12, minute = 0, second = 0)
		ReservaFin = time(hour = 12, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

	# caso borde
	def test_Limite_HorarioValido_Apertura_Cierre(self):
		HoraInicio = time(hour = 12, minute = 0, second = 0)
		HoraFin = time(hour = 12, minute = 0, second = 1)
		ReservaInicio = time(hour = 12, minute = 0, second = 0)
		ReservaFin = time(hour = 12, minute = 0, second = 1)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_Limite_Superior_HorarioValido_Apertura_Cierre(self):
		HoraInicio = time(hour = 0, minute = 0, second = 0)
		HoraFin = time(hour = 23, minute = 59, second = 59)
		ReservaInicio = time(hour = 12, minute = 0, second = 0)
		ReservaFin = time(hour = 23, minute = 59, second = 59)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_InicioReserva_Mayor_HoraCierreEstacionamiento(self):
		HoraInicio = time(hour = 12, minute = 0, second = 0)
		HoraFin = time(hour = 18, minute = 0, second = 0)
		ReservaInicio = time(hour = 19, minute = 0, second = 0)
		ReservaFin = time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

	# caso borde
	def test_InicioReserva_Mayor_HoraCierreEstacionamiento2(self):
		HoraInicio = time(hour = 12, minute = 0, second = 0)
		HoraFin = time(hour = 18, minute = 0, second = 0)
		ReservaInicio = time(hour = 19, minute = 0, second = 0)
		ReservaFin = time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

	# malicia
	def test_CierreReserva_Mayor_HoraCierreEstacionamiento(self):
		HoraInicio = time(hour = 12, minute = 0, second = 0)
		HoraFin = time(hour = 18, minute = 0, second = 0)
		ReservaInicio = time(hour = 17, minute = 0, second = 0)
		ReservaFin = time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de cierre de estacionamiento debe ser mayor o igual al horario de finalización de reservas'))

	# malicia
	def test_CierreReserva_Menos_HoraInicioEstacionamiento(self):
		HoraInicio = time(hour = 12, minute = 0, second = 0)
		HoraFin = time(hour = 18, minute = 0, second = 0)
		ReservaInicio = time(hour = 10, minute = 0, second = 0)
		ReservaFin = time(hour = 11, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe mayor o igual al horario de apertura del estacionamiento'))



###################################################################
# ESTACIONAMIENTO_RESERVA_FORM
###################################################################

	# malicia
	def test_EstacionamientoReserva_Vacio(self):
		form_data = {}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_EstacionamientoReserva_UnCampo(self):
		form_data = {'inicio':time(6, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# normal
	def test_EstacionamientoReserva_TodosCamposBien(self):
		ini = datetime.now()
		fin = ini + timedelta(days=+1)
		form_data = {'inicio':ini, 'final':fin}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_EstacionamientoReserva_InicioString(self):
		form_data = {'inicio':'hola',
								'final':time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_FinString(self):
		form_data = {'inicio':time(6, 0),
								'final':'hola'}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_InicioNone(self):
		form_data = {'inicio':None,
								'final':time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_finalNone(self):
		form_data = {'inicio':time(6, 0),
								'final':None}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)
		
###################################################################
# ESTACIONAMIENTO_PAGOS_FORM
###################################################################
	
	#malicia
	def test_Form_Campos_Vacios(self):
		form_data = {}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
		
	#borde
	def test_Form_Nombre_Vacio(self):
		form_data = {'apellido':"zeait",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#borde	
	def test_Form_Apellido_Vacio(self):
		form_data = {'nombre':"daniel",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#borde
	def test_Form_Cedula_Vacio(self):
		form_data = {'nombre':"Daniel",
					'apellido':"Zeait",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#borde	
	def test_Form_NumTarjeta_Vacio(self):
		form_data = {'nombre':"Daniel",
					'apellido':"Zeait",
					'cedula':"19294080",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#borde	
	def test_Form_CVV_Vacio(self):
		form_data = {'nombre':"Daniel",
					'apellido':"Zeait",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD	
	def test_Form_DosCampos_Vacios_12(self):
		form_data = {'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD	
	def test_Form_DosCampos_Vacios_13(self):
		form_data = {'apellido':"Zeait",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD	
	def test_Form_DosCampos_Vacios_14(self):
		form_data = {'apellido':"Zeait",
					'cedula':"19294080",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD		
	def test_Form_DosCampos_Vacios_15(self):
		form_data = {'apellido':"Zeait",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
			
	#TDD
	def test_Form_DosCampos_Vacios_23(self):
		form_data = {'nombre':"Daniel",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD
	def test_Form_DosCampos_Vacios_24(self):
		form_data = {'nombre':"Daniel",
					'cedula':"19294080",
					'codigo_val':"123"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD
	def test_Form_DosCampos_Vacios_25(self):
		form_data = {'nombre':"Daniel",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD
	def test_Form_DosCampos_Vacios_34(self):
		form_data = {'nombre':"Daniel",
					'apellido':"Zeait",
					'codigo_val':"123"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD	
	def test_Form_DosCampos_Vacios_35(self):
		form_data = {'nombre':"Daniel",
					'apellido':"Zeait",
					'num_tarjeta':"1234567890123456"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD	
	def test_Form_DosCampos_Vacios_45(self):
		form_data = {'nombre':"Daniel",
					'apellido':"Zeait",
					'cedula':"19294080",
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD	
	def test_Form_TresCampos_Vacios_123(self):
		form_data = {'num_tarjeta':"1234567890123456",
					'codigo_val':"123"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD	
	def test_Form_TresCampos_Vacios_124(self):
		form_data = {
					'cedula':"19294080",
					'codigo_val':"123"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD	
	def test_Form_DosCampos_Vacios_125(self):
		form_data = {
					'num_tarjeta':"1234567890123456",
					'cedula':"19294080",
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
		
	#TDD
	def test_Form_TresCampos_Vacios_234(self):
		form_data = {'nombre':"Daniel",
					'codigo_val':"123"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD	
	def test_Form_TresCampos_Vacios_235(self):
		form_data = {'nombre':"Daniel",
					'num_tarjeta':"1234567890123456"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD	
	def test_Form_TresCampos_Vacios_345(self):
		form_data = {
					'nombre':"Daniel",
					'apellido':"Zeait",
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)

	#TDD
	def test_Form_CuatroCampos_Vacios_1234(self):
		form_data = {
					'codigo_val':"123"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)

	#TDD
	def test_Form_CuatroCampos_Vacios_1235(self):
		form_data = {
					'num_tarjeta':"1234567890123456"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD
	def test_Form_CuatroCampos_Vacios_2345(self):
		form_data = {
					'nombre':"Daniel"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD
	def test_Form_CuatroCampos_Vacios_1345(self):
		form_data = {
					'apellido':"Zeait"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD
	def test_Form_CuatroCampos_Vacios_1245(self):
		form_data = {
					'cedula':"19294080"
					}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
		
	#Malicia	
	def test_Form_Campos_Todos_Invalidos(self):
		form_data = {'nombre':"Daniel1234",
					'apellido':"Zeait1234",
					'cedula':'fghkjhu',
					'num_tarjeta':"wertyui",
					'codigo_val':'ertyui'}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#borde
	def test_Form_Nombre_Invalido(self):
		form_data = {'nombre':"Daniel1234",
					'apellido':"Zeait",
					'cedula':'19294080',
					'num_tarjeta':"1234567890123456",
					'codigo_val':'123'}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#borde
	def test_Form_Apellido_Invalido(self):
		form_data = {'nombre':"Daniel",
					'apellido':"Zeait123",
					'cedula':'19294080',
					'num_tarjeta':"1234567890123456",
					'codigo_val':'123'}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#borde
	def test_Form_Cedula_Invalida(self):
		form_data = {'nombre':"Daniel",
					'apellido':"Zeait",
					'cedula':'19294080a',
					'num_tarjeta':"1234567890123456",
					'codigo_val':'123'}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#borde
	def test_Form_NumTarjeta_Invalida(self):
		form_data = {'nombre':"daniel",
					'apellido':"zeait",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456q",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#borde
	def test_Form_Cvv_Invalido(self):
		form_data = {'nombre':"daniel",
					'apellido':"zeait",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"1x3a"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#TDD
	def test_Form_DosNombres(self):
		form_data = {'nombre':"Daniel Elias",
					'apellido':"zeait",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)
	
	#TDD	
	def test_Form_DosApellidos(self):
		form_data = {'nombre':"Daniel",
					'apellido':"Pelayo Useche",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)

	#TDD	
	def test_Form_DosNombres_DosApellidos(self):
		form_data = {'nombre':"Daniel Alejandro",
					'apellido':"Pelayo Useche",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)

	#borde	
	def test_Form_NombresEspeciales_Acentos(self):
		form_data = {'nombre':"José",
					'apellido':"Alvarado",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)

	#borde	
	def test_Form_NombresEspeciales_Eñe(self):
		form_data = {'nombre':"Iñaqui",
					'apellido':"Alvarado",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)
		
	
	#TDD	
	def test_Form_DosNombresEspeciales_Acentos(self):
		form_data = {'nombre':"Martín José",
					'apellido':"Alvarado",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)
			
	#malicia	
	def test_Form_Nombres_Muy_Especiales(self):
		form_data = {'nombre':"María José del Carmen ",
					'apellido':"Alvarado",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)
		
	#malicia	
	def test_Form_Apellidos_Especiales1(self):
		form_data = {'nombre':" Daniel",
					'apellido':"Álvarez",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)
	
	#malicia	
	def test_Form_Apellidos_Especiales2(self):
		form_data = {'nombre':" Daniel",
					'apellido':"Nuñez",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)
	
	#malicia	
	def test_Form_Apellidos_Especiales3(self):
		form_data = {'nombre':" Daniel",
					'apellido':"Álvarez Nuñez",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)
	
	def test_Form_Apellidos_Especiales4(self):
		form_data = {'nombre':" Daniel",
					'apellido':"Álvarez De Jesús",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)
		
	def test_Form_NombresApellidos_Especiales(self):
		form_data = {'nombre':" Iñaqui José",
					'apellido':"Álvarez De Jesús",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)
		
	def test_Form_NombresApellidos_Especiales2(self):
		form_data = {'nombre':" Iñaqui Thomás José",
					'apellido':"Zúñiga Römer",
					'cedula':"19294080",
					'num_tarjeta':"1234567890123456",
					'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), True)
			
###################################################################
# PRUEBAS DE FUNCIONES DEL CONTROLADOR
###################################################################

##############################################################
# Estacionamiento Reserva Controlador
###################################################################

# HorarioReserva, pruebas Unitarias

	# normal
	def test_HorarioReservaValido(self):
		ReservaInicio = datetime(year = 2015, month = 2, day = 23, hour = 13, minute = 0, second = 0, tzinfo = timezone.utc)
		ReservaFin = datetime(year = 2015, month = 2, day = 23,hour = 15, minute = 0, second = 0, tzinfo = timezone.utc)
		HoraApertura = time(hour = 12, minute = 0, second = 0)
		HoraCierre = time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_HorarioReservaInvalido_InicioReservacion_Mayor_FinalReservacion(self):
		ReservaInicio = datetime(year = 2015, month = 2, day = 23, hour = 13, minute = 0, second = 0, tzinfo = timezone.utc)
		ReservaFin = datetime(year = 2015, month = 2, day = 23,hour = 12, minute = 59, second = 59, tzinfo = timezone.utc)
		HoraApertura = time(hour = 12, minute = 0, second = 0)
		HoraCierre = time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorarioReservaInvalido_TiempoTotalMenor1h(self):
		ReservaInicio = datetime(year = 2015, month = 2, day = 23, hour = 13, minute = 0, second = 0, tzinfo = timezone.utc)
		ReservaFin = datetime(year = 2015, month = 2, day = 23,hour = 13, minute = 59, second = 59, tzinfo = timezone.utc)
		HoraApertura = time(hour = 12, minute = 0, second = 0)
		HoraCierre = time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El tiempo de reserva debe ser al menos de 1 hora'))

	# caso borde
	#############################ACTUALIZADO#####################################
	def test_HorarioReservaInvalido_ReservaFinal_Mayor_HorarioCierre(self):
		ReservaInicio = datetime(year = 2015, month = 2, day = 23, hour = 13, minute = 0, second = 0, tzinfo = timezone.utc)
		ReservaFin = datetime(year = 2015, month = 2, day = 23,hour = 18, minute = 0, second = 1, tzinfo = timezone.utc)
		HoraApertura = time(hour = 12, minute = 0, second = 0)
		HoraCierre = time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El horario de fin de reserva debe estar en un horario válido'))

	# caso borde
	def test_HorarioReservaInvalido_ReservaInicial_Menor_HorarioApertura(self):
		ReservaInicio = datetime(year = 2015, month = 2, day = 23, hour = 11, minute = 59, second = 59, tzinfo = timezone.utc)
		ReservaFin = datetime(year = 2015, month = 2, day = 23,hour = 15, minute = 0, second = 1, tzinfo = timezone.utc)
		HoraApertura = time(hour = 12, minute = 0, second = 0)
		HoraCierre = time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El horario de cierre de reserva debe estar en un horario válido'))

	# malicia
	def test_Reservacion_CamposVacios(self):
		ini = datetime.now()
		fin = ini + timedelta(days=+1)
		form_data = {'inicio':ini, 'final':fin}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), True)
