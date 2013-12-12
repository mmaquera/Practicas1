from django.contrib import admin
from models import Email

class EmailAdmin(admin.ModelAdmin):
	list_display = ('Email','Password',)


admin.site.register(Email,EmailAdmin)