from django.contrib import admin
from .models import Empleado, Asignacion_Empleado
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class EmpleadosResource(resources.ModelResource):
    class Meta:
        model = Empleado

class EmpleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['primer_nombre']
    resource_class = EmpleadosResource


admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Asignacion_Empleado)
