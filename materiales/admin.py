from django.contrib import admin
from .models import Material, Asignacion_Material
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class MaterialResource(resources.ModelResource):
    class Meta:
        model = Material

class materialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    resource_class = MaterialResource

admin.site.register(Material, materialAdmin)
admin.site.register(Asignacion_Material)

#constraseña es rodriguez22