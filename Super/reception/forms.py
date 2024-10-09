# reception/forms.py

from django import forms
from patients.models import Patient

class PatientRegistrationForm(forms.ModelForm):
    """
    Form for registering new patients.
    """
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'dob', 'medical_history', 'hospital']
