from django.shortcuts import render
from .models import Curso, Profesor
from django.http import HttpResponse
from .forms import CursoForm
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
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']  # Obtén el nombre desde el formulario
            comision = form.cleaned_data['comision']  # Obtén la comisión desde el formulario
            
            curso = Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, "AppCoder/cursoformulario.html", {"mensaje": "Curso Creado"})
    else:
        formulario_curso = CursoForm()
        return render(request, "AppCoder/cursoformulario.html", {"formulario": formulario_curso})
    

def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")

def entregables(request):
    return render(request,"AppCoder/entregables.html")