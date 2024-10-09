from django.db import models
from hospital.models import Hospital, Department
from django.conf import settings
from patients.models import Patient
from django.core.exceptions import ValidationError

class Pharmacist(models.Model):
    """
    Model to represent pharmacists associated with a hospital and department.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='pharmacists')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='pharmacists')

    def __str__(self):
        return f"{self.user.username} - Pharmacist"

    def clean(self):
        if self.department.hospital != self.hospital:
            raise ValidationError(f"{self.department.name} is not a department of {self.hospital.name}.")


class MedicineInventory(models.Model):
    """
    Model to represent medicine inventory in the pharmacy.
    """
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='medicine_inventory')
    medicine_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.medicine_name} - {self.quantity} {self.unit} at {self.hospital.name}"

    class Meta:
        unique_together = ['hospital', 'medicine_name']

# Update the Prescription model
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.SET_NULL, null=True)
    medicine_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    fulfilled = models.BooleanField(default=False)

    def fulfill(self):
        if not self.fulfilled:
            inventory = MedicineInventory.objects.get(
                hospital=self.pharmacist.hospital,
                medicine_name=self.medicine_name
            )
            if inventory.quantity >= self.quantity:
                inventory.quantity -= self.quantity
                inventory.save()
                self.fulfilled = True
                self.save()
            else:
                raise ValidationError("Not enough medicine in inventory.")

    def __str__(self):
        return f"Prescription for {self.patient.first_name} {self.patient.last_name} by {self.pharmacist.user.username}"