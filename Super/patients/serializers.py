from rest_framework import serializers
from .models import Patient
from hospital.models import Hospital

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'hospital', 'medical_history', 'current_department']

class PatientRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['user', 'hospital', 'medical_history', 'current_department']
