from django.db import models
from django.conf import settings
import os
from django.utils import timezone
from cotizaciones.models import Cotizacion


User = settings.AUTH_USER_MODEL

class Cita(models.Model):
    fecha =models.DateField(auto_now_add=False,unique=True)
    hora =models.TimeField()

    def __str__(self):
        return str(self.fecha)

class Estado(models.Model):
    estado =models.CharField(max_length=100)

    def __str__(self):
        return self.estado


class Material(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre
   
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    tipo= models.CharField(max_length=100)
    fecha_inicio =models.DateField(auto_now_add=False)
    fecha_Final =models.DateField(auto_now_add=False)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proyecto")
    cita = models.ForeignKey('Cita', on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    cotizacion =models.ForeignKey(Cotizacion, blank=True, null=True,on_delete=models.CASCADE, related_name="proyectoCotizado")


    def __str__(self):
        return self.nombre




 
    

    






    
    

   
