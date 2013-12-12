from django.contrib import admin
from models import Facebook,Twitter,Blogger

class FacebookAdmin(admin.ModelAdmin):
	list_display = ('Url',)

class TwitterAdmin(admin.ModelAdmin):
	list_display = ('Url',)	

class BloggerAdmin(admin.ModelAdmin):
	list_display = ('Url',)	

admin.site.register(Facebook,FacebookAdmin)
admin.site.register(Twitter,TwitterAdmin)
admin.site.register(Blogger,BloggerAdmin)
