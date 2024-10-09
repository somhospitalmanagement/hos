# Super/reception/admin.py

from django.contrib import admin
from .models import Reception, ReceptionPatient, Appointment

class ReceptionPatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'registration_date', 'hospital')
    search_fields = ('first_name', 'last_name', 'hospital__name')
    list_filter = ('hospital', 'registration_date')
    ordering = ('registration_date',)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'notes')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__username')
    list_filter = ('doctor', 'appointment_date')
    ordering = ('appointment_date',)

# Register the models with the admin site
admin.site.register(Reception)
admin.site.register(ReceptionPatient, ReceptionPatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)