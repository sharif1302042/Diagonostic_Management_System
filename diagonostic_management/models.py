from django.contrib.postgres.indexes import BrinIndex
from django.db import models


class DoctorManager(models.Manager):
    pass


class Doctor(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    mid_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    degree = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True, db_index=True, )
    updated_at = models.DateField(blank=True, null=True)

    objects = DoctorManager()

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctor List"
        # indexes = (
        #     BrinIndex(fields=['pk','created_at'])
        # )
