# reception/urls.py

from django.urls import path
from .views import register_patient, retrieve_patients

urlpatterns = [
    path('register/', register_patient, name='register_patient'),
    path('patients/', retrieve_patients, name='retrieve_patients'),
]
