# reception/admin.py

from django.contrib import admin
from .models import Reception, ReceptionPatient


class ReceptionAdmin(admin.ModelAdmin):
    """
    Admin view for managing patients registered at the reception.
    """
    list_display = ('user', 'hospital',)
    search_fields = ('user__username', 'hospital__name')
    list_filter = ('hospital',)

    def __str__(self):
        return self.user.username 


class ReceptionPatientAdmin(admin.ModelAdmin):
    """
    Admin view for managing patients registered at the reception.
    """
    list_display = ('first_name', 'last_name', 'dob', 'hospital', 'registration_date')  # Display these fields in the list view
    search_fields = ('first_name', 'last_name', 'hospital__name')  # Enable search by first name, last name, and hospital name
    list_filter = ('hospital',)  # Filter by hospital

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # String representation for the admin interface

# Register the ReceptionPatient model with the admin site
admin.site.register(ReceptionPatient, ReceptionPatientAdmin)