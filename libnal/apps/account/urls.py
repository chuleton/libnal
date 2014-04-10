from django.conf.urls  import patterns, include, url

urlpatterns = patterns('libnal.apps.account.views',
	#urls de autenticacion
 	# nombre en url --- nombre en el  views -- nombre en el template
	url(r'^inicio_sesion/$','login', name='login_view'),
	url(r'^inicio_sesion/inicio/$','login', name='login'),
	url(r'^inicio_sesion/cerrar_sesion/$','logout', name='logout'),
	url(r'^inicio_sesion/ingresado/$','loggedin', name='loggedin'),
	url(r'^inicio_sesion/invalido/$','invalid_login', name='invalid_login'),
	#url(r'^account/$','registro_view', name='vista_registro'),	
)
