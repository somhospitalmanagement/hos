from django.contrib import admin
from .models import Pharmacist, Prescription

@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'hospital')
    search_fields = ('user__username', 'department__name', 'hospital__name')

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'pharmacist', 'medicine_name', 'dosage', 'date_prescribed')
    search_fields = ('patient__user__username', 'pharmacist__user__username', 'medicine_name')
    list_filter = ('date_prescribed',)

