# reception/admin.py

from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """
    Admin view for managing patients registered at the reception.
    """
    list_display = ('user', 'hospital',)
    search_fields = ('user__username', 'hospital__name')
    list_filter = ('hospital',)

    def __str__(self):
        return self.user.username 
