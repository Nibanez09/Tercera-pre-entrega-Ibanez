from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    empresa = models.CharField(max_length=40)
    profesion = models.CharField(max_length=40)
    email = models.EmailField()

class Proyecto(models.Model):
    codigo = models.CharField(max_length=40)
    fecha_recibido = models.DateField()
    plazo = models.IntegerField()
    categoria = models.CharField(max_length=40)

class Responsable(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
