# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404,render
from models import Menu, Articulo, Comentario, Exposicion, BannerInicio, Nosotro, BannerNosotro, Galeria, Artista, BannerArtista, Taller, DatosEmpresa
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import ContactoForm



def home(request):
	menu = Menu.objects.all()
	banner = BannerInicio.objects.order_by('Posicion')
	articulo = Articulo.objects.all()
	comentario = Comentario.objects.filter(Articulo_id__in = articulo)
	exposicion = Exposicion.objects.all()
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

def artista(request):
	artista = Artista.objects.all()
	banner = BannerArtista.objects.all()
	template = 'artista.html'
	diccionario = {'artista' : artista, 'banner': banner}
	return render_to_response(template, diccionario, context_instance=RequestContext(request))

def contacto(request):
	if request.method == 'POST':
		form = ContactoForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/contacto/')
	else:
		form = ContactoForm()

	datos = DatosEmpresa.objects.order_by('Posicion')
	template = 'contacto.html'
	diccionario = { 'form': form , 'datos' : datos }

	return  render_to_response(template,diccionario,context_instance = RequestContext(request))


