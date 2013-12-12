#encoding:utf-8
from django.db import models

class Nosotros(models.Model):
	Titulo = models.CharField(max_length = 140)
	Descripcion = models.TextField(max_length = 255)
	Posicion = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.Titulo

class Producto(models.Model):
	Nombre = models.CharField(max_length = 140)
	Descripcion = models.TextField(max_length = 255)
	ImagenMenu = models.ImageField(upload_to = 'imgs', verbose_name='Imagén Menu')
	ImagenPortal = models.ImageField(upload_to = 'imgs', verbose_name='Imagén Portal')
	Posicion = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.Nombre

	def obtenerImagenMenu(self):
		return self.ImagenMenu

	def obtenerImagenPortal(self):
		return self.ImagenPortal

class Contacto(models.Model):
	Titulo = models.CharField(max_length = 140)
	Descripcion = models.TextField(max_length = 255)
	Posicion = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.Titulo
