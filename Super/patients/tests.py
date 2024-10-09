from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from hospital.models import Hospital, Department
from .models import Patient, MedicalRecord
from .serializers import PatientSerializer, MedicalRecordSerializer
from .forms import PatientUpdateForm

class PatientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        cls.department = Department.objects.create(name="Test Department", hospital=cls.hospital)
        cls.patient = Patient.objects.create(
            first_name="John",
            last_name="Doe",
            dob=timezone.now().date() - timedelta(days=365*30),
            hospital=cls.hospital,
            current_department=cls.department
        )

    def test_patient_creation(self):
        self.assertTrue(isinstance(self.patient, Patient))
        self.assertEqual(str(self.patient), "John Doe - Patient")

    def test_patient_fields(self):
        self.assertEqual(self.patient.first_name, "John")
        self.assertEqual(self.patient.last_name, "Doe")
        self.assertEqual(self.patient.hospital, self.hospital)
        self.assertEqual(self.patient.current_department, self.department)

class MedicalRecordModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        cls.patient = Patient.objects.create(
            first_name="John",
            last_name="Doe",
            dob=timezone.now().date() - timedelta(days=365*30),
            hospital=cls.hospital
        )
        cls.medical_record = MedicalRecord.objects.create(
            patient=cls.patient,
            details="Test medical record"
        )

    def test_medical_record_creation(self):
        self.assertTrue(isinstance(self.medical_record, MedicalRecord))
        self.assertEqual(str(self.medical_record), f"Record for John Doe - Patient on {self.medical_record.record_date}")

    def test_medical_record_fields(self):
        self.assertEqual(self.medical_record.patient, self.patient)
        self.assertEqual(self.medical_record.details, "Test medical record")

class PatientSerializerTest(TestCase):
    def setUp(self):
        self.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        self.department = Department.objects.create(name="Test Department", hospital=self.hospital)

    def test_patient_serializer(self):
        patient_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'dob': timezone.now().date() - timedelta(days=365*25),
            'hospital': self.hospital.id,
            'current_department': self.department.id
        }
        serializer = PatientSerializer(data=patient_data)
        self.assertTrue(serializer.is_valid())

class MedicalRecordSerializerTest(TestCase):
    def setUp(self):
        self.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        self.patient = Patient.objects.create(
            first_name="John",
            last_name="Doe",
            dob=timezone.now().date() - timedelta(days=365*30),
            hospital=self.hospital
        )

    def test_medical_record_serializer(self):
        medical_record_data = {
            'patient': self.patient.id,
            'details': 'Test medical record details'
        }
        serializer = MedicalRecordSerializer(data=medical_record_data)
        self.assertTrue(serializer.is_valid())

class PatientUpdateFormTest(TestCase):
    def setUp(self):
        self.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        self.department = Department.objects.create(name="Test Department", hospital=self.hospital)

    def test_valid_form(self):
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'dob': timezone.now().date() - timedelta(days=365*25),
            'medical_history': 'None',
            'current_department': self.department.id
        }
        form = PatientUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_dob(self):
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'dob': timezone.now().date() + timedelta(days=1),
            'medical_history': 'None',
            'current_department': self.department.id
        }
        form = PatientUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('dob', form.errors)
        
