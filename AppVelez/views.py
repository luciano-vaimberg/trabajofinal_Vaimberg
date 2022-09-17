from django.shortcuts import render
from .models import SociosPlenos, SociosSemiPlenos, Empleados
from django.http import HttpResponse
from AppVelez.forms import plenoForm, semiPlenoForm, empleadoform
# Create your views here.

   

def inicio(request):
    return render (request, "AppVelez/inicio.html")

def sociopleno(request):   
    return render (request, "AppVelez/sociopleno.html")   

def sociosemipleno(request):   
    return render (request, "AppVelez/sociosemipleno.html")      

def empleado(request):   
    return render (request, "AppVelez/empleados.html")     

def semiplenoform(request):

    if request.method=="POST":
        formulario_semipleno=semiPlenoForm(request.POST)
        if formulario_semipleno.is_valid():
            info_semipleno=formulario_semipleno.cleaned_data
            nombre=info_semipleno["nombre"]
            apellido=info_semipleno["apellido"]
            genero=info_semipleno["genero"]
            edad=info_semipleno["edad"]
            documento=info_semipleno["documento"]
            email=info_semipleno["email"]
            direccion=info_semipleno["direccion"]
            localidad=info_semipleno["localidad"]
            provincia=info_semipleno["provincia"]
            pais=info_semipleno["pais"]
            numero_socio=info_semipleno["numero_socio"] 
            semipleno=SociosSemiPlenos(nombre=nombre, apellido=apellido,genero=genero,edad=edad,documento=documento,email=email,direccion=direccion,localidad=localidad,provincia=provincia,pais=pais,numero_socio=numero_socio)
            semipleno.save()
            return render(request, "AppVelez/inicio.html", {"mensaje_sociosemipleno":"socio semipleno creado con éxito"}) 
        else:
            return render(request, "AppVelez/inicio.html", {"mensaje_sociosemipleno":"error"}) 
    else:
        formulariosemipleno=semiPlenoForm()
        return render(request, "AppVelez/semiform.html", {"formulariosemipleno":formulariosemipleno})
   

def plenoform(request):

    if request.method=="POST":
        formulario_pleno=plenoForm(request.POST)
        if formulario_pleno.is_valid():
            info_pleno=formulario_pleno.cleaned_data
            nombre=info_pleno["nombre"]
            apellido=info_pleno["apellido"]
            genero=info_pleno["genero"]
            edad=info_pleno["edad"]
            documento=info_pleno["documento"]
            email=info_pleno["email"]
            direccion=info_pleno["direccion"]
            localidad=info_pleno["localidad"]
            provincia=info_pleno["provincia"]
            pais=info_pleno["pais"]
            numero_socio=info_pleno["numero_socio"] 
            pleno=SociosPlenos(nombre=nombre, apellido=apellido,genero=genero,edad=edad,documento=documento,email=email,direccion=direccion,localidad=localidad,provincia=provincia,pais=pais,numero_socio=numero_socio)
            pleno.save()
            return render(request, "AppVelez/inicio.html", {"mensaje_sociopleno":"socio pleno creado con éxito"}) 
        else:
            return render(request, "AppVelez/inicio.html", {"mensaje_sociopleno":"error"}) 
    else:
        formulariopleno=plenoForm()
        return render(request, "AppVelez/plenoform.html", {"formulariopleno":formulariopleno})


def empleadosform(request):
    if request.method=="POST":
        formulario_empleado=empleadoform(request.POST)
        if formulario_empleado.is_valid():
            info_empleado=formulario_empleado.cleaned_data
            nombre=info_empleado["nombre"]
            apellido=info_empleado["apellido"]
            genero=info_empleado["genero"]
            edad=info_empleado["edad"]
            documento=info_empleado["documento"]
            email=info_empleado["email"]
            direccion=info_empleado["direccion"]
            localidad=info_empleado["localidad"]
            provincia=info_empleado["provincia"]
            pais=info_empleado["pais"]
            cargo=info_empleado["cargo"] 
            sueldo=info_empleado["sueldo"]
            legajo=info_empleado["legajo"]
            empleados1=Empleados(nombre=nombre, apellido=apellido,genero=genero,edad=edad,documento=documento,email=email,direccion=direccion,localidad=localidad,provincia=provincia,pais=pais,cargo=cargo,sueldo=sueldo,legajo=legajo)
            empleados1.save()
            return render(request, "AppVelez/inicio.html", {"mensaje_empleado":"empleado creado con éxito"}) 
        else:
            return render(request, "AppVelez/inicio.html", {"mensaje_empleado":"error"}) 
    else:
        formulario_empleado=empleadoform()
        return render(request, "AppVelez/empleadoform.html", {"formularioemp":formulario_empleado})

#Busqueda por form socio pleno 

def busquedaSocioPleno(request):
    return render (request, "AppVelez/busquedasociopleno.html")

def buscarSocioPleno(request):
    if request.GET["numero_socio"]:
        numerodesocio=request.GET["numero_socio"]
        busqueda_socio_pleno=SociosPlenos.objects.filter(numero_socio=numerodesocio)
        
        if len(busqueda_socio_pleno)!=0:
            return render(request, "AppVelez/resultadospleno.html", {"busqueda_socio_pleno":busqueda_socio_pleno})
        else:  
            return render(request, "AppVelez/resultadospleno.html", {"mensaje_pleno_":"No existe ese socio"})   
    else:   
        return render(request, "AppVelez/busquedasociopleno.html", {"mensaje_pleno_":"No ingreso datos"})         
         


#Busqueda por form socio semipleno 

def busquedaSocioSemiPleno(request):
    return render (request, "AppVelez/busquedasociosemipleno.html")

