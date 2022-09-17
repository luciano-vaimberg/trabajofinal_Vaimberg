from django.db import models

# Create your models here.

class SociosSemiPlenos(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    numero_socio=models.IntegerField()

    def __str__(self) -> str:
        return self.apellido+" "+self.nombre
    
class SociosPlenos(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    numero_socio=models.IntegerField()

    def __str__(self) -> str:
        return self.apellido+" "+self.nombre

class Empleados(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    legajo=models.IntegerField()

    def __str__(self) -> str:
        return self.apellido+" "+self.nombre

    