# Super/patients/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, MedicalRecord
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PatientUpdateForm
from .serializers import MedicalRecordSerializer
from django.http import JsonResponse
import json

@login_required
def patient_list(request):
    """
    View to list all patients associated with the logged-in user's hospital.
    """
    patients = Patient.objects.filter(hospital=request.user.hospital)
    return render(request, 'patients/patient_list.html', {'patients': patients})

@login_required
def patient_detail(request, patient_id):
    """
    View to display details of a specific patient.
    """
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

@login_required
def patient_update(request, patient_id):
    """
    View to update patient information.
    """
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient information updated successfully.')
            return redirect('patient_detail', patient_id=patient.id)
    else:
        form = PatientUpdateForm(instance=patient)

    return render(request, 'patients/patient_update.html', {'form': form, 'patient': patient})

@login_required
def patient_delete(request, patient_id):
    """
    View to delete a patient.
    """
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient deleted successfully.')
        return redirect('patient_list')

    return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})

def create_medical_record(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = MedicalRecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Medical record created successfully!', 'record': serializer.data}, status=201)
        return JsonResponse({'errors': serializer.errors}, status=400)

def retrieve_medical_records(request):
    records = MedicalRecord.objects.all()
    serializer = MedicalRecordSerializer(records, many=True)
    return JsonResponse(serializer.data, safe=False)