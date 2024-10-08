from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer, PatientRegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = PatientRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
