from django.shortcuts  import render_to_response
from django.template  import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


from django.core.context_processors import csrf
from libnal.apps.register.forms import RegisterForm

def register_user(request):
	if request.method == "POST":
			form = RegisterForm(request.POST)
			inf = "Registro de nuevo usuario"
			if form.is_valid():
				username	=form.cleaned_data['username']
				name		=form.cleaned_data['name']
				lastname	=form.cleaned_data['lastname']
				password1	=form.cleaned_data['password1']
				password2	=form.cleaned_data['password2']
				email		=form.cleaned_data['email']
				
				u = usuario()
				u.username = username
				u.name 	= name
				u.lastname 	= lastname
				u.email		= email
				u.password = password1 
				
				u.save()#Registramos el nuevo usuario
				inf = "Se ha agregado correctamente a la base de datos"
			else:	
				inf = "La informacion contiente datos incorrectos"	
				form = RegisterForm()
				ctx = {'form':form, 'info':inf}
				return render_to_response('register/gracias.html',ctx, context_instance=RequestContext(request))
	else:
			form = RegisterForm()
			ctx = {'form':form}
			return render_to_response('register/registro.html',ctx, context_instance=RequestContext(request))
