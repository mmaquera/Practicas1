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
    url(r'^nosotros/(?P<id_menu>\d+)$','app.views.nosotros', name='nosotros'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
   
)
