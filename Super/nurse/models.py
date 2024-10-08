from django.db import models
from hospital.models import Hospital, Department
from django.contrib.auth.models import User
from patients.models import Patient
from django.conf import settings
class Nurse(models.Model):
    """
    Model to represent nurses associated with a hospital.
    Each nurse is a user type that belongs to a department.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='nurses')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='nurses')

    def __str__(self):
        return f"{self.user.username} - Nurse"

class PatientCare(models.Model):
    """
    Model to represent the care provided by nurses to patients.
    This includes observations and updates on the patient's condition.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='nurse_care')
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='patient_care')
    observations = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Care for {self.patient.user.username} by {self.nurse.user.username}"

