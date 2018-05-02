from django.shortcuts import render, redirect
from .forms import * 
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.core import serializers


def vista_about(request):
	return render(request, 'about.html')



#Listas
def vista_autores(request):
	Aut  = Autor.objects.all()
	Aut  = Autor.objects.order_by('nombres')

	return render(request, 'lista_autores.html', locals())

def vista_generos(request):
	Gen  = Genero.objects.all()
	Gen  = Genero.objects.order_by('nombre')

	return render(request, 'lista_generos.html', locals())

def vista_editoriales(request):
	Edi  = Editorial.objects.all()
	Edi  = Editorial.objects.order_by('nombre')

	return render(request, 'lista_editoriales.html', locals())

def vista_libros(request):
	Lib = Libro.objects.all()
	Lib = Libro.objects.order_by('id')

	return render(request, 'lista_libros.html', locals())

#Agregar libro
def vista_agregar_libro(request):
	if request.method == 'POST':
		formulario = agregar_libro_form(request.POST, request.FILES)
		if formulario.is_valid():
			libr = formulario.save(commit = False)
			libr.save()
			formulario.save_m2m()
			return redirect ('/libros/')
	else:
		formulario = agregar_libro_form()
	return render(request, 'agregar_libro.html', locals())

#Agregar autor
def vista_agregar_autor(request):
	if request.method == 'POST':
		formulario = agregar_autor_form(request.POST, request.FILES)
		if formulario.is_valid():
			libr = formulario.save(commit = False)
			libr.save()
			formulario.save_m2m()
			return redirect ('/autores/')
	else:
		formulario = agregar_autor_form()
	return render(request, 'agregar_autor.html', locals())

#Agregar genero
def vista_agregar_genero(request):
	if request.method == 'POST':
		formulario = agregar_genero_form(request.POST, request.FILES)
		if formulario.is_valid():
			libr = formulario.save(commit = False)
			libr.save()
			formulario.save_m2m()
			return redirect ('/generos/')
	else:
		formulario = agregar_genero_form()
	return render(request, 'agregar_genero.html', locals())

#Agregar editorial
def vista_agregar_editorial(request):
	if request.method == 'POST':
		formulario = agregar_editorial_form(request.POST, request.FILES)
		if formulario.is_valid():
			libr = formulario.save(commit = False)
			libr.save()
			formulario.save_m2m()
			return redirect ('/editoriales/')
	else:
		formulario = agregar_editorial_form()
	return render(request, 'agregar_editorial.html', locals())


#Ver autor
def vista_ver_autor(request, id_aut):
	a = Autor.objects.get(id=id_aut)
	return render(request, 'ver_autor.html', locals())

#Ver libro
def vista_ver_libro(request, id_lbr):
	l = Libro.objects.get(id=id_lbr)
	return render(request, 'ver_libro.html', locals())

#Ver genero
def vista_ver_genero(request, id_gen):
	g = Genero.objects.get(id=id_gen)
	return render(request, 'ver_genero.html', locals())

#Ver editorial
def vista_ver_editorial(request, id_edi):
	e = Editorial.objects.get(id=id_edi)
	return render(request, 'ver_editorial.html', locals())

	
#Editar libro
def vista_editar_libro(request, id_lbr):
	lbr = Libro.objects.get(id=id_lbr)
	if request.method == 'POST':
		formulario = agregar_libro_form(request.POST, request.FILES, instance= lbr)
		if formulario.is_valid():
			lbr = formulario.save()
			return redirect('/libros/')
	else:
		formulario = agregar_libro_form(instance= lbr)
	return render(request, 'agregar_libro.html', locals())

#Editar autor
def vista_editar_autor(request, id_aut):
	aut = Autor.objects.get(id=id_aut)
	if request.method == 'POST':
		formulario = agregar_autor_form(request.POST, request.FILES, instance= aut)
		if formulario.is_valid():
			aut = formulario.save()
			return redirect('/autores/')
	else:
		formulario = agregar_autor_form(instance= aut)
	return render(request, 'agregar_autor.html', locals())


#Editar genero
def vista_editar_genero(request, id_gen):
	gen = Genero.objects.get(id=id_gen)
	if request.method == 'POST':
		formulario = agregar_genero_form(request.POST, request.FILES, instance= gen)
		if formulario.is_valid():
			gen = formulario.save()
			return redirect('/generos/')
	else:
		formulario = agregar_genero_form(instance= gen)
	return render(request, 'agregar_genero.html', locals())

#Editar editorial
def vista_editar_editorial(request, id_edi):
	edi = Editorial.objects.get(id=id_edi)
	if request.method == 'POST':
		formulario = agregar_editorial_form(request.POST, request.FILES, instance= edi)
		if formulario.is_valid():
			edi = formulario.save()
			return redirect('/editoriales/')
	else:
		formulario = agregar_editorial_form(instance= edi)
	return render(request, 'agregar_editorial.html', locals())

#eliminar libro
def vista_eliminar_libro(request, id_lib):
	lib = Libro.objects.get(id= id_lib)
	lib.delete()
	return redirect ('/libros/')


#login
def vista_login(request):
	usu = ""
	cla = ""
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario'] 
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username= usu, password= cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/libros/')
			else:
				msj = "usuario o clave incorrectos"

	formulario = login_form()
	return render(request, 'login.html', locals())
#logout
def vista_logout(request):
	logout(request)
	return redirect('/autores/')

#registro
def vista_registro(request):
	formulario = registro_form()
	if request.method == 'POST':
		formulario = registro_form(request.POST)
		if formulario.is_valid():
			username     = formulario.cleaned_data['username'] 
			email        = formulario.cleaned_data['email']
			password     = formulario.cleaned_data['password']
			passwordConf = formulario.cleaned_data['passwordConf']
			u = User.objects.create_user(username=username, email=email, password=password)
			u.save() 
			return render(request, "mensaje.html", locals())
	return render(request, 'registro.html', locals())
	

def ws_libros_vista(request):
	data = serializers.serialize('json', Libro.objects.filter())
	return HttpResponse(data, content_type='aplication/json')
