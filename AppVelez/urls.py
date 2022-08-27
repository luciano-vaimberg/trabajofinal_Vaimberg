from django.urls import path
from .views import inicio, sociosemipleno, sociopleno, empleado

urlpatterns = [
    path('', inicio, name="inicio"),
    path('sociosemipleno/', sociosemipleno ,name="sociosemipleno"),
    path('sociopleno/', sociopleno ,name="sociopleno"),
    path('empleado/', empleado ,name="empleado"),

]