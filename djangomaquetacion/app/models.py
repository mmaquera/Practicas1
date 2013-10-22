#encoding:utf-8

from django.db import models

# Create your models here.
class Menu(models.Model):
	Descripcion = models.CharField(max_length=140)

	def __unicode__(self):
		return  self.Descripcion


class Articulo(models.Model):
	Titulo = models.CharField(max_length=140)
	Descripcion = models.TextField(max_length=255)
	Menu = models.ForeignKey(Menu)

	def __unicode__(self):
		return self.Titulo

class Comentario(models.Model):
	Descripcion = models.TextField(max_length=255)
	Autor = models.CharField(max_length=140)
	Articulo = models.ForeignKey(Articulo)

	def __unicode__(self):
		return self.Descripcion

class Exposicion(models.Model):
	Titulo = models.CharField(max_length=140)
	Descripcion = models.TextField(max_length=255)
	Imagen = models.ImageField(upload_to='app', verbose_name='Imágen')
	Menu = models.ForeignKey(Menu)

	def __unicode__(self):
		return self.Titulo
