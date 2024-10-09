# reception/forms.py

from django import forms
from .models import ReceptionPatient  # Import the ReceptionPatient model

class PatientRegistrationForm(forms.ModelForm):
    """
    Form for registering new patients.
    """
    class Meta:
        model = ReceptionPatient  # Use ReceptionPatient instead of Patient
        fields = ['first_name', 'last_name', 'dob', 'medical_history', 'current_department']