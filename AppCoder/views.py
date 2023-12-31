from django.shortcuts import render
from .models import Usuarios, CanchaPadel, CanchaFutbol
from django.http import HttpResponse
from datetime import datetime
from .forms import UsuarioForm, CanchaPadelForm, CanchaFutbolForm, VerificacionForm
# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def usuarios_create(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            telefono= info["telefono"]
            usuario = Usuarios(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
            usuario.save()
            formulario_usuario = UsuarioForm()
            return render(request, "AppCoder/usuarios.html", {"mensaje": "Usuario Inscripto", "formulario": formulario_usuario})
        else:
            return render(request, "AppCoder/usuarios.html", {"mensaje": "Datos inválidos"})
    else:

        formulario_usuario = UsuarioForm()

    return render(request, "AppCoder/usuarios.html", {"formulario": formulario_usuario})


def cancha_padel_create(request):
    if request.method == "POST":
        form = CanchaPadelForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre =info['nombre']
            apellido =info['apellido']
            fecha =info['fecha']
            hora =info['hora']

            cancha = CanchaPadel(nombre=nombre, apellido=apellido, fecha=fecha, hora=hora)
            cancha.save()
            return render(request, "AppCoder/CanchaPadel.html", {"mensaje": "Alquilaste tu cancha de Padel!"})
        return render(request, "AppCoder/CanchaPadel.html", {"mensaje": "Datos inválidos"})
    else:
        formulario_cancha_padel = CanchaPadelForm()
        return render(request, "AppCoder/CanchaPadel.html", {"formulario": formulario_cancha_padel})
    
def cancha_futbol_create(request):
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
    fecha_busqueda = request.GET.get('datetime')
    hora = request.GET.get('hora')
    if fecha_busqueda and hora:
        hora_busqueda = datetime.strptime(hora, "%H:%M").time()
        reservas = CanchaPadel.objects.filter(fecha__icontains=fecha_busqueda, hora__icontains=hora_busqueda)
        print(hora_busqueda)
        if reservas.exists():
            estado_cancha = "Cancha ocupada"
            return render(request, 'AppCoder/verificacion.html', {'estado_cancha': estado_cancha})
        else:
            estado_cancha = "Cancha libre"
            return render(request, 'AppCoder/verificacion.html', {'estado_cancha': estado_cancha})


    return render(request, "AppCoder/buscar_disponibilidad.html")

