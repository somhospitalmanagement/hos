from django.db import models
from hospital.models import Hospital, Department
from django.contrib.auth.models import User 
from patients.models import Patient
from django.conf import settings
class LabTechnician(models.Model):
    """
    Model to represent lab technicians associated with a hospital.
    Each technician is a user type that belongs to a department.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='lab_technicians')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='lab_technicians')

    def __str__(self):
        return f"{self.user.username} - Lab Technician"

class LabTest(models.Model):
    """
    Model to represent lab tests conducted for patients.
    This links back to the patient and includes test results.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='lab_tests')
    test_type = models.CharField(max_length=255)
    results = models.TextField(blank=True, null=True)
    date_conducted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Test: {self.test_type} for {self.patient.user.username}"


