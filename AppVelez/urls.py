from django.urls import path
from .views import busquedaEmpleados, buscarEmpleados,buscarSocioSemiPleno, busquedaSocioSemiPleno ,busquedaSocioPleno, inicio, sociosemipleno, sociopleno, empleado, plenoform, semiplenoform, empleadosform, buscarSocioPleno

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
]