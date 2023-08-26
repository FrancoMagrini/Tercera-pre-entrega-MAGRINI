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

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def cursos(request):
    cursos= Curso.objects.all()
    return render(request,"AppCoder/cursos.html", {"cursos":cursos})

def profesores(request):
    return render(request,"AppCoder/profesores.html")

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")

def entregables(request):
    return render(request,"AppCoder/entregables.html")