def buscarSocioSemiPleno(request):
    if request.GET["numero_socio"]:
        numerodesocio=request.GET["numero_socio"]
        busqueda_socio_semi_pleno=SociosSemiPlenos.objects.filter(numero_socio=numerodesocio)
        
        if len(busqueda_socio_semi_pleno)!=0:
            return render(request, "AppVelez/resultadossemipleno.html", {"busqueda_socio_semi":busqueda_socio_semi_pleno})
        else:
            return render(request, "AppVelez/resultadossemipleno.html", {"mensaje_semipleno_":"No existe ese socio"})  
    else:
         return render(request, "AppVelez/busquedasociosemipleno.html", {"mensaje_semipleno_":"No ingreso datos"})   

#Busqueda por form empleados

def busquedaEmpleados(request):
    return render (request, "AppVelez/busquedaempleado.html")

def buscarEmpleados(request):
    if request.GET["legajo"]:
        legajo1=request.GET["legajo"]
        busqueda_empleado=Empleados.objects.filter(legajo=legajo1)
    
    
        if len(busqueda_empleado)!=0:
            return render(request, "AppVelez/resultadosempleado.html", {"busqueda_empleados":busqueda_empleado})
        else:
            return render(request, "AppVelez/resultadosempleado.html", {"mensaje_empleado":"No existe ese legajo"})
    else:
        return render(request, "AppVelez/busquedaempleado.html", {"mensaje_empleado_":"No ingreso datos"})


#leer socios y empleados

def leerSociosPlenos(request):
    leerplenos=SociosPlenos.objects.all()
    return render(request, "AppVelez/leerSociosPlenos.html", {"leerplenos":leerplenos})

def leerSociosSemiPlenos(request):
    leersemiplenos=SociosSemiPlenos.objects.all()
    return render(request, "AppVelez/leerSociosSemiPlenos.html", {"leersemiplenos":leersemiplenos})

def leerEmpleados(request):
    leerempleados=Empleados.objects.all()
    return render(request, "AppVelez/leerEmpleados.html", {"leerempleados":leerempleados})


# Eliminar socios y empleados

def eliminarSociosPlenos(request, id):
    eliminarsociopleno=SociosPlenos.objects.get(id=id)
    eliminarsociopleno.delete()
    leerplenos=SociosPlenos.objects.all()
    return render(request, "AppVelez/leerSociosPlenos.html", {"leerplenos":leerplenos})

def eliminarSociosSemiPlenos(request, id):
    eliminarsociosemipleno=SociosSemiPlenos.objects.get(id=id)
    eliminarsociosemipleno.delete()
    leersemiplenos=SociosSemiPlenos.objects.all()
    return render(request, "AppVelez/leerSociosSemiPlenos.html", {"leersemiplenos":leersemiplenos})


def eliminarEmpleados(request, id):
    eliminarempleado=Empleados.objects.get(id=id)
    eliminarempleado.delete()
    leerempleados=Empleados.objects.all()
    return render(request, "AppVelez/leerEmpleados.html", {"leerempleados":leerempleados})     


# Modificar socios y empleados

def editarSociosPlenos(request, id):
    modificarsociopleno=SociosPlenos.objects.get(id=id)
    if request.method=="POST":
        form=plenoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            modificarsociopleno.nombre=info["nombre"]
            modificarsociopleno.apellido=info["apellido"]
            modificarsociopleno.numero_socio=info["numero_socio"]
            modificarsociopleno.save()
            leerplenos=SociosPlenos.objects.all()
            return render(request, "AppVelez/leerSociosPlenos.html", {"leerplenos":leerplenos})
    else:
        form=plenoForm(initial={"nombre":modificarsociopleno.nombre ,"apellido":modificarsociopleno.apellido , "numero_socio": modificarsociopleno.numero_socio})
        return render (request, "AppVelez/editarSociosPlenos.html", {"formulario_pleno":form , "id": modificarsociopleno.id })


def editarSociosSemiPlenos(request, id):
    modificarsociosemipleno=SociosSemiPlenos.objects.get(id=id)
    if request.method=="POST":
        form=semiPlenoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            modificarsociosemipleno.nombre=info["nombre"]
            modificarsociosemipleno.apellido=info["apellido"]
            modificarsociosemipleno.numero_socio=info["numero_socio"]
            modificarsociosemipleno.save()
            leersemiplenos=SociosSemiPlenos.objects.all()
            return render(request, "AppVelez/leerSociosSemiPlenos.html", {"leersemiplenos":leersemiplenos})
    else:
        form=semiPlenoForm(initial={"nombre":modificarsociosemipleno.nombre ,"apellido":modificarsociosemipleno.apellido , "numero_socio": modificarsociosemipleno.numero_socio})
        return render (request, "AppVelez/editarSociosSemiPlenos.html", {"formulario_semipleno":form , "id": modificarsociosemipleno.id })


def editarEmpleados(request, id):
    modificarempleado=Empleados.objects.get(id=id)
    if request.method=="POST":
        form=empleadoform(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            modificarempleado.nombre=info["nombre"]
            modificarempleado.apellido=info["apellido"]
            modificarempleado.legajo=info["legajo"]
            modificarempleado.save()
            leerempleados=Empleados.objects.all()
            return render(request, "AppVelez/leerEmpleados.html", {"leerempleados":leerempleados})   
    else:
        form=empleadoform(initial={"nombre":modificarempleado.nombre ,"apellido":modificarempleado.apellido , "legajo": modificarempleado.legajo})
        return render (request, "AppVelez/editarEmpleados.html", {"formulario_empleado":form , "id": modificarempleado.id })

