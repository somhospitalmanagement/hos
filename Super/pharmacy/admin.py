from django.contrib import admin
from .models import Pharmacist, MedicineInventory, Prescription


class PharmacistAdmin(admin.ModelAdmin):
    list_display = ('user', 'hospital', 'department')
    search_fields = ('user__username', 'hospital__name', 'department__name')
    list_filter = ('hospital', 'department')


class MedicineInventoryAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'quantity', 'unit', 'hospital')
    search_fields = ('medicine_name', 'hospital__name')
    list_filter = ('hospital', 'unit')
    ordering = ('hospital', 'medicine_name')
    list_editable = ('quantity',)


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('get_patient_username', 'get_medicine_name', 'quantity', 'fulfilled', 'get_pharmacist_username')
    search_fields = ('patient__user__username', 'pharmacist__user__username', 'medicine__name')
    list_filter = ('fulfilled',)
    ordering = ('fulfilled', 'quantity')

    
    def mark_as_fulfilled(self, request, queryset):
        for prescription in queryset:
            if not prescription.fulfilled:
                prescription.fulfill()
        self.message_user(request, "Selected prescriptions have been fulfilled.")
    mark_as_fulfilled.short_description = "Mark selected prescriptions as fulfilled"

    
    def get_patient_username(self, obj):
        return obj.patient.user.username
    get_patient_username.short_description = 'Patient'

    def get_medicine_name(self, obj):
        return obj.medicine_name
    get_medicine_name.short_description = 'Medicine'

    def get_pharmacist_username(self, obj):
        return obj.pharmacist.user.username
    get_pharmacist_username.short_description = 'Pharmacist'


admin.site.register(Pharmacist, PharmacistAdmin)
admin.site.register(MedicineInventory, MedicineInventoryAdmin)
admin.site.register(Prescription, PrescriptionAdmin)

