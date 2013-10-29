from django.core.urlresolvers import reverse

def menu(request):
	menu = {'menu': [
		{'name' : 'Inicio', 'url' : reverse('home')},
		{'name' : 'Nosotros', 'url' : reverse('nosotros')},
		{'name' : 'Galería', 'url' : reverse('galeria')},
		{'name' : 'El Taller', 'url' : reverse('taller')},
		{'name' : 'El Artista', 'url' : reverse('artista')},
		{'name' : 'Contacto', 'url' : reverse('contacto')}
	]}

	for item in menu:
		if request.path == item['url']:
			item['active'] = True
	return menu