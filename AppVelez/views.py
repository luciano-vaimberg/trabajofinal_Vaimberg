from multiprocessing import AuthenticationError
from django.shortcuts import render
from .models import Avatar, SociosPlenos, SociosSemiPlenos, Empleados, Avatar
from django.http import HttpResponse
from AppVelez.forms import plenoForm, semiPlenoForm, empleadoform, UserEditForm
#imports para login
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

   
@login_required
def inicio(request):
    return render (request, "AppVelez/inicio.html", {"imagen_avatar": obtenerAvatar(request)})

@login_required
def sociopleno(request):   
    return render (request, "AppVelez/sociopleno.html", {"imagen_avatar": obtenerAvatar(request)})   

@login_required
def sociosemipleno(request):   
    return render (request, "AppVelez/sociosemipleno.html", {"imagen_avatar": obtenerAvatar(request)})      

@login_required
def empleado(request):   
    return render (request, "AppVelez/empleados.html", {"imagen_avatar": obtenerAvatar(request)})     

@login_required
def semiplenoform(request):

    if request.method=="POST":
        formulario_semipleno=semiPlenoForm(request.POST)
        if formulario_semipleno.is_valid():
            info_semipleno=formulario_semipleno.cleaned_data
            nombre=info_semipleno["nombre"]
            apellido=info_semipleno["apellido"]
            numero_socio=info_semipleno["numero_socio"] 
            semipleno=SociosSemiPlenos(nombre=nombre, apellido=apellido,numero_socio=numero_socio)
            semipleno.save()
            return render(request, "AppVelez/inicio.html", {"mensaje_sociosemipleno":"socio semipleno creado con éxito"}) 
        else:
            return render(request, "AppVelez/inicio.html", {"mensaje_sociosemipleno":"error"}) 
    else:
        formulariosemipleno=semiPlenoForm()
        return render(request, "AppVelez/semiform.html", {"formulariosemipleno":formulariosemipleno , "imagen_avatar": obtenerAvatar(request)})
   
@login_required
def plenoform(request):

    if request.method=="POST":
        formulario_pleno=plenoForm(request.POST)
        if formulario_pleno.is_valid():
            info_pleno=formulario_pleno.cleaned_data
            nombre=info_pleno["nombre"]
            apellido=info_pleno["apellido"]
            numero_socio=info_pleno["numero_socio"] 
            pleno=SociosPlenos(nombre=nombre, apellido=apellido,numero_socio=numero_socio)
            pleno.save()
            return render(request, "AppVelez/inicio.html", {"mensaje_sociopleno":"socio pleno creado con éxito"}) 
        else:
            return render(request, "AppVelez/inicio.html", {"mensaje_sociopleno":"error"}) 
    else:
        formulariopleno=plenoForm()
        return render(request, "AppVelez/plenoform.html", {"formulariopleno":formulariopleno , "imagen_avatar": obtenerAvatar(request)})

@login_required
def empleadosform(request):
    if request.method=="POST":
        formulario_empleado=empleadoform(request.POST)
        if formulario_empleado.is_valid():
            info_empleado=formulario_empleado.cleaned_data
            nombre=info_empleado["nombre"]
            apellido=info_empleado["apellido"]
            legajo=info_empleado["legajo"]
            empleados1=Empleados(nombre=nombre, apellido=apellido,legajo=legajo)
            empleados1.save()
            return render(request, "AppVelez/inicio.html", {"mensaje_empleado":"empleado creado con éxito"}) 
        else:
            return render(request, "AppVelez/inicio.html", {"mensaje_empleado":"error"}) 
    else:
        formulario_empleado=empleadoform()
        
        return render(request, "AppVelez/empleadoform.html", {"formularioemp":formulario_empleado, "imagen_avatar": obtenerAvatar(request)})

#Busqueda por form socio pleno 
@login_required
def busquedaSocioPleno(request):
    return render (request, "AppVelez/busquedasociopleno.html",{"imagen_avatar": obtenerAvatar(request)})
