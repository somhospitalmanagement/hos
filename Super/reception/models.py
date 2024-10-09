# Super/reception/models.py

from django.db import models
from hospital.models import Hospital
from django.conf import settings
from patients.models import Patient
from hospital.models import Hospital, Department


class Reception(models.Model):
    """
    Model to represent patients registered at the reception.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reception_patients')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='reception_patients')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='reception')

    def __str__(self):
        return f"{self.user.username} - Reception Patient"

class ReceptionPatient(Patient):
    """
    Model to represent patients registered at the reception.
    Inherits from the Patient model in the patients app.
    """
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Reception Patient"

class Appointment(models.Model):
    """
    Model to represent appointments for patients.
    """
    patient = models.ForeignKey(ReceptionPatient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type__name': 'Doctor'})
    appointment_date = models.DateTimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.appointment_date}"