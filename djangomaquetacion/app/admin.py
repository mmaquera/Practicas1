from django.contrib import admin
from models import Menu, Articulo, Comentario,Exposicion,BannerInicio,Nosotro,BannerNosotro,Galeria,Taller,DatosEmpresa,Artista,BannerArtista

class ArticuloAdmin(admin.ModelAdmin):
	list_display = ('Titulo','Descripcion',)

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('Articulo','Descripcion','Autor',)


admin.site.register(Menu)
admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Exposicion)
admin.site.register(BannerInicio)
admin.site.register(Nosotro)
admin.site.register(BannerNosotro)
admin.site.register(Galeria)
admin.site.register(Taller)
admin.site.register(DatosEmpresa)
admin.site.register(Artista)
admin.site.register(BannerArtista)


