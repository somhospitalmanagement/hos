# doctors/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultationViewSet

router = DefaultRouter()
router.register(r'consultations', ConsultationViewSet, basename='consultation')  # Register the ViewSet

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]
