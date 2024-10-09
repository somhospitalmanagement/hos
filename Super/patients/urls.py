# Super/patients/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('patient/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('patient/<int:patient_id>/update/', views.patient_update, name='patient_update'),
    path('patient/<int:patient_id>/delete/', views.patient_delete, name='patient_delete'),
    path('medical-records/', views.create_medical_record, name='create_medical_record'),
    path('medical-records/list/', views.retrieve_medical_records, name='retrieve_medical_records'),
]
