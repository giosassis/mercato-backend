from rest_framework import serializers
from core.domain.models import User
from core.domain.serializers import EmployeeSerializer

class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)  

    class Meta:
        model = User
        fields = ["id", "username", "register_number", "employee", "role"]
