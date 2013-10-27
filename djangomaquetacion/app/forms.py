from django import forms

class ContactoForm(forms.Form):
	Nombre = forms.CharField(widget = forms.TextInput())
	Email = forms.EmailField(widget = forms.TextInput())
	Asunto = forms.CharField(widget = forms.TextInput())
	Mensaje = forms.CharField(widget = forms.Textarea(attrs = {'cols': '30'}))