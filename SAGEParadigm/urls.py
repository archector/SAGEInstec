from django.conf.urls import patterns, include, url
from django.contrib import admin
from estacionamientos import views, urls


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'estacionamientos.views.index', name='index'),
    url(r'^estacionamientos/', include('estacionamientos.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
