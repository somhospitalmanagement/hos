from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'hospital', 'current_department', 'medical_history')
    search_fields = ('user__username', 'hospital__name', 'current_department__name')
    list_filter = ('hospital', 'current_department')

