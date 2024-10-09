<<<<<<< HEAD
# reception/views.py

=======
>>>>>>> f6967acb9d9876b25d83f85b103629027b0e82ca
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
<<<<<<< HEAD
            # Set the hospital from the request or user context
            patient.hospital = request.user.hospital  # Assuming the user has a hospital attribute
=======
            patient.hospital = request.user.hospital  # Associate with the logged-in user's hospital
>>>>>>> f6967acb9d9876b25d83f85b103629027b0e82ca
            patient.save()
            return JsonResponse({'message': 'Patient registered successfully!', 'patient_id': patient.id}, status=201)
        return JsonResponse({'errors': form.errors}, status=400)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

<<<<<<< HEAD
def retrieve_patients(request):
    """
    View to retrieve and return a list of patients as JSON.
    """
    patients = Patient.objects.all().values('first_name', 'last_name', 'dob', 'hospital__name', 'medical_history') 
    return JsonResponse(list(patients), safe=False)
=======
>>>>>>> f6967acb9d9876b25d83f85b103629027b0e82ca
