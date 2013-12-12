from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.inicio.views',
	url(r'^$','inicio_views', name='inicio_views'),
	url(r'^nosotros/(?P<id_lang>\d)$','nosotros_views', name='nosotros_views'),
	url(r'^producto/(?P<id_lang>\d)/(?P<id_producto>\d)/(?P<id_max>\d)/(?P<id_flecha>\d)$','producto_views', name='producto_views'),
	url(r'^contacto/(?P<id_lang>\d)$','contacto_views', name='contacto_views'),
)
