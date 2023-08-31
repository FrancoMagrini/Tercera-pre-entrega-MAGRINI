from django import forms



class UsuarioForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    telefono= forms.IntegerField()
    
class CanchaPadelForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    fecha= forms.DateField()
    hora= forms.TimeField()

class CanchaFutbolForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellidoo= forms.CharField(max_length=50)
    fecha= forms.DateField()
    hora= forms.TimeField()

class VerificacionForm(forms.Form):
    fecha = forms.DateField()
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))