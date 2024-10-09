from django.db import models
from hospital.models import Hospital, Department
from django.conf import settings
from patients.models import Patient
from django.core.exceptions import ValidationError

class Doctor(models.Model):
    """
    Model to represent doctors associated with a hospital and department.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')

    def __str__(self):
        return f"Dr. {self.user.username}"

    def clean(self):
        if self.department.hospital != self.hospital:
            raise ValidationError(f"{self.department.name} is not a department of {self.hospital.name}.")


class Consultation(models.Model):
    """
    Model to represent a consultation between a doctor and patient.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='consultations')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='consultations')
    notes = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation with {self.patient.first_name} {self.patient.last_name} by {self.doctor.user.username}"

