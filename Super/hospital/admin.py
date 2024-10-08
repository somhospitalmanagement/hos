from django.contrib import admin
from .models import Hospital, UserType


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name',)


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'hospital')