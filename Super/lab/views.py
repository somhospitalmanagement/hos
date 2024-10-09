# Super/lab/views.py

from rest_framework import viewsets
from .models import LabTest
from .serializers import LabTestSerializer
from rest_framework.permissions import IsAuthenticated

class LabTestViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer
    permission_classes = [IsAuthenticated]

