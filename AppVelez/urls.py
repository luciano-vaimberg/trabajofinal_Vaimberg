from django.urls import path
from .views import inicio, sociossemiplenos, sociosplenos, empleados

urlpatterns = [
    path('', inicio, name="inicio"),
    path('sociossemiplenos/', sociossemiplenos ,name="sociossemiplenos"),
    path('sociosplenos/', sociosplenos ,name="sociosplenos"),
    path('empleados/', empleados ,name="empleados"),

]