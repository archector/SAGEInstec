# -*- coding: utf-8 -*-
from django.contrib import admin
from estacionamientos.models import Estacionamiento, ReservasModel, Tarifa

admin.site.register(Estacionamiento)
admin.site.register(Tarifa, list_display=('tipoTarifa',))
admin.site.register(ReservasModel)