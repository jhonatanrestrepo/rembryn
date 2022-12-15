from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from proyecto.models import Proyecto
from empleados.models import Asignacion_Empleado
from materiales.models import Asignacion_Material

from django.contrib.auth import get_user_model
User = get_user_model()


class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logged_in_user=request.user

        projects = Proyecto.objects.filter(cliente__in=[logged_in_user.id])
        empleados = Asignacion_Empleado.objects.filter(proyecto__cliente__in=[logged_in_user.id])
        materiales = Asignacion_Material.objects.filter(proyecto__cliente__in=[logged_in_user.id]).all()
       
        for o in materiales.all():
            print(o.material, "Este es el material")


        context={
            'projects':projects,
            'empleados':empleados,
            'materiales':materiales,
        }
        
        return render(request, 'pages/index.html', context)
        