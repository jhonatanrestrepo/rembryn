from django.db import models
from proyecto.models import Proyecto
import os
from django.conf import settings

from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

def user_directory_path_empleado(instance, filename):
    profile_picture_name = 'empleados/{0}/profile.jpg'.format(instance.primer_nombre)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name


class Empleado(models.Model):
    identificacion = models.IntegerField(blank=False,
        default=1,
        validators=[
            MaxValueValidator(999999999999),
            MinValueValidator(100_000)
        ])
    primer_nombre = models.CharField(max_length=100, blank=False)
    segundo_nombre = models.CharField(max_length=100,blank=True,null=True)
    primer_apellido = models.CharField(max_length=100,blank=False)
    segundo_apellido = models.CharField(max_length=100,blank=True,null=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    celular = models.IntegerField(blank=False,
        default=1,
        validators=[
            MaxValueValidator(3999999999),
            MinValueValidator(300_000_0000)
        ])
    email = models.EmailField(blank=True,null=True)
    foto = models.ImageField(default='users/user_default_profile.png', upload_to=user_directory_path_empleado)


    def __str__(self):
        return self.primer_nombre

class Asignacion_Empleado(models.Model):
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, related_name="empleados")
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="proyecto")

    def __str__(self):
        return str(self.empleado)


