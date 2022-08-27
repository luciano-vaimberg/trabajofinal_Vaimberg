from django.shortcuts import render
from .models import SociosPlenos, SociosSemiPlenos, Empleados
from django.http import HttpResponse
# Create your views here.

   

def inicio(request):
    return render (request, "AppVelez/inicio.html")

def sociopleno(request):   
    return render (request, "AppVelez/sociopleno.html")   

def sociosemipleno(request):   
    return render (request, "AppVelez/sociosemipleno.html")      

def empleado(request):   
    return render (request, "AppVelez/empleados.html")     