from django.contrib import admin
from .models import Cotizacion
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class CotizacionResource(resources.ModelResource):
    class Meta:
        model = Cotizacion

class CotizacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['proyecto']
    resource_class = CotizacionResource

admin.site.register(Cotizacion, CotizacionAdmin)