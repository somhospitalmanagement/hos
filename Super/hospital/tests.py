from django.test import TestCase
from .models import Hospital, Department
from .serializers import HospitalSerializer, DepartmentSerializer

class HospitalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(
            name="Test Hospital",
            address="123 Test St",
            phone_number="1234567890"
        )

    def test_hospital_creation(self):
        self.assertTrue(isinstance(self.hospital, Hospital))
        self.assertEqual(str(self.hospital), "Test Hospital")

    def test_hospital_fields(self):
        self.assertEqual(self.hospital.name, "Test Hospital")
        self.assertEqual(self.hospital.address, "123 Test St")
        self.assertEqual(self.hospital.phone_number, "1234567890")

class DepartmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(
            name="Test Hospital",
            address="123 Test St",
            phone_number="1234567890"
        )
        cls.department = Department.objects.create(
            name="Test Department",
            hospital=cls.hospital
        )

    def test_department_creation(self):
        self.assertTrue(isinstance(self.department, Department))
        self.assertEqual(str(self.department), "Test Department - Test Hospital")

    def test_department_fields(self):
        self.assertEqual(self.department.name, "Test Department")
        self.assertEqual(self.department.hospital, self.hospital)

class HospitalSerializerTest(TestCase):
    def test_hospital_serializer(self):
        hospital_data = {
            'name': 'New Hospital',
            'address': '456 New St',
            'phone_number': '9876543210'
        }
        serializer = HospitalSerializer(data=hospital_data)
        self.assertTrue(serializer.is_valid())

class DepartmentSerializerTest(TestCase):
    def setUp(self):
        self.hospital = Hospital.objects.create(
            name="Test Hospital",
            address="123 Test St",
            phone_number="1234567890"
        )

    def test_department_serializer(self):
        department_data = {
            'name': 'New Department',
            'hospital': self.hospital.id
        }
        serializer = DepartmentSerializer(data=department_data)
        self.assertTrue(serializer.is_valid())