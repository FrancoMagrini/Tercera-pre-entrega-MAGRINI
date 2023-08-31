from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios_create/', usuarios_create, name="usuarios_create"),
    path('cancha_padel_create/', cancha_padel_create, name="cancha_padel_create"),
    path('cancha_futbol_create/', cancha_futbol_create, name="cancha_futbol_create"),
  #  path('busquedacomision/', busquedacomision, name="busquedacomision"),
  #  path('buscar/', buscar, name="buscar"),
    path('verificar_disponibilidad/', verificar_disponibilidad, name='verificar_disponibilidad'),
    
]