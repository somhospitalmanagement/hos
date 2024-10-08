# lab/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LabTestViewSet

router = DefaultRouter()
router.register(r'lab-tests', LabTestViewSet, basename='lab-test')

urlpatterns = [
    path('', include(router.urls)),
]
