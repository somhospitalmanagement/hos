from django.db import models
from hospital.models import Hospital, Department
from patients.models import Patient
from django.conf import settings
from django.core.exceptions import ValidationError


class Nurse(models.Model):
    """
    Model to represent nurses associated with a hospital and department.
    Each nurse is a user type that belongs to a department and a hospital.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='nurses')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='nurses')

    def __str__(self):
        return f"{self.user.username} - Nurse"

    def clean(self):
        # Ensure the department belongs to the nurse's hospital
        if self.department.hospital != self.hospital:
            raise ValidationError(f"Department {self.department.name} does not belong to {self.hospital.name}.")
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class PatientCare(models.Model):
    """
    Model to represent the care provided by nurses to patients.
    This includes observations and updates on the patient's condition.
    Nurses must belong to the same hospital as the patient.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='nurse_care')
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name='patient_care')
    observations = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Care for {self.patient.user.username} by {self.nurse.user.username}"

    def clean(self):
        
        if self.nurse.hospital != self.patient.hospital:
            raise ValidationError(f"Nurse {self.nurse.user.username} does not work at {self.patient.hospital.name}.")
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


