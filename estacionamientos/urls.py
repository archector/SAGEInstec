# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from estacionamientos import views


# Este error es raro, en django funciona
urlpatterns = patterns('',
    url(r'^$', views.estacionamientos_all, name = 'estacionamientos_all'),
    url(r'^(?P<_id>\d+)/$', views.estacionamiento_detail, name = 'estacionamiento_detail'),
    url(r'^(?P<_id>\d+)/reserva$', views.estacionamiento_reserva, name = 'estacionamiento_reserva'),
	url(r'^estacionamientos$', views.estacionamientos_all, name = 'estacionamientos_all'),    
    url(r'^(?P<_id>\d+)/pagos$', views.estacionamiento_pagos, name = 'estacionamiento_pagos'),
    url(r'^(?P<_id>\d+)/eliminandoreserva$',views.eliminar_reserva_view, name = 'eliminar_reserva_view'),
    url(r'^(?P<_id>\d+)/recibo$',views.recibo_pago, name = 'recibo_pago'),
    url(r'^(?P<_id>\d+)/pagosform$',views.form_pago, name = 'form_pago'),
    url(r'^(?P<_id>\d+)/pagoconfirm$',views.pago_confirm, name = 'pago_confirm'),
    url(r'^reporteingresos$',views.reporte_ingresos, name = 'reporte_ingresos'),
    url(r'^reportereservas$',views.reporte_reservas, name = 'reporte_reservas'),
    url(r'^reportetasas$',views.reporte_tasas, name = 'reporte_tasas'),
)
