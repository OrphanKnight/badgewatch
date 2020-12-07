from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from.models import Officer, Complaint

# Register your models here.
class OfficerResource(resources.ModelResource):

    class Meta:
        model = Officer

class OfficerAdmin(ImportExportModelAdmin):
    resource_class = OfficerResource

class ComplaintResource(resources.ModelResource):

    class Meta:
        model = Complaint

class ComplaintAdmin(ImportExportModelAdmin):
    resource_class = ComplaintResource


admin.site.register(Officer, OfficerAdmin)
admin.site.register(Complaint, ComplaintAdmin)
