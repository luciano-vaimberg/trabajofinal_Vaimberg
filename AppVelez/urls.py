from django.urls import path
from .views import inicio, sociosemipleno, sociopleno, empleado, plenoform, semiplenoform, empleadosform

urlpatterns = [
    path('', inicio, name="inicio"),
    path('sociosemipleno/', sociosemipleno ,name="sociosemipleno"),
    path('sociopleno/', sociopleno ,name="sociopleno"),
    path('empleado/', empleado ,name="empleado"),
    path('plenoform/', plenoform ,name="plenoform"),
    path('semiplenoform/', semiplenoform ,name="semiplenoform"),
    path('empleadoform/', empleadosform ,name="empleadoform"),
    
]