# Super/nurse/views.py

from rest_framework import viewsets
from .models import PatientCare
from .serializers import PatientCareSerializer
from rest_framework.permissions import IsAuthenticated

class PatientCareViewSet(viewsets.ModelViewSet):
    queryset = PatientCare.objects.all()
    serializer_class = PatientCareSerializer
    permission_classes = [IsAuthenticated]
