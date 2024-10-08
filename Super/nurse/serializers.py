from rest_framework import serializers
from .models import PatientCare
from patients.models import Patient

class PatientCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCare
        fields = ['id', 'patient', 'nurse', 'observations', 'date']


