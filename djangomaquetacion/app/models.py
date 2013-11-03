#encoding:utf-8

from django.db import models

# Create your models here.

class BannerInicio(models.Model):
	Nombre = models.CharField(max_length=140)
	Imagen = models.ImageField(upload_to='banner',verbose_name='Imágen')
	Posicion = models.IntegerField(default=0)

	def enviar_imagen(self):
		return self.Imagen

class Articulo(models.Model):
	Titulo = models.CharField(max_length=140)
	Descripcion = models.TextField(max_length=255)

	def __unicode__(self):
		return self.Titulo


class Comentario(models.Model):
	Descripcion = models.TextField(max_length=255)
	Autor = models.CharField(max_length=140)
	Articulo = models.ForeignKey(Articulo)


class Exposicion(models.Model):
	Titulo = models.CharField(max_length=140)
	Descripcion = models.TextField(max_length=255)
	Imagen = models.ImageField(upload_to='app', verbose_name='Imágen')

	def enviar_imagen(self):
		return self.Imagen

class Nosotro(models.Model):
	Titulo = models.CharField(max_length=140)
	Descripcion = models.TextField(max_length=255)


class BannerNosotro(models.Model):
	Descripcion = models.CharField(max_length=140)
	Imagen = models.ImageField(upload_to = 'banner', verbose_name='Imágen')
	Posicion = models.IntegerField(default=0)

	def enviar_imagen(self):
		return self.Imagen

class Galeria(models.Model):
	Descripcion = models.CharField(max_length=140)
	Imagen = models.ImageField(upload_to='galeria',verbose_name='Imágen')

	def __unicode__(self):
		return self.Descripcion

	def enviar_imagen(self):
		return self.Imagen

class DetalleGaleria(models.Model):
	Titulo = models.CharField(max_length=140)
	Descripcion = models.TextField(max_length=255)
	Imagen = models.ImageField(upload_to='galeria',verbose_name="Imágen")
	Galeria = models.ForeignKey(Galeria)

	def enviar_imagen(self):
		return self.Imagen

class Taller(models.Model):
	Titulo = models.CharField(max_length=140)
	Descripcion = models.TextField(max_length=255)
	Imagen = models.ImageField(upload_to='app',verbose_name='Imágen')
	Posicion = models.IntegerField(default=0)

	def enviar_imagen(self):
		return self.Imagen

class Artista(models.Model):
	Titulo = models.CharField(max_length=140)
	Descripcion = models.TextField(max_length=255)

class BannerArtista(models.Model):
	Descripcion = models.CharField(max_length=140)
	Imagen = models.ImageField(upload_to = 'banner', verbose_name='Imágen')
	Posicion = models.IntegerField(default=0)

	def enviar_imagen(self):
		return self.Imagen

class DatosEmpresa(models.Model):
	Titulo = models.CharField(max_length=140)
	Descripcion = models.TextField(max_length=255)
	Posicion = models.IntegerField(default=0)
