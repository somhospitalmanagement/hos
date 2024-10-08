from rest_framework import viewsets
from .models import Prescription
from .serializers import PrescriptionSerializer
from rest_framework.permissions import IsAuthenticated

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
