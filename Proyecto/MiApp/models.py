from django.db import models

# Create your models here.
class Jugadores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=40)

class Torneos(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    puntos_otorgados = models.IntegerField()

class Entrenadores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    entrenado = models.CharField(max_length=40)
    email = models.EmailField()


