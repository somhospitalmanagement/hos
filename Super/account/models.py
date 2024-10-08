from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from hospital.models import Hospital


class UserType(models.Model):
    """
    Model to define user types within a hospital.
    This allows hospitals to easily add new user types.
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name='users',
        null=True,
        blank=True
    )
    user_type = models.ForeignKey(
        UserType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        unique_together = ('hospital', 'username')

    def __str__(self):
        return f"{self.username} ({self.user_type.name if self.user_type else 'No user type'})"

    def clean(self):
        
        if not self.user_type:
            raise ValidationError('User type must be specified.')





