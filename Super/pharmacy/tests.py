from django.test import TestCase
from django.contrib.auth import get_user_model
from hospital.models import Hospital, Department
from patients.models import Patient
from .models import Pharmacist, MedicineInventory, Prescription
from .serializers import PrescriptionSerializer, MedicineInventorySerializer

User = get_user_model()

class PharmacistModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        cls.department = Department.objects.create(name="Pharmacy", hospital=cls.hospital)
        cls.user = User.objects.create_user(username="testpharmacist", password="testpass")
        cls.pharmacist = Pharmacist.objects.create(user=cls.user, department=cls.department, hospital=cls.hospital)

    def test_pharmacist_creation(self):
        self.assertTrue(isinstance(self.pharmacist, Pharmacist))
        self.assertEqual(str(self.pharmacist), "testpharmacist - Pharmacist")

    def test_pharmacist_fields(self):
        self.assertEqual(self.pharmacist.user, self.user)
        self.assertEqual(self.pharmacist.department, self.department)
        self.assertEqual(self.pharmacist.hospital, self.hospital)

class MedicineInventoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        cls.medicine = MedicineInventory.objects.create(
            hospital=cls.hospital,
            medicine_name="Test Medicine",
            quantity=100,
            unit="tablets"
        )

    def test_medicine_inventory_creation(self):
        self.assertTrue(isinstance(self.medicine, MedicineInventory))
        self.assertEqual(str(self.medicine), "Test Medicine - 100 tablets at Test Hospital")

    def test_medicine_inventory_fields(self):
        self.assertEqual(self.medicine.hospital, self.hospital)
        self.assertEqual(self.medicine.medicine_name, "Test Medicine")
        self.assertEqual(self.medicine.quantity, 100)
        self.assertEqual(self.medicine.unit, "tablets")

class PrescriptionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        cls.department = Department.objects.create(name="Pharmacy", hospital=cls.hospital)
        cls.pharmacist_user = User.objects.create_user(username="testpharmacist", password="testpass")
        cls.pharmacist = Pharmacist.objects.create(user=cls.pharmacist_user, department=cls.department, hospital=cls.hospital)
        cls.patient = Patient.objects.create(first_name="John", last_name="Doe", hospital=cls.hospital)
        cls.prescription = Prescription.objects.create(
            patient=cls.patient,
            pharmacist=cls.pharmacist,
            medicine_name="Test Medicine",
            quantity=30,
            fulfilled=False
        )

    def test_prescription_creation(self):
        self.assertTrue(isinstance(self.prescription, Prescription))
        self.assertEqual(str(self.prescription), f"Prescription for John Doe by testpharmacist")

    def test_prescription_fields(self):
        self.assertEqual(self.prescription.patient, self.patient)
        self.assertEqual(self.prescription.pharmacist, self.pharmacist)
        self.assertEqual(self.prescription.medicine_name, "Test Medicine")
        self.assertEqual(self.prescription.quantity, 30)
        self.assertFalse(self.prescription.fulfilled)

class PrescriptionSerializerTest(TestCase):
    def setUp(self):
        self.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")
        self.department = Department.objects.create(name="Pharmacy", hospital=self.hospital)
        self.pharmacist_user = User.objects.create_user(username="testpharmacist", password="testpass")
        self.pharmacist = Pharmacist.objects.create(user=self.pharmacist_user, department=self.department, hospital=self.hospital)
        self.patient = Patient.objects.create(first_name="John", last_name="Doe", hospital=self.hospital)

    def test_prescription_serializer(self):
        prescription_data = {
            'patient': self.patient.id,
            'pharmacist': self.pharmacist.id,
            'medicine_name': 'Test Medicine',
            'quantity': 30,
            'fulfilled': False
        }
        serializer = PrescriptionSerializer(data=prescription_data)
        self.assertTrue(serializer.is_valid())

class MedicineInventorySerializerTest(TestCase):
    def setUp(self):
        self.hospital = Hospital.objects.create(name="Test Hospital", address="123 Test St", phone_number="1234567890")

    def test_medicine_inventory_serializer(self):
        inventory_data = {
            'hospital': self.hospital.id,
            'medicine_name': 'Test Medicine',
            'quantity': 100,
            'unit': 'tablets'
        }
        serializer = MedicineInventorySerializer(data=inventory_data)
        self.assertTrue(serializer.is_valid())