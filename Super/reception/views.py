# reception/views.py

from django.http import JsonResponse
from .forms import PatientRegistrationForm
from .models import ReceptionPatient  # Import the ReceptionPatient model
import json

def register_patient(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = PatientRegistrationForm(data)
        if form.is_valid():
            patient = form.save(commit=False)
            # Set the hospital from the request or user context
            patient.hospital = request.user.hospital  # Assuming the user has a hospital attribute
            patient.save()
            return JsonResponse({'message': 'Patient registered successfully!', 'patient_id': patient.id}, status=201)
        return JsonResponse({'errors': form.errors}, status=400)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def retrieve_patients(request):
    """
    View to retrieve and return a list of patients as JSON.
    """
    patients = ReceptionPatient.objects.all().values('first_name', 'last_name', 'dob', 'hospital__name', 'medical_history') 
    return JsonResponse(list(patients), safe=False)
