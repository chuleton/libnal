from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #Habilitamos el modulo de administracion del aplicativo web
    url(r'^admin/', include(admin.site.urls)),
    # Habilitamos el uso de la carpeta media/  para el uso posterior de imagenes, css, o js
    url('^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    # Habilitamos el modulo en para que se muestren los templates
    url(r'^', include('libnal.apps.home.urls')),
    url(r'^', include('libnal.apps.account.urls')),
    url(r'^', include('libnal.apps.register.urls')),
)
