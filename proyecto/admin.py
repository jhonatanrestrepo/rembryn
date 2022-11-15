from django.contrib import admin
from .models import Proyecto,Cita,Estado, Material
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ProyectoResource(resources.ModelResource):
    class Meta:
        model = Proyecto


class ProyectoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    resource_class = ProyectoResource


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Cita)
admin.site.register(Estado)
