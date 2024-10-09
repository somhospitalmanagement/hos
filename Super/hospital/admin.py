from django.contrib import admin
from .models import Hospital


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'hospital')