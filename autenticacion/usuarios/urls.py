# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('verificacion/', views.verificacion, name='verificacion'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
]
