from django.contrib import admin
from .models import CustomUser, Hospital, UserType


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'hospital', 'user_type')
    search_fields = ('username', 'email', 'hospital__name', 'user_type__name')
    list_filter = ('hospital', 'user_type')


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(UserType, UserTypeAdmin)


