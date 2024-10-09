from django.http import JsonResponse
from .forms import PatientRegistrationForm
from patients.models import Patient
import json

def register_patient(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = PatientRegistrationForm(data)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.hospital = request.user.hospital  # Associate with the logged-in user's hospital
            patient.save()
            return JsonResponse({'message': 'Patient registered successfully!', 'patient_id': patient.id}, status=201)
        return JsonResponse({'errors': form.errors}, status=400)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

