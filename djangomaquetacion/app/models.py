#encoding:utf-8

from django.db import models

# Create your models here.
class Menu(models.Model):
	Descripcion = models.CharField(max_length=140)

	def __unicode__(self):
		return  self.Descripcion

class BannerInicio(models.Model):
	Nombre = models.CharField(max_length=140)
	Imagen = models.ImageField(upload_to='banner',verbose_name='Imágen')
	Posicion = models.IntegerField(default=0)

	def __unicode__(self):
		return 'Comentario: %s - Posicion: %i' % (self.Nombre,self.Posicion)

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

class Nosotro(models.Model):
	Titulo = models.CharField(max_length=140)
	Descripcion = models.TextField(max_length=255)

	def __unicode__(self):
		return self.Titulo

class BannerNosotro(models.Model):
	Descripcion = models.CharField(max_length=140)
	Imagen = models.ImageField(upload_to = 'banner', verbose_name='Imágen')
	Posicion = models.IntegerField(default=0)

	def __unicode__(self):
		return 'Comentario: %s - Posicion: %i' % (self.Descripcion,self.Posicion)

class Galeria(models.Model):
	Descripcion = models.CharField(max_length=140)
	Imagen = models.ImageField(upload_to='galeria',verbose_name='Imágen')

	def __unicode__(self):
		return self.Descripcion

class Taller(models.Model):
	Titulo = models.CharField(max_length=140)
	Descripcion = models.TextField(max_length=255)
	Imagen = models.ImageField(upload_to='app',verbose_name='Imágen')

	def __unicode__(self):
		return self.Titulo
