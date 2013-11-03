# Create your views here.
#enconding:utf-8
from django.shortcuts import render_to_response,get_object_or_404,render
from models import Articulo, Comentario, Exposicion, BannerInicio, Nosotro, BannerNosotro, Galeria, DetalleGaleria, Artista, BannerArtista, Taller, DatosEmpresa
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import ContactoForm
from django.core.mail import EmailMultiAlternatives



def home(request):
	banner = BannerInicio.objects.order_by('Posicion')
	articulo = Articulo.objects.all()
	comentario = Comentario.objects.filter(Articulo_id__in = articulo)
	exposicion = Exposicion.objects.all()
	template = 'index.html'
	diccionario = {'articulo' : articulo,'comentario' : comentario, 'exposicion': exposicion ,'banner' : banner}
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
			nombre = form.cleaned_data['Nombre']
			email = form.cleaned_data['Email']
			asunto = form.cleaned_data['Asunto']
			mensaje = form.cleaned_data['Mensaje']

			to_admin = 'llanco.artista@gmail.com'
			html_content = 'Informacion Recibida:<br><br>Nombre:<br>%s<br><br>E-mail:<br>%s<br><br>Mensaje:<br>%s' % (nombre,email,mensaje)
			msg = EmailMultiAlternatives(asunto,html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content, 'text/html')
			msg.send()
	else:
		form = ContactoForm()

	datos = DatosEmpresa.objects.order_by('Posicion')
	template = 'contacto.html'
	diccionario = { 'form': form , 'datos' : datos }

	return  render_to_response(template,diccionario,context_instance = RequestContext(request))

def galeria_imagen(request,id_galeria):
	idGaleria = get_object_or_404(Galeria,pk=id_galeria)
	detalleGaelriaImagen = DetalleGaleria.objects.filter(Galeria_id=idGaleria)
	template = 'galeria_imagenes.html'
	diccionario = {'detalleGaelriaImagen':detalleGaelriaImagen}
	return render_to_response(template,diccionario,context_instance=RequestContext(request))


 