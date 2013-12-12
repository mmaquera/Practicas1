from django.core.urlresolvers import reverse
from apps.follow.models import Facebook,Twitter,Blogger

def menuEn(request):
	menu = {'menuEn' : [
	{'name' : 'ABOUT US' , 'url': reverse('nosotros_views', args=[1])},
	{'name' : 'PRODUCTS' , 'url': reverse('producto_views', args=[1,0,3,0])},
	{'name' : 'CONTACT' , 'url': reverse('contacto_views', args=[1])},
	]}

	for item in menu['menuEn']:
		if request.path == item['url']:
			item['active'] = True
	
	return menu

def menuEs(request):
	menu = {'menuEs' : [
	{'name' : 'NOSOTROS' , 'url': reverse('nosotros_views',args=[2]) },
	{'name' : 'PRODUCTOS' , 'url': reverse('producto_views', args=[2,0,3,0])},
	{'name' : 'CONTACTO' , 'url': reverse('contacto_views', args=[2])},
	]}

	for item in menu['menuEs']:
		if request.path == item['url']:
			item['active'] = True
	
	return menu

def facebook(request):
	try:
		face = Facebook.objects.all()[0]
	except:
		face = '#'
	redes = {'nameFace': face}
	return redes

def blogger(request):
	try:
		blo = Blogger.objects.all()[0]
	except:
		blo = '#'
	redes = {'nameBlo': blo}
	return redes

def twitter(request):
	try:
		twi = Twitter.objects.all()[0]
	except:
		twi = '#'
	redes = {'nameTwi': twi}
	return redes