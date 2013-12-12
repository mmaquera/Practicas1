from django import forms

class ContactForm(forms.Form):
	Nombre = forms.CharField(widget = forms.TextInput(),label='NAME')
	Email = forms.CharField(widget = forms.TextInput(),label = 'E-MAIL')
	Asunto = forms.CharField(widget = forms.TextInput(),label = 'SUBJECT')
	Mensaje = forms.CharField(widget = forms.Textarea(attrs = {'cols': '30'}),label='MESSAGE')