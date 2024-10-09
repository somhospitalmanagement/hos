# Super/reception/views.py

from django.http import JsonResponse
from .forms import PatientRegistrationForm
from .models import ReceptionPatient
from .serializers import ReceptionPatientSerializer
import json

def register_patient(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = PatientRegistrationForm(data)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.hospital = request.user.hospital  # Set the hospital from the logged-in user
            patient.save()
            serializer = ReceptionPatientSerializer(patient)  # Use the serializer
            return JsonResponse({'message': 'Patient registered successfully!', 'patient': serializer.data}, status=201)
        return JsonResponse({'errors': form.errors}, status=400)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def retrieve_patients(request):
    """
    View to retrieve and return a list of patients as JSON.
    """
    patients = ReceptionPatient.objects.all()
    serializer = ReceptionPatientSerializer(patients, many=True)  # Use the serializer
    return JsonResponse(serializer.data, safe=False)