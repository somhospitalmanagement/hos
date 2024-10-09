from django.test import TestCase
from django.contrib.auth import get_user_model
from hospital.models import Hospital, Department
from patients.models import Patient
from .models import LabTest
from .serializers import LabTestSerializer

User = get_user_model()

class LabTestModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        cls.department = Department.objects.create(name="Lab", hospital=cls.hospital)
        cls.patient = Patient.objects.create(first_name="John", last_name="Doe", hospital=cls.hospital)
        cls.lab_technician = User.objects.create_user(username="labtechnician", password="testpass")
        cls.lab_test = LabTest.objects.create(
            patient=cls.patient,
            test_name="Blood Test",
            test_result="Normal",
            conducted_by=cls.lab_technician
        )

    def test_lab_test_creation(self):
        self.assertTrue(isinstance(self.lab_test, LabTest))
        self.assertEqual(str(self.lab_test), f"Blood Test for John Doe")

    def test_lab_test_fields(self):
        self.assertEqual(self.lab_test.patient, self.patient)
        self.assertEqual(self.lab_test.test_name, "Blood Test")
        self.assertEqual(self.lab_test.test_result, "Normal")
        self.assertEqual(self.lab_test.conducted_by, self.lab_technician)

class LabTestSerializerTest(TestCase):
    def setUp(self):
        self.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        self.patient = Patient.objects.create(first_name="John", last_name="Doe", hospital=self.hospital)
        self.lab_technician = User.objects.create_user(username="labtechnician", password="testpass")

    def test_lab_test_serializer(self):
        lab_test_data = {
            'patient': self.patient.id,
            'test_name': 'Blood Test',
            'test_result': 'Normal',
            'conducted_by': self.lab_technician.id
        }
        serializer = LabTestSerializer(data=lab_test_data)
        self.assertTrue(serializer.is_valid())