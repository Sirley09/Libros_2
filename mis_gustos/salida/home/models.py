from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
	nombres   = models.CharField(max_length = 100)
	apellidos = models.CharField(max_length = 100)

	def __str__(self):
		return self.nombres

class Genero(models.Model):
	nombre      = models.CharField(max_length = 30)

	def __str__(self):
		return self.nombre
class Editorial(models.Model):
	nombre      = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre

class Libro(models.Model):
	titulo    = models.CharField(max_length = 100)
	isbn      = models.CharField(max_length=13)
	paginas   = models.IntegerField()
	resumen  = models.TextField(max_length=2000)
	autor     = models.ManyToManyField (Autor, null = True, blank = False)
	genero    = models.ForeignKey(Genero, on_delete= models.CASCADE)
	editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
	foto      = models.ImageField(upload_to= "fotos", null=True, blank=True)

	def __str__(self):
		return self.titulo