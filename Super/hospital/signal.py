from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Hospital, Department

# Predefined list of department names
DEFAULT_DEPARTMENTS = ['nurse', 'pharmacy', 'lab', 'reception', 'doctor']

@receiver(post_save, sender=Hospital)
def create_departments(sender, instance, created, **kwargs):
    """
    Signal to automatically create departments for each new hospital.
    """
    if created:
        # When a new hospital is created, add default departments
        for department_name in DEFAULT_DEPARTMENTS:
            Department.objects.create(name=department_name, hospital=instance)
