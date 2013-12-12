from django.contrib import admin
from models import Nosotros,Producto,Contacto

class NosotrosAdmin(admin.ModelAdmin):
	list_display = ('Titulo','Descripcion','Posicion',)

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('Nombre','Descripcion','ImagenProductoMenu','ImagenProductoPortal','Posicion',)

	def ImagenProductoMenu(self,obj):
		url = obj.obtenerImagenMenu()
		tag = "<img src='/media/%s' width='100px'/>" % url
		return tag

	ImagenProductoMenu.allow_tags = True

	def ImagenProductoPortal(self,obj):
		url = obj.obtenerImagenPortal()
		tag = "<img src='/media/%s' width='100px'/>" % url
		return tag

	ImagenProductoPortal.allow_tags = True

class ContactoAdmin(admin.ModelAdmin):
	list_display = ('Titulo','Descripcion','Posicion',)

admin.site.register(Nosotros,NosotrosAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Producto,ProductoAdmin)

