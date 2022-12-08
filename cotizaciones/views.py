from django.shortcuts import render
from django.views import View
from materiales.models import Asignacion_Material
from cotizaciones.models import Cotizacion
from proyecto.models import Proyecto

from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail

# Create your views here.

class CotizacionProyecto(View):
    def get(self, request, *args, **kwargs):
        logged_in_user=request.user
        materiales = Asignacion_Material.objects.filter(proyecto__cliente__in=[logged_in_user.id])

        print(materiales)

        proyect = get_object_or_404(Proyecto, cliente__in=[logged_in_user.id])

        print(proyect)

        print(request.user.email)

        email = request.user.email

        precio = 0
        for materiale in materiales:
            print(materiale.material, " --> ",materiale.material.precio)
            precio = precio + materiale.material.precio

        print(precio)
            
        # p, created = Cotizacion.objects.get_or_create(proyecto=proyect,precio=precio)
        # p.save()

        send_mail(
            subject="Cotización realizada",
            message="Realizaste la cotización de tu proyecto, esperamos que te haya gustado.",
            recipient_list=[email],
            from_email="Rembryn <henry_rodriguez23201@elpoli.edu.co>"
        )

        context={
            'materiales':materiales,
        }
        
        return render(request, 'pages/index.html', context)
        





