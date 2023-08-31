from django.shortcuts import render
from .models import Usuarios, CanchaPadel, CanchaFutbol
from django.http import HttpResponse
from datetime import datetime
from .forms import UsuarioForm, CanchaPadelForm, CanchaFutbolForm
# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def Usuarios(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            telefono= info["telefono"]
            usuario = usuario(nombre=nombre, apellido=apellido, email=email, telefonon=telefono)
            usuario.save()
            formulario_usuario = UsuarioForm()
            return render(request, "AppCoder/usuarios.html", {"mensaje": "Usuario Inscripto", "formulario": formulario_usuario})
        else:
            return render(request, "AppCoder/usuarios.html", {"mensaje": "Datos inválidos"})
    else:

        formulario_usuario = UsuarioForm()

    return render(request, "AppCoder/usuarios.html", {"formulario": formulario_usuario})


def CanchaPadel(request):
    if request.method == "POST":
        form = CanchaPadelForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre =info['nombre']  
            apellido =info['apellido']  
            fecha =info['fecha']
            hora =info['hora'] 

            CanchaPadel = CanchaPadel(nombre=nombre, apellido=apellido, fecha=fecha, hora=hora)
            CanchaPadel.save()
            return render(request, "AppCoder/CanchaPadel.html", {"mensaje": "Alquilaste tu cancha de Padel!"})
        return render(request, "AppCoder/CanchaPadel.html", {"mensaje": "Datos inválidos"})
    else:
        formulario_cancha_padel = CanchaPadelForm()
        return render(request, "AppCoder/CanchaPadel.html", {"formulario": formulario_cancha_padel})
    
def CanchaFutbol(request):
    if request.method == "POST":
        form = CanchaFutbolForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre =info['nombre']  
            apellido =info['apellido']   
            fecha =info['fecha']
            hora =info['hora'] 

            CanchaFutbol = CanchaFutbol(nombre=nombre, apellido=apellido, fecha=fecha, hora=hora)
            CanchaFutbol.save()
            return render(request, "AppCoder/CanchaFutbol.html", {"mensaje": "Alquilaste tu cancha de Futbol!"})
        return render(request, "AppCoder/CanchaFutbol.html", {"mensaje": "Datos inválidos"})
    else:
        formulario_cancha_futbol = CanchaFutbolForm()
        return render(request, "AppCoder/CanchaFutbol.html", {"formulario": formulario_cancha_futbol})
  
def verificar_disponibilidad(request):
    if request.method == 'POST':
        fecha_busqueda = request.POST.get('fecha')
        hora_busqueda = datetime.strptime(request.POST.get('hora'), "%H:%M").time()

        estado_cancha = CanchaPadel.verificar_disponibilidad(fecha_busqueda, hora_busqueda)

        return render(request, 'verificacion.html', {'estado_cancha': estado_cancha})

    return render(request, 'buscar_disponibilidad.html')


#def busquedacomision(request):
  #  return render(request,"AppCoder/busquedacomision.html")

#def buscar(request):
    #comision=request.GET["comision"]
    #if comision!="":
     #   cursos=Curso.objects.filter(comision__icontains=comision)
       # return render(request,"AppCoder/resultadosBusqueda.html", {"cursos":cursos})
    #else:
      #  return render(request,"AppCoder/busquedaComision.html", {"mensaje":"che! no me ingresaste nada!!"})