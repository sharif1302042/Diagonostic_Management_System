import django_tables2 as tables
from .models import Doctor

class DoctorTable(tables.Table):
    class Meta:
        model = Doctor
        template_name = "django_tables2/bootstrap.html"
        fields = ("username", "degree","first_name")