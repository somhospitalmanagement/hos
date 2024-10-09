from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Hospital, Department


DEFAULT_DEPARTMENTS = ['nurse', 'pharmacy', 'lab', 'reception', 'doctor']

@receiver(post_save, sender=Hospital)
def create_departments(sender, instance, created, **kwargs):
    """
    Signal to automatically create departments for each new hospital.
    """
    if created:
        
        for department_name in DEFAULT_DEPARTMENTS:
            Department.objects.create(name=department_name, hospital=instance)
