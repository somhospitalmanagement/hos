from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrescriptionViewSet, MedicineInventoryViewSet

router = DefaultRouter()
router.register(r'prescriptions', PrescriptionViewSet, basename='prescription')
router.register(r'medicine-inventory', MedicineInventoryViewSet, basename='medicine-inventory')

urlpatterns = [
    path('', include(router.urls)),
]
