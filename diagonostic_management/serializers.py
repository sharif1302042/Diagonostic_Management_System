from rest_framework import serializers

from .models import Doctor

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
