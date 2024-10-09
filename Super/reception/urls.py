# Super/reception/urls.py

from django.urls import path
from .views import register_patient, retrieve_patients, create_appointment, retrieve_appointments

urlpatterns = [
    path('register/', register_patient, name='register_patient'),
    path('patients/', retrieve_patients, name='retrieve_patients'),
    path('appointments/', create_appointment, name='create_appointment'),
    path('appointments/list/', retrieve_appointments, name='retrieve_appointments'),
]
