# reception/models.py

from django.db import models
from hospital.models import Hospital
from django.conf import settings

class Patient(models.Model):
    """
    Model to represent patients registered at the reception.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reception_patients')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='reception_patients')

    def __str__(self):
        return f"{self.user.username} - Reception Patient"
