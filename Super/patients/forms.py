from django import forms
from django.utils import timezone
from .models import Patient

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'dob', 'current_department', 'medical_history']

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if dob and dob > timezone.now().date():
            raise forms.ValidationError("Date of birth cannot be in the future.")
        return dob