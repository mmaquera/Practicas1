from django.template import RequestContext
from django.shortcuts import render_to_response
from apps.inicio.models import Nosotros,Contacto,Producto
from apps.home.models import AboutUs,Contact,Product
from apps.inicio.forms import ContactoForm
from apps.home.forms import ContactForm

def inicio_views(request):
	template = 'inicio/inicio.html'
	return render_to_response(template,context_instance = RequestContext(request))

def nosotros_views(request,id_lang):
	lang = int(id_lang)
	if lang == 1:
		try:
			nosotros = AboutUs.objects.order_by('Position')[0]
		except:
			nosotros = {}
	else:
		try:
			nosotros = Nosotros.objects.order_by('Posicion')[0]
		except:
			nosotros = {}

	diccionario = {'id_lang': lang, 'nosotros': nosotros}
	template = 'inicio/nosotros.html'
	return render_to_response(template,diccionario,context_instance = RequestContext(request))

def producto_views(request,id_lang,id_producto,id_max,id_flecha):
	lang = int(id_lang)
	flecha = int(id_flecha)
	maximo = int(id_max)
	if lang == 1:
		cantidad = Product.objects.all()
	else:
		cantidad = Producto.objects.all()

	if flecha != 3:
		if flecha == 1:
			maximo = maximo - 1
			minimo = maximo - 2
		elif flecha == 2:
			maximo = maximo + 1
			minimo = maximo - 2
		else:
			minimo = 1
			maximo = 3

		if minimo < 1:
			minimo = 1
			maximo = 3

		if maximo > cantidad.count():
			maximo = cantidad.count()
			minimo = maximo - 2
	else:
		minimo = maximo - 2

	if lang == 1:
		producto = Product.objects.filter(Position__gte = minimo, Position__lte = maximo)
		if int(id_producto) == 0:
			try:
				producto_unit = Product.objects.all()[0]
			except:
				producto_unit = {'pk':0}
		else:
			producto_unit = Product.objects.get(pk = id_producto)
	else:
		producto = Producto.objects.filter(Posicion__gte = minimo, Posicion__lte = maximo)
		if int(id_producto) == 0:
			try:
				producto_unit = Producto.objects.all()[0]
			except:
				producto_unit = {'pk':0}
		else:
			producto_unit = Producto.objects.get(pk=id_producto)

	template = 'inicio/producto.html'
	diccionario = {'id_lang':lang, 'producto':producto, 'producto_unit':producto_unit,'id_max': maximo }
	return render_to_response(template,diccionario,context_instance = RequestContext(request))

def contacto_views(request,id_lang):
	lang = int(id_lang)
	if request.method == 'POST':
		pass
	else:
		if lang == 1:
			form = ContactForm()
			contactenos = Contact.objects.order_by('Position')
			
		else:
			form = ContactoForm()
			contactenos = Contacto.objects.order_by('Posicion')

	template = 'inicio/contacto.html'
	diccionario = { 'id_lang': lang ,'form':form, 'contacto':contactenos }
	return render_to_response(template,diccionario,context_instance = RequestContext(request))