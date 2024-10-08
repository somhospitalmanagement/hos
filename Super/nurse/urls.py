# patient_care/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientCareViewSet

router = DefaultRouter()
router.register(r'patient-care', PatientCareViewSet, basename='patient-care')
urlpatterns = [
    path('', include(router.urls)), 
]
