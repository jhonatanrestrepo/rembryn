from django.db import models

# Create your models here.

class Cotizacion(models.Model):
    fecha =models.DateField(auto_now_add=True)
    precio = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Cotizacion"
        verbose_name_plural = "Cotizaciones"

    def __str__(self):
        return str(self.fecha)



