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
)

urlpatterns = [
    
    path('admin/login/', admin_login, name='admin_login'),
    path('user/login/', user_login, name='user_login'),
    path('logout/', logout_user, name='logout_user'),

    
    path('create-user/', create_user, name='create_user'),
    path('users/', list_users_by_role, name='list_users_by_role'),

    
    path('password-reset-request/', password_reset_request, name='password_reset_request'),
    path('password-reset/', password_reset, name='password_reset'),

    # Hospital detail URL
    
]

