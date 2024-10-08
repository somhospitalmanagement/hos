from rest_framework import serializers
from .models import Consultation
from patients.models import Patient

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['id', 'patient', 'doctor', 'notes', 'date']

