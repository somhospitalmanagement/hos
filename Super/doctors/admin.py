# apps/doctors/admin.py
from django.contrib import admin
from .models import Consultation  # Import your Consultation model

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'notes', 'date')
    list_filter = ('date',)
    search_fields = ('doctor',)

