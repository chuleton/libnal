from django.db import models

class agencia(models.Model):
	ciudad		=models.CharField(max_length = 20)
	nombre		=models.CharField(max_length = 50)
	direccion	=models.CharField(max_length = 50)
	telefono	=models.CharField(max_length = 12)
	horarios	=models.TextField(max_length = 100)
	manejo 		=models.TextField(max_length = 100)

	def __unicode__(self):
			nombreagencia = "%s %s"%(self.ciudad, self.nombre)
			return nombreagencia
