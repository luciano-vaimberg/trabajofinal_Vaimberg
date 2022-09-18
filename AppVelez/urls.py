from django.urls import path
from .views import editarPerfil, register, login_request, editarEmpleados, editarSociosSemiPlenos, editarSociosPlenos, eliminarEmpleados, eliminarSociosSemiPlenos, eliminarSociosPlenos, leerEmpleados, leerSociosSemiPlenos, leerSociosPlenos, busquedaEmpleados, buscarEmpleados,buscarSocioSemiPleno, busquedaSocioSemiPleno ,busquedaSocioPleno, inicio, sociosemipleno, sociopleno, empleado, plenoform, semiplenoform, empleadosform, buscarSocioPleno
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name="inicio"),
    path('sociosemipleno/', sociosemipleno ,name="sociosemipleno"),
    path('sociopleno/', sociopleno ,name="sociopleno"),
    path('empleado/', empleado ,name="empleado"),
    path('plenoform/', plenoform ,name="plenoform"),
    path('semiplenoform/', semiplenoform ,name="semiplenoform"),
    path('empleadoform/', empleadosform ,name="empleadoform"),
    path('busquedasociopleno/', busquedaSocioPleno ,name="busquedasociopleno"),
    path('buscarsociopleno/', buscarSocioPleno ,name="buscarsociopleno"),
    path('busquedasociosemipleno/', busquedaSocioSemiPleno ,name="busquedasociosemipleno"),
    path('buscarsociosemipleno/', buscarSocioSemiPleno ,name="buscarsociosemipleno"),
    path('busquedaempleado/', busquedaEmpleados ,name="busquedaempleado"),
    path('buscarempleados/', buscarEmpleados  ,name="buscarempleados"),
    path('leerSociosPlenos/', leerSociosPlenos  ,name="leerSociosPlenos"),
    path('leerSociosSemiPlenos/', leerSociosSemiPlenos  ,name="leerSociosSemiPlenos"),
    path('leerEmpleados/', leerEmpleados  ,name="leerEmpleados"),
    path('eliminarSociosPlenos/<id>', eliminarSociosPlenos  ,name="eliminarSociosPlenos"),
    path('eliminarSociosSemiPlenos/<id>', eliminarSociosSemiPlenos  ,name="eliminarSociosSemiPlenos"),
    path('eliminarEmpleados/<id>', eliminarEmpleados  ,name="eliminarEmpleados"),
    path('editarSociosPlenos/<id>', editarSociosPlenos  ,name="editarSociosPlenos"),
    path('editarSociosSemiPlenos/<id>', editarSociosSemiPlenos  ,name="editarSociosSemiPlenos"),
    path('editarEmpleados/<id>', editarEmpleados  ,name="editarEmpleados"),
    path('login', login_request  ,name="login"),
    path('register', register  ,name="register"),
    path('logout', LogoutView.as_view(template_name="AppVelez/logout.html")  ,name="logout"),
    path('editarPerfil', editarPerfil  ,name="editarPerfil")
]
