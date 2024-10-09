# reception/models.py

from django.db import models
from hospital.models import Hospital
from django.conf import settings
from patients.models import Patient

class Reception(models.Model):
    """
    Model to represent patients registered at the reception.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reception_patients')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='reception_patients')

    def __str__(self):
        return f"{self.user.username} - Reception Patient"





class ReceptionPatient(Patient):
    """
    Model to represent patients registered at the reception.
    Inherits from the Patient model in the patients app.
    """
    
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Reception Patient"