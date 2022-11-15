from django.db import models
from proyecto.models import Proyecto

# Create your models here.

class Cotizacion(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="proyectoCotizado")
    fecha =models.DateField(auto_now_add=True)
    precio = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Cotizacion"
        verbose_name_plural = "Cotizaciones"

    def __str__(self):
        return str(self.proyecto)



