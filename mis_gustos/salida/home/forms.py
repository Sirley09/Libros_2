from django import forms
from .models import *
from django.contrib.auth.models import User

 
class contacto_form(forms.Form):
	correo  = forms.EmailField(widget=forms.TextInput())
	subjetc = forms.CharField(widget=forms.TextInput())
	texto   = forms.CharField(widget=forms.Textarea())

class agregar_libro_form(forms.ModelForm):
	class Meta:
		model  = Libro
		fields = '__all__'

class agregar_autor_form(forms.ModelForm):
	class Meta:
		model  = Autor
		fields = '__all__'

class agregar_genero_form(forms.ModelForm):
	class Meta:
		model  = Genero
		fields = '__all__'

class agregar_editorial_form(forms.ModelForm):
	class Meta:
		model  = Editorial
		fields = '__all__'

class login_form(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput())
	clave   = forms.CharField(widget=forms.PasswordInput())

class registro_form(forms.Form):
	username     = forms.CharField(label="Nombre de usuario", widget=forms.TextInput())
	email        = forms.EmailField(label="Correo Electronico", widget=forms.TextInput())
	password     = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))
	passwordConf = forms.CharField(label="Confirmar Password", widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')

	def clean_passwordConf(self):
		password     = self.cleaned_data['password']
		passwordConf = self.cleaned_data['passwordConf']
		 
		if password == passwordConf:
			pass
		else:
			raise forms.ValidationError('password no coinciden')