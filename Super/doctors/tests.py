from django.test import TestCase
from django.contrib.auth import get_user_model
from hospital.models import Hospital, Department
from .models import Doctor, Consultation
from patients.models import Patient
from .serializers import ConsultationSerializer

User = get_user_model()

class DoctorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        cls.department = Department.objects.create(name="Test Department", hospital=cls.hospital)
        cls.user = User.objects.create_user(username="testdoctor", password="testpass")
        cls.doctor = Doctor.objects.create(user=cls.user, department=cls.department, hospital=cls.hospital)

    def test_doctor_creation(self):
        self.assertTrue(isinstance(self.doctor, Doctor))
        self.assertEqual(str(self.doctor), "Dr. testdoctor")

    def test_doctor_fields(self):
        self.assertEqual(self.doctor.user, self.user)
        self.assertEqual(self.doctor.department, self.department)
        self.assertEqual(self.doctor.hospital, self.hospital)

class ConsultationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        cls.department = Department.objects.create(name="Test Department", hospital=cls.hospital)
        cls.doctor_user = User.objects.create_user(username="testdoctor", password="testpass")
        cls.doctor = Doctor.objects.create(user=cls.doctor_user, department=cls.department, hospital=cls.hospital)
        cls.patient = Patient.objects.create(first_name="John", last_name="Doe", hospital=cls.hospital)
        cls.consultation = Consultation.objects.create(patient=cls.patient, doctor=cls.doctor, notes="Test consultation")

    def test_consultation_creation(self):
        self.assertTrue(isinstance(self.consultation, Consultation))
        self.assertEqual(str(self.consultation), f"Consultation with John Doe by testdoctor")

    def test_consultation_fields(self):
        self.assertEqual(self.consultation.patient, self.patient)
        self.assertEqual(self.consultation.doctor, self.doctor)
        self.assertEqual(self.consultation.notes, "Test consultation")

class ConsultationSerializerTest(TestCase):
    def setUp(self):
        self.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        self.department = Department.objects.create(name="Test Department", hospital=self.hospital)
        self.doctor_user = User.objects.create_user(username="testdoctor", password="testpass")
        self.doctor = Doctor.objects.create(user=self.doctor_user, department=self.department, hospital=self.hospital)
        self.patient = Patient.objects.create(first_name="John", last_name="Doe", hospital=self.hospital)

    def test_consultation_serializer(self):
        consultation_data = {
            'patient': self.patient.id,
            'doctor': self.doctor.id,
            'notes': 'Test consultation notes'
        }
        serializer = ConsultationSerializer(data=consultation_data)
        self.assertTrue(serializer.is_valid())