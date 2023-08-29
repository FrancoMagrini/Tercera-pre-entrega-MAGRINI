from django.shortcuts import render
from .models import Curso, Profesor
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
    profes=Profesor.objects.all()
    return render(request,"AppCoder/profesores.html", {"profes":profes})

def cursoformulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        comision=request.POST["comision"]
        curso=Curso(nombre=nombre, comision=comision)
        curso.save()
        return render(request,"AppCoder/cursoformulario.html", {"mensaje":"Curso Creado"})
    else:
        return render(request,"AppCoder/cursoformulario.html")
    

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")

def entregables(request):
    return render(request,"AppCoder/entregables.html")