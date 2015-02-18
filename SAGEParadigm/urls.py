from django.conf.urls import patterns, include, url
from django.contrib import admin
from estacionamientos import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SAGEPhoenix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #Redirige / a /estacionamientos
    url(r'^$', 'estacionamientos.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^estacionamientos/',include('estacionamientos.urls')),
)
