from rest_framework import serializers
from core.domain.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "name", "birth_date", "address", "phone", "email"]
