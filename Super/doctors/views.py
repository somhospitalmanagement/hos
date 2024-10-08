from rest_framework import viewsets
from .models import Consultation
from .serializers import ConsultationSerializer
from rest_framework.permissions import IsAuthenticated

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]




