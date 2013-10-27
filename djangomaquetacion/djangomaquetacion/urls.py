from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangomaquetacion.views.home', name='home'),
    # url(r'^djangomaquetacion/', include('djangomaquetacion.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

    url(r'^$','app.views.home',name='home'),
    url(r'^nosotros/$','app.views.nosotros', name='nosotros'),
    url(r'^galeria/$','app.views.galeria', name='galeria'),
    url(r'^taller/$', 'app.views.taller', name='taller'),
    url(r'^artista/$','app.views.artista' , name='artista'),
    url(r'^contacto/$', 'app.views.contacto', name = 'contacto'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
   
)
