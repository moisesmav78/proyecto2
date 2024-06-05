from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import CodigoVerificacion
from .forms import RegistroForm, InicioSesionForm, CodigoVerificacionForm
from django.shortcuts import render


def home(request):
    return render(request, 'usuarios/home.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('verificacion')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        form = InicioSesionForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('verificacion')
    else:
        form = InicioSesionForm()
    return render(request, 'usuarios/inicio_sesion.html', {'form': form})

@login_required
def verificacion(request):
    user = request.user
    codigo, created = CodigoVerificacion.objects.get_or_create(user=user)
    if created:
        codigo.generar_codigo()
    if request.method == 'POST':
        form = CodigoVerificacionForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['codigo'] == codigo.codigo:
                return redirect('bienvenido')
            else:
                form.add_error('codigo', 'Código incorrecto.')
    else:
        form = CodigoVerificacionForm()
    return render(request, 'usuarios/verificacion.html', {'form': form, 'codigo': codigo.codigo})

@login_required
def bienvenido(request):
    return render(request, 'usuarios/bienvenido.html')

# usuarios/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'usuarios/home.html')


# Create your views here.
