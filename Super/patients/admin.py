# patients/admin.py
from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'hospital', 'current_department', 'dob', 'medical_history')
    search_fields = ('first_name', 'last_name', 'hospital__name', 'current_department__name')
    list_filter = ('hospital', 'current_department')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('hospital', 'current_department')


