# Super/hospital/views.py

from rest_framework import viewsets
from .models import Hospital, Department
from .serializers import HospitalSerializer, DepartmentSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from django.views.decorators.cache import cache_page


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticated]

    @cache_page(60 * 15)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        cache_key = f'hospital_{kwargs["pk"]}'
        hospital = cache.get(cache_key)
        if not hospital:
            hospital = super().retrieve(request, *args, **kwargs)
            cache.set(cache_key, hospital, timeout=60*15)
        return hospital

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]



