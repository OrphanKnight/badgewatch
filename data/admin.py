from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from.models import Officer, Complaint

# Register your models here.
class OfficerResource(resources.ModelResource):

    class Meta:
        model = Officer
        import_id_fields = ['badgeID']

class OfficerAdmin(ImportExportModelAdmin):
    list_display= ('badgeID', 'firstName', 'lastName')
    resource_class = OfficerResource

class ComplaintResource(resources.ModelResource):

    class Meta:
        model = Complaint
        import_id_fields = ['id']
class ComplaintAdmin(ImportExportModelAdmin):
    list_display= ( 'badgeID_id', 'category', 'classification', 'allegation', 'finding')
    resource_class = ComplaintResource

admin.site.register(Officer, OfficerAdmin)
admin.site.register(Complaint,  ComplaintAdmin)