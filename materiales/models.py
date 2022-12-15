from django.db import models
from proyecto.models import Proyecto

# Create your models here.

class Material(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    precio = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

class Asignacion_Material(models.Model):
    material = models.ManyToManyField('Material', related_name="material")
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="proyecto+")

    def __str__(self):
        return str(self.proyecto)

    class Meta:
        verbose_name = "Asignacion_Material"
        verbose_name_plural = "Asignacion_Materiales"