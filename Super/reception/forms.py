from django import forms
from .models import ReceptionPatient
from django.utils import timezone

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = ReceptionPatient
        fields = ['first_name', 'last_name', 'dob', 'medical_history', 'current_department']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError("First name should only contain letters.")
        return first_name

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if dob and dob > timezone.now().date():
            raise forms.ValidationError("Date of birth cannot be in the future.")
        return dob