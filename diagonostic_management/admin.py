from django.contrib import admin
from .models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'degree')


admin.site.register(Doctor, DoctorAdmin)
