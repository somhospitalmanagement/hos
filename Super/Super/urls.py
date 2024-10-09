
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hospital.urls')),
    path('api/', include('patients.urls')),
    path('api/', include('doctors.urls')),
    path('api/', include('lab.urls')),
    path('api/', include('pharmacy.urls')),
    path('api/', include('nurse.urls')),
    path('api/', include('account.urls')),
    path('api/', include('reception.urls')),
    path('analytics/', include('analytics.urls')),
]




