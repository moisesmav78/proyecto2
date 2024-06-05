from django.contrib.auth.models import AbstractUser
from django.db import models
import random

class Usuario(AbstractUser):
    pass

class CodigoVerificacion(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=6)
    creado = models.DateTimeField(auto_now_add=True)

    def generar_codigo(self):
        self.codigo = str(random.randint(100000, 999999))
        self.save()


# Create your models here.
