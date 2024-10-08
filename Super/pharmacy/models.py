from django.db import models
from hospital.models import Hospital, Department
from django.contrib.auth.models import User
from patients.models import Patient
from django.conf import settings
class Pharmacist(models.Model):
    """
    Model to represent pharmacists associated with a hospital.
    Each pharmacist is a user type that belongs to a department.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='pharmacists')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='pharmacyists')

    def __str__(self):
        return f"{self.user.username} - Pharmacist"

class Prescription(models.Model):
    """
    Model to represent prescriptions made for patients.
    This links the pharmacist with the patient and includes medicine details.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE, related_name='prescriptions')
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField(blank=True, null=True)
    date_prescribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.user.username} by {self.pharmacist.user.username}"
