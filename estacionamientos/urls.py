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
)
