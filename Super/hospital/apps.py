from django.apps import AppConfig

class HospitalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hospital'

    def ready(self):
        import hospital.signal  # Import the signals to make them active
