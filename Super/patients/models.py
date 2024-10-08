from django.db import models
from hospital.models import Hospital, Department
from django.contrib.auth.models import User
from django.conf import settings
class Patient(models.Model):
    """
    Model to represent patients associated with a hospital.
    Each patient is linked to the hospital they are registered in.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='patients')
    medical_history = models.TextField(blank=True, null=True)
    current_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='current_patients')

    def __str__(self):
        return f"{self.user.username} - Patient"




