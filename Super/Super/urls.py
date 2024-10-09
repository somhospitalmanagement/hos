# urls.py (main project)
from django.contrib import admin  # Import the admin module
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Include the admin URLs
    path('api/', include('hospital.urls')),  # Include hospitals URLs
    path('api/', include('patients.urls')),   # Include patients URLs
    path('api/', include('doctors.urls')),    # Include doctors URLs
    path('api/', include('lab.urls')),         # Include lab URLs
    path('api/', include('pharmacy.urls')),    # Include pharmacy URLs
    path('api/', include('nurse.urls')),
    path('api/', include('account.urls')),
    path('api/', include('reception.urls')),   # Include nurse URLs
]