@login_required
def buscarSocioPleno(request):
    if request.GET["numero_socio"]:
        numerodesocio=request.GET["numero_socio"]
        busqueda_socio_pleno=SociosPlenos.objects.filter(numero_socio=numerodesocio)
        
        if len(busqueda_socio_pleno)!=0:
            return render(request, "AppVelez/resultadospleno.html", {"busqueda_socio_pleno":busqueda_socio_pleno})
        else:  
            return render(request, "AppVelez/resultadospleno.html", {"mensaje_pleno_":"No existe ese socio"})   
    else:   
        return render(request, "AppVelez/busquedasociopleno.html", {"mensaje_pleno_":"No ingreso datos" , "imagen_avatar": obtenerAvatar(request)})         
         

#Busqueda por form socio semipleno 

@login_required
def busquedaSocioSemiPleno(request):
    return render (request, "AppVelez/busquedasociosemipleno.html" ,{"imagen_avatar": obtenerAvatar(request)})

@login_required
def buscarSocioSemiPleno(request):
    if request.GET["numero_socio"]:
        numerodesocio=request.GET["numero_socio"]
        busqueda_socio_semi_pleno=SociosSemiPlenos.objects.filter(numero_socio=numerodesocio)
        
        if len(busqueda_socio_semi_pleno)!=0:
            return render(request, "AppVelez/resultadossemipleno.html", {"busqueda_socio_semi":busqueda_socio_semi_pleno})
        else:
            return render(request, "AppVelez/resultadossemipleno.html", {"mensaje_semipleno_":"No existe ese socio"})  
    else:
         return render(request, "AppVelez/busquedasociosemipleno.html", {"mensaje_semipleno_":"No ingreso datos" , "imagen_avatar": obtenerAvatar(request)})   

#Busqueda por form empleados

@login_required
def busquedaEmpleados(request):
    return render (request, "AppVelez/busquedaempleado.html",{"imagen_avatar": obtenerAvatar(request)})

@login_required
def buscarEmpleados(request):
    if request.GET["legajo"]:
        legajo1=request.GET["legajo"]
        busqueda_empleado=Empleados.objects.filter(legajo=legajo1)
    
    
        if len(busqueda_empleado)!=0:
            return render(request, "AppVelez/resultadosempleado.html", {"busqueda_empleados":busqueda_empleado})
        else:
            return render(request, "AppVelez/resultadosempleado.html", {"mensaje_empleado":"No existe ese legajo"})
    else:
        return render(request, "AppVelez/busquedaempleado.html", {"mensaje_empleado_":"No ingreso datos","imagen_avatar": obtenerAvatar(request)})


#leer socios y empleados

@login_required
def leerSociosPlenos(request):
    leerplenos=SociosPlenos.objects.all()
    return render(request, "AppVelez/leerSociosPlenos.html", {"leerplenos":leerplenos,"imagen_avatar": obtenerAvatar(request)})

@login_required
def leerSociosSemiPlenos(request):
    leersemiplenos=SociosSemiPlenos.objects.all()
    return render(request, "AppVelez/leerSociosSemiPlenos.html", {"leersemiplenos":leersemiplenos,"imagen_avatar": obtenerAvatar(request)})

@login_required
def leerEmpleados(request):
    leerempleados=Empleados.objects.all()
    return render(request, "AppVelez/leerEmpleados.html", {"leerempleados":leerempleados,"imagen_avatar": obtenerAvatar(request)})


# Eliminar socios y empleados

@login_required
def eliminarSociosPlenos(request, id ):
    eliminarsociopleno=SociosPlenos.objects.get(id=id)
    eliminarsociopleno.delete()
    leerplenos=SociosPlenos.objects.all()
    return render(request, "AppVelez/leerSociosPlenos.html", {"leerplenos":leerplenos , "mensaje_eliminado_sp":"< - - Socio Pleno eliminado con exito  - ->","imagen_avatar": obtenerAvatar(request)})

