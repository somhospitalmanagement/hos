# patients/forms.py
from django import forms
from .models import Patient

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'dob', 'current_department', 'medical_history']