from django.db import models
from proyecto.models import Proyecto
import os
from django.conf import settings

# Create your models here.

def user_directory_path_empleado(instance, filename):
    profile_picture_name = 'empleados/{0}/profile.jpg'.format(instance.primer_nombre)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name


class Empleado(models.Model):
    identificacion = models.CharField(max_length=100, blank=False)
    primer_nombre = models.CharField(max_length=100, blank=False)
    segundo_nombre = models.CharField(max_length=100,blank=False,null=True)
    primer_apellido = models.CharField(max_length=100,blank=False)
    segundo_apellido = models.CharField(max_length=100,blank=False,null=True)
    edad = models.PositiveIntegerField(blank=False, null=True)
    celular = models.CharField(max_length=10,blank=False)
    email = models.EmailField(blank=False,null=True)
    foto = models.ImageField(default='users/user_default_profile.png', upload_to=user_directory_path_empleado)


    def __str__(self):
        return self.primer_nombre


class Asignacion_Empleado(models.Model):
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, related_name="empleados")
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="proyecto")

    def __str__(self):
        return str(self.empleado)


