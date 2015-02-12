# -*- coding: utf-8 -*-
from django.contrib import admin
from estacionamientos.models import Estacionamiento, ReservasModel, Tarifa

admin.site.register(Estacionamiento,list_display=('Tarifa',))
admin.site.register(Tarifa, list_display=('tipoTarifa',),search_fields=('Tarifa',))
admin.site.register(ReservasModel)