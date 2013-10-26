# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from models import Menu, Articulo, Comentario, Exposicion, BannerInicio, Nosotro, BannerNosotro, Galeria, Taller
from django.template import RequestContext

def home(request):
	menu = Menu.objects.all()
	banner = BannerInicio.objects.order_by('Posicion')
	articulo = Articulo.objects.filter(Menu_id = 1)
	comentario = Comentario.objects.filter(Articulo_id__in = articulo)
	exposicion = Exposicion.objects.filter(Menu_id = 1)
	template = 'index.html'
	diccionario = {'menu' : menu , 'articulo' : articulo,'comentario' : comentario, 'exposicion': exposicion ,'banner' : banner}
	return render_to_response(template, diccionario, context_instance=RequestContext(request))


def nosotros(request):
	nosotros = Nosotro.objects.all()
	banner = BannerNosotro.objects.order_by('Posicion')
	template = 'nosotros.html'
	diccionario = {'nosotros' : nosotros ,'banner' : banner}
	return render_to_response(template, diccionario, context_instance = RequestContext(request))

def galeria(request):
	galeria = Galeria.objects.all()
	template = 'galeria.html'
	diccionario = { 'galeria' : galeria }
	return render_to_response(template,diccionario, context_instance = RequestContext(request))

	
def taller(request):
	taller = Taller.objects.order_by('Posicion')
	template = 'taller.html'
	diccionario = { 'taller' : taller }
	return render_to_response(template,diccionario,context_instance = RequestContext(request))