from django.db import models
from datetime import datetime

class Usuarios(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    telefono= models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class CanchaPadel(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    fecha= models.DateField()
    hora= models.TimeField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.fecha} - {self.hora}"
    

class CanchaFutbol(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    fecha= models.DateField()
    hora= models.TimeField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.fecha} - {self.hora}"
