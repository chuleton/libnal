from django.conf.urls  import patterns, url

urlpatterns = patterns('libnal.apps.register.views',
	# nombre en url --- nombre en el  views -- nombre en el template
	url(r'^registro/$','register_user', name='user_register'),
	#url(r'^registro/gracias/$','register_user', name='user_register'),


)