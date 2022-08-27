from django.db import models

# Create your models here.

class SociosSemiPlenos(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    genero=models.CharField(max_length=25)
    edad=models.IntegerField()
    documento=models.IntegerField()
    email=models.EmailField()
    direccion=models.CharField(max_length=50)
    localidad=models.CharField(max_length=50)
    provincia=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    numero_socio=models.IntegerField()
    
class SociosPlenos(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    genero=models.CharField(max_length=25)
    edad=models.IntegerField()
    documento=models.IntegerField()
    email=models.EmailField()
    direccion=models.CharField(max_length=50)
    localidad=models.CharField(max_length=50)
    provincia=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    numero_socio=models.IntegerField()

class Empleados(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    genero=models.CharField(max_length=25)
    edad=models.IntegerField()
    documento=models.IntegerField()
    email=models.EmailField()
    direccion=models.CharField(max_length=50)
    localidad=models.CharField(max_length=50)
    provincia=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    cargo=models.CharField(max_length=50)
    sueldo=models.IntegerField()
    legajo=models.IntegerField()

    