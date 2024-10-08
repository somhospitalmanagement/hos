from django.contrib import admin
from .models import Nurse, PatientCare

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ('user', 'hospital', 'department')
    search_fields = ('user__username', 'hospital__name', 'department__name')

@admin.register(PatientCare)
class PatientCareAdmin(admin.ModelAdmin):
    list_display = ('patient', 'nurse', 'date')
    search_fields = ('patient__user__username', 'nurse__user__username')
    list_filter = ('nurse', 'date')
