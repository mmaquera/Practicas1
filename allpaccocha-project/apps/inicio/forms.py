from django import forms

class ContactoForm(forms.Form):
	Nombre = forms.CharField(widget = forms.TextInput(),label='NOMBRE')
	Email = forms.CharField(widget = forms.TextInput(),label = 'E-MAIL')
	Asunto = forms.CharField(widget = forms.TextInput(),label = 'ASUNTO')
	Mensaje = forms.CharField(widget = forms.Textarea(attrs = {'cols': '30'}),label='MENSAJE')