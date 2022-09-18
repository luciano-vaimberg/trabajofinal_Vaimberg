from calendar import c
from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    

    class Meta:
        abstract=True


class SociosSemiPlenos(Persona):
    
    numero_socio=models.IntegerField()

    def __str__(self) -> str:
        return self.apellido+" "+self.nombre
    
class SociosPlenos(Persona):
    
    numero_socio=models.IntegerField()

    def __str__(self) -> str:
        return self.apellido+" "+self.nombre

class Empleados(Persona):
    
    legajo=models.IntegerField()

    def __str__(self) -> str:
        return self.apellido+" "+self.nombre

    