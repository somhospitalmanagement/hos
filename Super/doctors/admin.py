# apps/doctors/admin.py
from django.contrib import admin
from .models import Consultation, Doctor
@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'notes', 'date')
    list_filter = ('date',)
    search_fields = ('doctor',)



@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'hospital', 'department')
    search_fields = ('doctor', 'hospital__name', 'department__name')

