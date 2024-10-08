from django.contrib import admin
from .models import LabTechnician, LabTest

@admin.register(LabTechnician)
class LabTechnicianAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'hospital')
    search_fields = ('user__username', 'department__name', 'hospital__name')

@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_type', 'date_conducted')
    search_fields = ('patient__user__username', 'test_type')
    list_filter = ('date_conducted',)

