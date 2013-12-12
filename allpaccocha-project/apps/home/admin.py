from django.contrib import admin
from models import AboutUs,Product,Contact

class AboutUsAdmin(admin.ModelAdmin):
	list_display = ('Title','Description','Position',)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('Name','Description','ImageProductMenu','ImageProductPortal','Position',)

	def ImageProductPortal(self,obj):
		url = obj.getImagePortal()
		tag = "<img src='/media/%s' width='100px'/>" % url
		return tag

	ImageProductPortal.allow_tags = True
	
	def ImageProductMenu(self,obj):
		url = obj.getImageMenu()
		tag = "<img src='/media/%s' width='100px'/>" % url
		return tag

	ImageProductMenu.allow_tags = True

class ContactAdmin(admin.ModelAdmin):
	list_display = ('Title','Description','Position',)

admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Product,ProductAdmin)