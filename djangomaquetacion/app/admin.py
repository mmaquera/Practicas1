from django.contrib import admin
from models import Articulo, Comentario,Exposicion,BannerInicio,Nosotro,BannerNosotro,Galeria,Taller,DatosEmpresa,Artista,BannerArtista

class ArticuloAdmin(admin.ModelAdmin):
	list_display = ('Titulo','Descripcion',)

class ArtistaAdmin(admin.ModelAdmin):
	list_display = ('Titulo','Descripcion',)


class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('Articulo','Descripcion','Autor',)

class ExposicionAdmin(admin.ModelAdmin):
	list_display = ('Titulo','Descripcion','Imagen_Exposicion',)

	def Imagen_Exposicion(self,obj):
		url = obj.enviar_imagen()
		tag = '<img src="/media/%s" width ="100px" />' % url
		return tag

	Imagen_Exposicion.allow_tags = True

class BannerInicioAdmin(admin.ModelAdmin):
	list_display = ('Nombre','Imagen_Banner','Posicion',)

	def Imagen_Banner(self,obj):
		url = obj.enviar_imagen()
		tag = '<img src="/media/%s" width="100px" />' % url
		return tag

	Imagen_Banner.allow_tags = True

class NosotrosAdmin(admin.ModelAdmin):
	list_display = ('Titulo','Descripcion',)

class BannerNosotrosAdmin(admin.ModelAdmin):
	list_display = ('Descripcion','Imagen_banner','Posicion',)

	def Imagen_banner(self,obj):
		url = obj.enviar_imagen()
		tag = '<img src="/media/%s" width="100px"/>' % url
		return tag

	Imagen_banner.allow_tags = True

class GaleriaAdmin(admin.ModelAdmin):
	list_display = ('Descripcion','Imagen_galeria',)

	def Imagen_galeria(self,obj):
		url = obj.enviar_imagen()
		tag = '<img src="/media/%s" width="100px"/>' % url
		return tag
	Imagen_galeria.allow_tags = True

class TallerAdmin(admin.ModelAdmin):
	list_display = ('Titulo','Descripcion','Imagen_taller','Posicion',)

	def Imagen_taller(self,obj):
		url = obj.enviar_imagen()
		tag = '<img src="/media/%s" width = "100px"/>' % url
		return tag

	Imagen_taller.allow_tags = True

class DatosEmpresaAdmin(admin.ModelAdmin):
	list_display = ('Titulo','Descripcion','Posicion',)

	
class BannerArtistaAdmin(admin.ModelAdmin):
	list_display = ('Descripcion','Imagen_banner','Posicion',)

	def Imagen_banner(self,obj):
		url = obj.enviar_imagen()
		tag = '<img src="/media/%s" width="150px" />' % url
		return tag

	Imagen_banner.allow_tags = True

admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Exposicion,ExposicionAdmin)
admin.site.register(BannerInicio,BannerInicioAdmin)
admin.site.register(Nosotro,NosotrosAdmin)
admin.site.register(BannerNosotro,BannerNosotrosAdmin)
admin.site.register(Galeria,GaleriaAdmin)
admin.site.register(Taller,TallerAdmin)
admin.site.register(DatosEmpresa,DatosEmpresaAdmin)
admin.site.register(Artista,ArtistaAdmin)
admin.site.register(BannerArtista,BannerArtistaAdmin)


