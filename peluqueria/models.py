from django.db import models


class Servicios(models.Model):
	nombre = models.CharField('Servicio', max_length=30,unique=True)
	precio = models.FloatField()
	descripcion = models.TextField()
	imagen = models.ImageField(null=True,blank=True)

class Barbero(models.Model):
	cedula = models.CharField("Cédula",max_length=9,unique=True)
	nombre = models.CharField("Nombre",max_length=20)
	apellido = models.CharField("Apellido",max_length=20)
	direccion = models.TextField()
	telefono = models.CharField("Teléfono",max_length=11)
	servi = models.ForeignKey(Servicios,on_delete = models.CASCADE)
	#foto = models.ImageField()

	def __str__(self):
		return self.nombre

class ImgCarrucel(models.Model):
	img1 = models.ImageField(null=True,blank=True)
	img2 = models.ImageField(null=True,blank=True)
	img3 = models.ImageField(null=True,blank=True)
	img4 = models.ImageField(null=True,blank=True)


class diseñoGeneral(models.Model):
	titulo = models.CharField('Titulo',max_length=40)
	fondo = models.ImageField(null=True,blank=True)

class Galeria(models.Model):
	imagen = models.ImageField()

class Reservacion(models.Model):
	pass





