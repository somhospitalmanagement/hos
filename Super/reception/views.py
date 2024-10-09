# Super/reception/views.py

from django.http import JsonResponse
from .forms import PatientRegistrationForm
from .models import Appointment, ReceptionPatient
from .serializers import ReceptionPatientSerializer, AppointmentSerializer
import json

def register_patient(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = PatientRegistrationForm(data)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.hospital = request.user.hospital
            patient.save()
            serializer = ReceptionPatientSerializer(patient)
            return JsonResponse({'message': 'Patient registered successfully!', 'patient': serializer.data}, status=201)
        return JsonResponse({'errors': form.errors}, status=400)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def retrieve_patients(request):
    """
    View to retrieve and return a list of patients as JSON.
    """
    patients = ReceptionPatient.objects.all()
    serializer = ReceptionPatientSerializer(patients, many=True)
    return JsonResponse(serializer.data, safe=False)

def create_appointment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = AppointmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Appointment created successfully!', 'appointment': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)

def retrieve_appointments(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return JsonResponse(serializer.data, safe=False)