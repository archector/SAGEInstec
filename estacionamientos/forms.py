# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import RegexValidator
from estacionamientos.models import Tarifa
from django.forms.widgets import *

class TarifaForm(forms.Form):
    tipo = forms.CharField(required = True, label = 'Tipo de Tarifa')

class EstacionamientoForm(forms.Form):

    phone_validator = RegexValidator(
                            regex = '^((0212)|(0412)|(0416)|(0414)|(0424)|(0426))-?\d{7}',
                            message = 'Debe introducir un formato válido.'
                        )

    # nombre del dueno (no se permiten digitos)
    propietario = forms.CharField(
                    required = True,
                    label = "Propietario",
                    validators = [
                          RegexValidator(
                                regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚ ]+$',
                                message = 'Sólo debe contener letras.'
                        )
                    ]
                )

    nombre = forms.CharField(required = True, label = "Nombre")

    direccion = forms.CharField(required = True)

    telefono_1 = forms.CharField(required = False, validators = [phone_validator])
    telefono_2 = forms.CharField(required = False, validators = [phone_validator])
    telefono_3 = forms.CharField(required = False, validators = [phone_validator])

    email_1 = forms.EmailField(required = False)
    email_2 = forms.EmailField(required = False)

    rif = forms.CharField(
                    required = True,
                    label = "RIF",
                    validators = [
                          RegexValidator(
                                regex = '^[JVD]-?\d{8}-?\d$',
                                message = 'Introduzca un RIF con un formato válido. (J/V/D)-XXXXXXXX-X'
                        )
                    ]
                )

class EstacionamientoExtendedForm(forms.Form):
    puestos = forms.IntegerField(min_value = 0, label = 'Número de Puestos')

    tarifa_validator = RegexValidator(
                            regex = '(^([0-9]+(\.[0-9]+)?))$',
                            message = 'Debe contener dígitos.'
                        )

    horarioin = forms.TimeField(required = True, label = 'Horario Apertura')
    horarioout = forms.TimeField(required = True, label = 'Horario Cierre')

    horario_reserin = forms.TimeField(required = True, label = 'Horario Inicio Reserva')
    horario_reserout = forms.TimeField(required = True, label = 'Horario Fin Reserva')

    tarifa = forms.ModelChoiceField(queryset=Tarifa.objects.all())
    monto_tarifa = forms.CharField(required = True,validators = [tarifa_validator])
    
    pico_inicio = forms.TimeField(required = False,label = 'Inicio Pico')
    pico_fin = forms.TimeField(required = False,label = 'Final Pico')
    monto_pico = forms.CharField(required = False,label = 'Monto Pico',validators = [tarifa_validator])


class EstacionamientoReserva(forms.Form):
    inicio = forms.DateTimeField(required = True,label = 'Inicio Reserva')
    final = forms.DateTimeField(required = True,label = 'Final Reserva')


class EstacionamientoRif(forms.Form):
    rif = forms.CharField(
                    required = True,
                    label = "RIF: J-12345678-0",
                    validators = [
                          RegexValidator(
                                regex = '^[JVD]-?\d{8}-?\d$',
                                message = 'Introduzca un RIF con un formato válido. (J/V/D)-XXXXXXXX-X'
                        )
                    ]
                )

class EstacionamientoCi(forms.Form):
    ci_validator = RegexValidator(
                        regex = "^\d{5,9}$",
                        message = 'Introduzca una cédula con un formato válido.'
                    )

    ci = forms.CharField(required = True,label = "Ej: 12345678",validators = [ci_validator])
    

class EstacionamientoPago(forms.Form):
    num_validator = RegexValidator(
                            regex = '^(\d{16})$',
                        )
    
    cvv_validator = RegexValidator(
                            regex = '^(\d{3}$)',
                        )
    
    cedula_validator = RegexValidator(
                            regex = '^(\d{8}$)',
                        )
    
    nombre_validator = RegexValidator(
                            regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ ]+$',
                        )
 
    apellido_validator = RegexValidator(
                            regex = '^[a-zA-ZáéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ ]+$',
                        )
    
    nombre = forms.CharField(required = True,validators=[nombre_validator])
    apellido = forms.CharField(required = True,validators=[apellido_validator])
    cedula = forms.CharField(required = True,validators=[cedula_validator])
    num_tarjeta = forms.CharField(required = True, validators=[num_validator])
    codigo_val = forms.CharField(required = True,validators=[cvv_validator])
    
