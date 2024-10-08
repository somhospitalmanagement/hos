from rest_framework import serializers
from .models import Prescription
from patients.models import Patient

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['id', 'patient', 'pharmacist', 'medicine_name', 'dosage', 'instructions', 'date_prescribed']
