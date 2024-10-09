

from rest_framework import serializers
from .models import Reception, ReceptionPatient

class ReceptionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Reception model.
    """
    class Meta:
        model = Reception
        fields = ['user', 'hospital']

class ReceptionPatientSerializer(serializers.ModelSerializer):
    """
    Serializer for the ReceptionPatient model.
    """
    class Meta:
        model = ReceptionPatient
        fields = ['id', 'first_name', 'last_name', 'dob', 'medical_history', 'current_department', 'registration_date', 'hospital']
        read_only_fields = ['registration_date', 'hospital']  # Make registration_date and hospital read-only