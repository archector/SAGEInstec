# -*- coding: utf-8 -*-

import datetime
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
		HoraInicio = datetime.time(hour = 6, minute = 0, second = 0)
		HoraFinal = datetime.time(hour = 18, minute = 0, second = 0)
		self.assertTrue(algoritmo_Marzullo(n,(HoraInicio,HoraFinal),10)[0])
		
	'''Caso de agregar una reservacion con el estacionamiento lleno'''    
	def testAgregarUnoConEstacionamientoLleno(self):
		n = []
		i=0
		HoraInicio = datetime.time(hour = 6, minute = 0, second = 0)
		HoraFinal = datetime.time(hour = 18, minute = 0, second = 0)
		while (i <10):
			n.append((HoraInicio,HoraFinal))
			i=i+1   
		self.assertFalse(algoritmo_Marzullo(n,(HoraInicio,HoraFinal),10)[0])
	
	'''Prueba dos intervalos con la misma cantidad de puestos reservados'''
	def testDosIntervalosMismaCantidadDePuestos(self):	
		Hora1 = datetime.time(hour = 8, minute = 0, second = 0)
		Hora2 = datetime.time(hour = 9, minute = 0, second = 0)
		Hora3 = datetime.time(hour = 10, minute = 0, second = 0)
		Hora4 = datetime.time(hour = 12, minute = 0, second = 0)
		self.assertTrue(algoritmo_Marzullo(((Hora1,Hora2),(Hora1,Hora4),(Hora3,Hora4)),(Hora3,Hora4),10)[0]) 
		
	'''Caso de llenar el estacionemiento'''    
	def testEstacionemientoLleno(self):
		n = []
		i=0
		HoraInicio = datetime.time(hour = 6, minute = 0, second = 0)
		HoraFinal = datetime.time(hour = 18, minute = 0, second = 0)
		while (i <9):
			n.append((HoraInicio,HoraFinal))
			i=i+1    
		self.assertTrue(algoritmo_Marzullo(n,(HoraInicio,HoraFinal),10)[0])
		
	'''Caso Horas reservadas Cruzadas'''
	def testHorasCruzadas(self):
		n = []
		i=0
		Hora1 = datetime.time(hour = 6, minute = 0, second = 0)
		Hora2 = datetime.time(hour = 7, minute = 0, second = 0)
		Hora3 = datetime.time(hour = 8, minute = 0, second = 0)
		Hora4 = datetime.time(hour = 9, minute = 0, second = 0)
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
		HoraInicio = datetime.time(hour = 8, minute = 0, second = 0)
		HoraFinal = datetime.time(hour = 9, minute = 0, second = 0)
		while (i <10):
			n.append((HoraInicio,HoraFinal))
			i=i+1  
		self.assertFalse(algoritmo_Marzullo(n,(HoraInicio,HoraFinal),10)[0])
		
	'''Prueba para Offset iguales y tipe opuestos'''
	def testOffsetIgualesTypeOpuestos(self):
		Hora1 = datetime.time(hour = 8, minute = 0, second = 0)
		Hora2 = datetime.time(hour = 9, minute = 0, second = 0)
		Hora3 = datetime.time(hour = 10, minute = 0, second = 0)
		Hora4 = datetime.time(hour = 11, minute = 0, second = 0)
		Hora5 = datetime.time(hour = 12, minute = 0, second = 0)
		Hora6 = datetime.time(hour = 13, minute = 0, second = 0)
		Hora7 = datetime.time(hour = 14, minute = 0, second = 0)
		Hora8 = datetime.time(hour = 15, minute = 0, second = 0)
		self.assertTrue(algoritmo_Marzullo(((Hora4,Hora8),(Hora1,Hora8),(Hora2,Hora4),(Hora3,Hora7),(Hora4,Hora7),(Hora2,Hora3),(Hora2,Hora6),(Hora5,Hora8),(Hora1,Hora4),(Hora7,Hora8)),(Hora7,Hora8),10)[0])
	
	'''Prueba Simple'''
	def testPruebaSimple(self):
		Hora1 = datetime.time(hour = 8, minute = 0, second = 0)
		Hora2 = datetime.time(hour = 10, minute = 0, second = 0)
		Hora3 = datetime.time(hour = 11, minute = 0, second = 0)
		Hora4 = datetime.time(hour = 12, minute = 0, second = 0)
		Hora5 = datetime.time(hour = 13, minute = 0, second = 0)
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
								'horarioin': datetime.time(6, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_TresCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_CuatroCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	def test_EstacionamientoExtendedForm_CincoCampos(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0)}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# caso borde
	#############################ACTUALIZADO#####################################
	def test_EstacionamientoExtendedForm_TodosCamposBien(self):
		tarifa = Tarifa(
					tipoTarifa = 'wuu')
		tarifa.save()
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
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
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
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
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(6, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
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
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(7, 0),
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
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa' : tarifa,
								'monto_tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_StringHoraInicio(self):
		form_data = { 'puestos': 2,
								'horarioin': 'holaa',
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NumeroNegativoHoraInicio(self):
		form_data = { 'puestos': 2,
								'horarioin':-1,
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NoneEntarifa(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': datetime.time(14, 0),
								'tarifa': None}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_NoneEnHorarioReserva(self):
		form_data = { 'puestos': 2,
								'horarioin': 'holaa',
								'horarioout': datetime.time(19, 0),
								'horario_reserin': None,
								'horario_reserout': datetime.time(14, 0),
								'tarifa': '12'}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoExtendedForm_listaEnHoraReserva(self):
		form_data = { 'puestos': 2,
								'horarioin': datetime.time(6, 0),
								'horarioout': datetime.time(19, 0),
								'horario_reserin': datetime.time(7, 0),
								'horario_reserout': [datetime.time(14, 0)],
								'tarifa': 12}
		form = EstacionamientoExtendedForm(data = form_data)
		self.assertEqual(form.is_valid(), False)

######################################################################
# ESTACIONAMIENTO_EXTENDED pruebas controlador
###################################################################

	# normal
	def test_HorariosValidos(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# malicia
	def test_HorariosInvalido_HoraCierre_Menor_HoraApertura(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 11, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierre_Igual_HoraApertura(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierreReserva_Menor_HoraAperturaReserva(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 11, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

	# caso borde
	def test_HorariosInvalido_HoraCierreReserva_Igual_HoraAperturaReserva(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 12, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de inicio de reserva debe ser menor al horario de cierre'))

	# caso borde
	def test_Limite_HorarioValido_Apertura_Cierre(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 12, minute = 0, second = 1)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 12, minute = 0, second = 1)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_Limite_Superior_HorarioValido_Apertura_Cierre(self):
		HoraInicio = datetime.time(hour = 0, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 23, minute = 59, second = 59)
		ReservaInicio = datetime.time(hour = 12, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 23, minute = 59, second = 59)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_InicioReserva_Mayor_HoraCierreEstacionamiento(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 19, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

	# caso borde
	def test_InicioReserva_Mayor_HoraCierreEstacionamiento2(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 19, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento'))

	# malicia
	def test_CierreReserva_Mayor_HoraCierreEstacionamiento(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 17, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 20, minute = 0, second = 0)
		x = HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin)
		self.assertEqual(x, (False, 'El horario de cierre de estacionamiento debe ser mayor o igual al horario de finalización de reservas'))

	# malicia
	def test_CierreReserva_Menos_HoraInicioEstacionamiento(self):
		HoraInicio = datetime.time(hour = 12, minute = 0, second = 0)
		HoraFin = datetime.time(hour = 18, minute = 0, second = 0)
		ReservaInicio = datetime.time(hour = 10, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 11, minute = 0, second = 0)
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
		form_data = {'inicio':datetime.time(6, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# normal
	def test_EstacionamientoReserva_TodosCamposBien(self):
		form_data = {'inicio':datetime.time(6, 0), 'final':datetime.time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), True)

	# malicia
	def test_EstacionamientoReserva_InicioString(self):
		form_data = {'inicio':'hola',
								'final':datetime.time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_FinString(self):
		form_data = {'inicio':datetime.time(6, 0),
								'final':'hola'}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_InicioNone(self):
		form_data = {'inicio':None,
								'final':datetime.time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)

	# malicia
	def test_EstacionamientoReserva_finalNone(self):
		form_data = {'inicio':datetime.time(6, 0),
								'final':None}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), False)
		
###################################################################
# ESTACIONAMIENTO_PAGOS_FORM
###################################################################
	
	#malicia
	def test_Form_Vacio(self):
		form_data = {}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
		
	#normal
	def test_Form_Primer_Campo_Vacio(self):
		form_data = {'codigo_val':"123"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#normal	
	def test_Form_Segundo_Campo_Vacio(self):
		form_data = {'num_tarjeta':"1234567890123456"}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#normal	
	def test_Form_Campos_Tipos_Invalidos(self):
		form_data = {'num_tarjeta':"wertyui",
					'codigo_val':'ertyui'}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#borde	
	def test_Form_TiposCorrectos_LongitudInvalida(self):
		form_data = {'num_tarjeta':"123345678",
					'codigo_val':'123456'}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)
	
	#borde
	def test_Form_PrimerCampoValido(self):
		form_data = {'num_tarjeta':"1234567890123456",
					'codigo_val':'123456'}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)

	#borde
	def test_Form_SegundoCampoValido(self):
		form_data = {'num_tarjeta':"qwertyui",
					'codigo_val':'123'}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)

	#malicia
	def test_Form_CamposMixtos(self):
		form_data = {'num_tarjeta':"123456789012345b",
					'codigo_val':'12v'}
		form = EstacionamientoPago(data = form_data)
		self.assertEqual(form.is_valid(), False)

###################################################################
# PRUEBAS DE FUNCIONES DEL CONTROLADOR
###################################################################

##############################################################
# Estacionamiento Reserva Controlador
###################################################################

# HorarioReserva, pruebas Unitarias

	# normal
	def test_HorarioReservaValido(self):
		ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 15, minute = 0, second = 0)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (True, ''))

	# caso borde
	def test_HorarioReservaInvalido_InicioReservacion_Mayor_FinalReservacion(self):
		ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 12, minute = 59, second = 59)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El horario de apertura debe ser menor al horario de cierre'))

	# caso borde
	def test_HorarioReservaInvalido_TiempoTotalMenor1h(self):
		ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 13, minute = 59, second = 59)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El tiempo de reserva debe ser al menos de 1 hora'))

	# caso borde
	#############################ACTUALIZADO#####################################
	def test_HorarioReservaInvalido_ReservaFinal_Mayor_HorarioCierre(self):
		ReservaInicio = datetime.time(hour = 13, minute = 0, second = 0)
		ReservaFin = datetime.time(hour = 18, minute = 0, second = 1)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El horario de fin de reserva debe estar en un horario válido'))

	# caso borde
	def test_HorarioReservaInvalido_ReservaInicial_Menor_HorarioApertura(self):
		ReservaInicio = datetime.time(hour = 11, minute = 59, second = 59)
		ReservaFin = datetime.time(hour = 15, minute = 0, second = 1)
		HoraApertura = datetime.time(hour = 12, minute = 0, second = 0)
		HoraCierre = datetime.time(hour = 18, minute = 0, second = 0)
		x = validarHorarioReserva(ReservaInicio, ReservaFin, HoraApertura, HoraCierre)
		self.assertEqual(x, (False, 'El horario de cierre de reserva debe estar en un horario válido'))

	# malicia
	def test_Reservacion_CamposVacios(self):
		form_data = {'inicio':datetime.time(6, 0), 'final':datetime.time(12, 0)}
		form = EstacionamientoReserva(data = form_data)
		self.assertEqual(form.is_valid(), True)
