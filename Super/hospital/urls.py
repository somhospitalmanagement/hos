from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HospitalViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


