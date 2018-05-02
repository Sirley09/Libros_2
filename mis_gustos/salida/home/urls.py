from django.urls import path
from .views import *

urlpatterns = [
	path('about/',vista_about, name = 'vista_about'),

	#Listas
	path('libros/', vista_libros, name='vista_libros'),
	path('autores/', vista_autores, name='vista_autores'),
	path('generos/', vista_generos, name='vista_generos'),
	path('editoriales/', vista_editoriales, name='vista_editoriales'),

	#Agregar
	path('agregar_libro/', vista_agregar_libro, name='vista_agregar_libro'),
	path('agregar_autor/', vista_agregar_autor, name='vista_agregar_autor'),
	path('agregar_genero/', vista_agregar_genero, name='vista_agregar_genero'),
	path('agregar_editorial/', vista_agregar_editorial, name='vista_agregar_editorial'),

	#Ver
	path('ver_libro/<int:id_lbr>/', vista_ver_libro, name='vista_ver_libro'),
	path('ver_autor/<int:id_aut>/', vista_ver_autor, name='vista_ver_autor'),
	path('ver_genero/<int:id_gen>/', vista_ver_genero, name='vista_ver_genero'),
	path('ver_editorial/<int:id_edi>/', vista_ver_editorial, name='vista_ver_editorial'),

	#Editar
	path('editar_libro/<int:id_lbr>/', vista_editar_libro, name='vista_editar_libro'),
	path('editar_autor/<int:id_aut>/', vista_editar_autor, name='vista_editar_autor'),
	path('editar_genero/<int:id_gen>/', vista_editar_genero, name='vista_editar_genero'),
	path('editar_editorial/<int:id_edi>/', vista_editar_editorial, name='vista_editar_editorial'),
	path('eliminar_libro/<int:id_lib>/', vista_eliminar_libro, name='vista_eliminar_libro'),
	path('login/', vista_login, name= 'vista_login'),	
	path('logout/', vista_logout, name='vista_logout'),
	path('registro/', vista_registro, name='vista_registro'),
	path('ws/libros/', ws_libros_vista, name='ws_libros_vista'),

]