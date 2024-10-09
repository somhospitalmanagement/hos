# Super/account/urls.py

from django.urls import path
from .views import (
    admin_login,
    create_user,
    user_login,
    logout_user,
    password_reset_request,
    password_reset,
    list_users_by_role,
    hospital_detail,
)

urlpatterns = [
    path('admin/login/', admin_login, name='admin_login'),
    path('user/login/', user_login, name='user_login'),
    path('create-user/', create_user, name='create_user'),
    path('logout/', logout_user, name='logout_user'),
    path('password-reset-request/', password_reset_request, name='password_reset_request'),
    path('password-reset/', password_reset, name='password_reset'),
    path('users/', list_users_by_role, name='list_users_by_role'),
    path('hospital/<int:pk>/', hospital_detail, name='hospital_detail'),
]
