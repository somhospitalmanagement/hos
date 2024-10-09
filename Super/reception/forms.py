# reception/forms.py

from django import forms
from patients.models import Patient

class PatientRegistrationForm(forms.ModelForm):
    """
    Form for registering new patients.
    """
    class Meta:
        model = Patient
<<<<<<< HEAD
        fields = ['first_name', 'last_name', 'dob', 'medical_history', 'current_department']
=======
        fields = ['first_name', 'last_name', 'dob', 'medical_history', 'hospital']
>>>>>>> f6967acb9d9876b25d83f85b103629027b0e82ca
