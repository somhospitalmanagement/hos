from django.db import models
from hospital.models import Hospital, Department
from django.conf import settings
from patients.models import Patient
from django.core.exceptions import ValidationError

class Pharmacist(models.Model):
    """
    Model to represent pharmacists associated with a hospital and department.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='pharmacists')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='pharmacists')

    def __str__(self):
        return f"{self.user.username} - Pharmacist"

    def clean(self):
        if self.department.hospital != self.hospital:
            raise ValidationError(f"{self.department.name} is not a department of {self.hospital.name}.")


class Prescription(models.Model):
    """
    Model to represent prescriptions made for patients.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE, related_name='prescriptions')
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField(blank=True, null=True)
    date_prescribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.user.username} by {self.pharmacist.user.username}"
