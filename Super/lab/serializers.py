from rest_framework import serializers
from .models import LabTest

class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = ['id', 'patient', 'test_name', 'test_result', 'conducted_by', 'date_conducted']

