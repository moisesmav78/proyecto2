from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2']

class InicioSesionForm(AuthenticationForm):
    pass

class CodigoVerificacionForm(forms.Form):
    codigo = forms.CharField(max_length=6, required=True)
