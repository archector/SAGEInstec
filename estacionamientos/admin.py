# -*- coding: utf-8 -*-
from django.contrib import admin
from estacionamientos.models import Estacionamiento, ReservasModel, Tarifa, RecibosModel

admin.site.register(Estacionamiento,list_display=('Propietario','Nombre','Rif'))
admin.site.register(Tarifa, list_display=('tipoTarifa',),search_fields=('Tarifa',))
admin.site.register(ReservasModel,list_display=('InicioReserva','FinalReserva','Puesto','Estacionamiento'))
admin.site.register(RecibosModel, list_display=('NumeroTransaccion',),search_fields=('Recibos',))