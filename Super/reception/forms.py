# reception/forms.py

from django import forms
from .models import ReceptionPatient

class PatientRegistrationForm(forms.ModelForm):
    """
    Form for registering new patients.
    """
    class Meta:
        model = ReceptionPatient
        fields = ['first_name', 'last_name', 'dob', 'medical_history', 'current_department']