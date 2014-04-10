from django.conf.urls  import patterns, url

urlpatterns = patterns('libnal.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^libros/$','libros_view', name='vista_libros'),
	url(r'^bonos/$','bonos_view', name='vista_bonos'),
	url(r'^novedades/$','novedades_view', name='vista_novedades'),
	url(r'^contactenos/$','contactenos_view', name='vista_contactenos'),
	url(r'^inicio_sesion/$','inicio_sesion_view', name='login_view'),
)