@login_required
def eliminarSociosSemiPlenos(request, id):
    eliminarsociosemipleno=SociosSemiPlenos.objects.get(id=id)
    eliminarsociosemipleno.delete()
    leersemiplenos=SociosSemiPlenos.objects.all()
    return render(request, "AppVelez/leerSociosSemiPlenos.html", {"leersemiplenos":leersemiplenos , "mensaje_eliminado_ssp":"<- -  Socio Semi Pleno eliminado con exito  - ->","imagen_avatar": obtenerAvatar(request)})

@login_required
def eliminarEmpleados(request, id):
    eliminarempleado=Empleados.objects.get(id=id)
    eliminarempleado.delete()
    leerempleados=Empleados.objects.all()
    return render(request, "AppVelez/leerEmpleados.html", {"leerempleados":leerempleados , "mensaje_eliminado_empleado":"<- -  Empleado eliminado con exito  - ->","imagen_avatar": obtenerAvatar(request)})     


# Modificar socios y empleados

@login_required
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
        return render (request, "AppVelez/editarSociosPlenos.html", {"formulario_pleno":form , "id": modificarsociopleno.id,"imagen_avatar": obtenerAvatar(request) })

@login_required
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
        return render (request, "AppVelez/editarSociosSemiPlenos.html", {"formulario_semipleno":form , "id": modificarsociosemipleno.id,"imagen_avatar": obtenerAvatar(request) })

@login_required
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
        return render (request, "AppVelez/editarEmpleados.html", {"formulario_empleado":form , "id": modificarempleado.id,"imagen_avatar": obtenerAvatar(request) })

# LOGIN - LOGOUT Y REGISTRO DE USUARIOS


def login_request(request):
    if request.method=="POST":
        formulario_login=AuthenticationForm(request, data = request.POST)
        if formulario_login.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]
            
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppVelez/inicio.html", {"mensaje_login": f"Bienvenido {usuario}" ,})
            else:
                return render(request, "AppVelez/login.html", {"formulario_login": formulario_login , "mensaje_login": "Usuario o contraseña incorrectas" })
        else:
             return render(request, "AppVelez/login.html", {"formulario_login": formulario_login , "mensaje_login": "Usuario o contraseña incorrectas" })        
    else:
         formulario_login=AuthenticationForm()
         return render(request, "AppVelez/login.html", {"formulario_login": formulario_login })

def register(request):
    if request.method=="POST":
        formulario_registro= UserCreationForm(request.POST)
        if formulario_registro.is_valid():
            username=formulario_registro.cleaned_data["username"]
            formulario_registro.save()
            return render (request, "AppVelez/inicio.html", {"mensaje_register": f"Usuario {username} creado"})
    else:
        formulario_registro=UserCreationForm()
        return render (request, "AppVelez/register.html" , {"formulario_registro":formulario_registro})    


# EDITAR PERFIL DE USUARIO

@login_required
def editarPerfil (request):
    usuario=request.user
    if request.method=="POST":
        formulario_edicion= UserEditForm(request.POST, instance=usuario)
        if formulario_edicion.is_valid():
            info=formulario_edicion.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.firstname=info=["first_name"]
            usuario.lastname=info=["last_name"]
            formulario_edicion.save()
            return render(request, "AppVelez/inicio.html", {"mensaje_edicion":f"Perfil de {usuario} editado"})
    else:
        formulario_edicion=UserEditForm(instance=usuario)    
    return render(request, "AppVelez/editarPerfil.html", {"formulario_edicion":formulario_edicion, "usuario":usuario ,"imagen_avatar": obtenerAvatar(request)})

# AVATAR

def obtenerAvatar(request):   
    lista_avatar= Avatar.objects.filter(user=request.user)
    if len(lista_avatar)!=0:
        imagen_avatar=lista_avatar[0].imagen.url
    else:
        imagen_avatar=""   
    return imagen_avatar