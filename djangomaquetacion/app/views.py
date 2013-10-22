# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from models import Menu, Articulo,Comentario, Exposicion
from django.template import RequestContext

def home(request):
	menu = Menu.objects.all()
	articulo = Articulo.objects.filter(Menu_id = 1)
	comentario = Comentario.objects.filter(Articulo_id__in = articulo)
	exposicion = Exposicion.objects.filter(Menu_id = 1)
	template = 'index.html'
	diccionario = {'menu' : menu , 'articulo' : articulo,'comentario' : comentario, 'exposicion': exposicion}
	return render_to_response(template, diccionario, context_instance=RequestContext(request))


def nosotros(request, id_menu):
	dato = get_object_or_404(Menu,pk=id_menu)
	articulo = Articulo.objects.filter(Menu_id = dato)
	template = 'nosotros.html'
	diccionario = {'articulo' : articulo}
	return render_to_response(template, diccionario, context_instance = RequestContext(request))

def galeria(request,id_menu):
	pass
