from rest_framework import serializers
from .models import DriverApplication

class DriverApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverApplication
        fields = '__all__'
