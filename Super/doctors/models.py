from django.db import models
from hospital.models import Hospital, Department
from django.contrib.auth.models import User  # Use your CustomUser if needed
from patients.models import Patient
from django.conf import settings
class Doctor(models.Model):
    """
    Model to represent doctors associated with a hospital.
    Each doctor is a user type that belongs to a department.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # or CustomUser
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')

    def __str__(self):
        return f"{self.user.username} - Doctor"

class Consultation(models.Model):
    """
    Model to represent a consultation between a patient and a doctor.
    This records details of the patient visit and any updates.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='consultations')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='consultations')
    notes = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation with {self.patient.user.username} by {self.doctor.user.username}"

