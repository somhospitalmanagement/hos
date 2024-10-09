# patients/models.py

from django.db import models
from hospital.models import Hospital, Department
from django.core.exceptions import ValidationError
from django.utils import timezone

class Patient(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='patients')
    medical_history = models.TextField(blank=True, null=True)
    current_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='current_patients')
    dob = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) 
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Patient"
