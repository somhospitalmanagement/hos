from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import ReceptionPatient, Hospital, Department
from .forms import PatientRegistrationForm

class PatientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        cls.department = Department.objects.create(name="Test Department", hospital=cls.hospital)
        cls.patient = ReceptionPatient.objects.create(
            first_name="John",
            last_name="Doe",
            dob=timezone.now().date() - timedelta(days=365*30),
            hospital=cls.hospital,
            current_department=cls.department
        )

    def test_patient_creation(self):
        self.assertTrue(isinstance(self.patient, ReceptionPatient))
        self.assertEqual(str(self.patient), "John Doe - Reception Patient")

    def test_patient_fields(self):
        self.assertEqual(self.patient.first_name, "John")
        self.assertEqual(self.patient.last_name, "Doe")
        self.assertEqual(self.patient.hospital, self.hospital)
        self.assertEqual(self.patient.current_department, self.department)

class PatientRegistrationFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        cls.department = Department.objects.create(name="Test Department", hospital=cls.hospital)

    def test_valid_form(self):
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'dob': timezone.now().date() - timedelta(days=365*25),
            'medical_history': 'None',
            'current_department': self.department.id
        }
        form = PatientRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_first_name(self):
        form_data = {
            'first_name': 'Jane123',
            'last_name': 'Doe',
            'dob': timezone.now().date() - timedelta(days=365*25),
            'medical_history': 'None',
            'current_department': self.department.id
        }
        form = PatientRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

    def test_future_dob(self):
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'dob': timezone.now().date() + timedelta(days=1),
            'medical_history': 'None',
            'current_department': self.department.id
        }
        form = PatientRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('dob', form.errors)