from rest_framework import serializers
from .models import LabTest
from patients.models import Patient

class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = ['id', 'patient', 'test_type', 'results', 'date_conducted']

