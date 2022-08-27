from django.shortcuts import render
from .models import SociosPlenos, SociosSemiPlenos, Empleados
from django.http import HttpResponse
# Create your views here.

def sociossemiplenos(request):  #semiplenos se considera a los socios que solo abonan para ingresar a la cancha y no para utilizar las instalaciones del club"
    socio_semipleno=SociosSemiPlenos(nombre="1", apellido="2", genero="Masculino",edad=22, documento=333333, email="dasd@dfad.com", direccion="dasdas", localidad="dasdad", provincia="dasdad", pais="dasdad", numero_socio=33)
    socio_semipleno.save()
    texto=f"smiplenos"
    return HttpResponse(texto)

def sociosplenos(request): #pleno se considera a los socios que abonan para ingresar a la cancha y pueden utilizar las instalaciones de club, ya sea parrillas, hacer algun deporte, o utilizar la pileta" 
    socio_pleno=SociosPlenos(nombre="1", apellido="2", genero="Masculino",edad=23, documento=555333, email="d321321d@dfad.com", direccion="daqqqs", localidad="qqqad", provincia="qqqsdad", pais="qqsdad", numero_socio=133)
    socio_pleno.save()
    texto2=f"plenos"
    return HttpResponse(texto2)

def empleados(request): #se considera empleados a toda aquella persona que cobra un sueldo a cambio de un trabajo en relacion de dependencia directa con el club
    empleado=Empleados(nombre="1", apellido="2", genero="Masculino",edad=43, documento=8555333, email="bvvb@dfad.com", direccion="dvcvcqqs", localidad="qqqad", provincia="qqqsdad", pais="qqsdad", cargo="kjkjkj", sueldo=3000, legajo=4343)
    empleado.save()
    texto3=f"empleados"
    return HttpResponse(texto3)        

def inicio(request):
    return render (request, "AppVelez/inicio.html")

def sociopleno(request):   
    return render (request, "AppVelez/sociopleno.html")   

def sociosemipleno(request):   
    return render (request, "AppVelez/sociosemipleno.html")      

def empleado(request):   
    return render (request, "AppVelez/empleados.html")     