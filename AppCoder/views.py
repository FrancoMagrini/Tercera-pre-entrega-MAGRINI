from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def crear_curso(request):

    nombre_curso="Programacion Basica"
    comision_curso=999888
    print("creando curso")
    curso=Curso(nombre=nombre_curso,comision=comision_curso)
    curso.save()
    respuesta=f"Curso creado: {curso.nombre} - {curso.comision}"    
    return HttpResponse(respuesta)
