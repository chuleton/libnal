from django.db import models

class banner(models.Model):
	imagen		=models.CharField(max_length=200)
	url			=models.TextField(max_length=300)
	info		=models.CharField(max_length=200)

	def __unicode__(self):
			imagendescripcion = "%s %s %s"%(self.imagen, self.info, self.url )
			return imagendescripcion