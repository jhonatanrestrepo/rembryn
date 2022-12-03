from django.contrib import admin
from .models import User,Profile
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class UsersResource(resources.ModelResource):
    class Meta:
        model = User

class UsersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['username']
    resource_class = UsersResource

admin.site.register(User,UsersAdmin)
admin.site.register(Profile)


