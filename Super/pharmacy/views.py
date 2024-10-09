from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .models import Prescription, MedicineInventory
from .serializers import PrescriptionSerializer, MedicineInventorySerializer
from django.core.exceptions import ValidationError

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    @action(detail=True, methods=['post'])
    def fulfill(self, request, pk=None):
        prescription = self.get_object()
        try:
            prescription.fulfill()
            return Response({'status': 'prescription fulfilled'})
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class MedicineInventoryViewSet(viewsets.ModelViewSet):
    queryset = MedicineInventory.objects.all()
    serializer_class = MedicineInventorySerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    @action(detail=False, methods=['post'])
    def add_stock(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            medicine, created = MedicineInventory.objects.get_or_create(
                hospital=serializer.validated_data['hospital'],
                medicine_name=serializer.validated_data['medicine_name'],
                defaults={'quantity': 0, 'unit': serializer.validated_data['unit']}
            )
            medicine.quantity += serializer.validated_data['quantity']
            medicine.save()
            return Response({'status': 'stock added'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)