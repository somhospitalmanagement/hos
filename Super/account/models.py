from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from hospital.models import Hospital, Department


class UserType(models.Model):
    """
    Model to define user types (e.g., Doctor, Pharmacist, etc.).
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    """
    Extends the built-in user model to include hospital and user type.
    """
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name='users',
        null=True,
        blank=True
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )
    user_type = models.ForeignKey(
        UserType,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ('hospital', 'username')

    def __str__(self):
        return f"{self.username} ({self.user_type.name if self.user_type else 'No user type'})"

    def clean(self):
        # Ensure the user belongs to a department within the selected hospital
        if self.department and self.hospital and self.department.hospital != self.hospital:
            raise ValidationError(f"{self.department.name} does not belong to {self.hospital.name}.")
        if not self.user_type:
            raise ValidationError('User type must be specified.')




