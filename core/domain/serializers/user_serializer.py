from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from core.domain.models import User
from core.domain.serializers.employee_serializer import EmployeeSerializer


class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "password", "register_number", "role", "employee"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        employee_data = validated_data.pop("employee")
        employee = Employee.objects.create(**employee_data)
        user = User.objects.create(employee=employee, **validated_data)
        user.password = make_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        employee_data = validated_data.pop("employee", None)

        if employee_data:
            for key, value in employee_data.items():
                setattr(instance.employee, key, value)
            instance.employee.save()

        for key, value in validated_data.items():
            if key == "password":
                instance.password = make_password(value)
            else:
                setattr(instance, key, value)

        instance.save()
        return instance
