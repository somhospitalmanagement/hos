# Super/hospital/views.py

from rest_framework import viewsets
from .models import Hospital, Department
from .serializers import HospitalSerializer, DepartmentSerializer
from rest_framework.permissions import IsAuthenticated

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticated]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]



