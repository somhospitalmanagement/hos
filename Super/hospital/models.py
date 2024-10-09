from django.db import models

class Hospital(models.Model):
    """
    Model to represent a hospital.
    """
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    Model to represent departments within a hospital.
    """
    name = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return f"{self.name} - {self.hospital.name}"

