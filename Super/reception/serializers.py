# Super/reception/serializers.py

from rest_framework import serializers
from .models import Reception, ReceptionPatient, Appointment

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
        read_only_fields = ['registration_date', 'hospital']

class AppointmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Appointment model.
    """
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'appointment_date', 'notes']