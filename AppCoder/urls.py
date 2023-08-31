from django.urls import path
from .views import *

urlpatterns = [
    path('Usuarios/', Usuarios, name="Usuarios"),
    path('CanchaPadel/', CanchaPadel, name="CanchaPadel"),
    path('CanchaFutbol/', CanchaFutbol, name="CanchaFutbol"),
  #  path('busquedacomision/', busquedacomision, name="busquedacomision"),
  #  path('buscar/', buscar, name="buscar"),
     path('verificar-disponibilidad/', verificar_disponibilidad, name='verificar_disponibilidad'),
]