from django.urls import path
from .views import (
    hospital_login,
    list_users_by_role,
    hospital_detail,
    logout_user
)

urlpatterns = [
    path('login/', hospital_login, name='hospital_login'),
    path('users/', list_users_by_role, name='list_users_by_role'),
    path('hospital/<int:pk>/', hospital_detail, name='hospital_detail'),
    path('logout/', logout_user, name='logout_user'),
]

