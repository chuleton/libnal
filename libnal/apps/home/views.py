from django.shortcuts  import render_to_response
from django.template  import RequestContext
from django.http import HttpResponseRedirect

from libnal.apps.agencias.models import agencia
from libnal.apps.banner.models import banner


def index_view(request):
	banners = banner.objects.filter
	ctx = { 'banner': banners}
	return render_to_response('home/index.html', ctx , context_instance=RequestContext(request))

def libros_view(request):
	return render_to_response('home/libros.html', context_instance=RequestContext(request))

def bonos_view(request):
	listabonos = [20000 , 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000 ]
	return render_to_response("home/bonos.html", { "LISTABONOS" : listabonos })
	#country_list = Country.objects.all()
	#return render_to_response("home/bonos.html", { "COUNTRY_LIST" : country_list })

def contactenos_view(request):
	agencias = agencia.objects.filter
	ctx = { 'agencia': agencias}
	return render_to_response('home/contactenos.html', ctx , context_instance=RequestContext(request))

def novedades_view(request):
	return render_to_response('home/novedades.html', context_instance=RequestContext(request))


def registro_view(request):
    return render_to_response('register/registro.html', context_instance=RequestContext(request))


def inicio_sesion_view(request):
    return render_to_response('account/login.html', context_instance=RequestContext(request))