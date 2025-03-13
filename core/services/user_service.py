from core.repositories.user_repository import UserRepository
from core.repositories.employee_repository import EmployeeRepository
from core.domain.models import Employee, User
from django.contrib.auth.hashers import make_password
import uuid


class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def get_user_by_id(user_id):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    @staticmethod
    def create_user(data):
        employee_data = data.pop("employee")

        if "register_number" not in data or not data["register_number"]:
            data["register_number"] = UserService.generate_register_number()

        if UserRepository.get_by_register_number(data["register_number"]):
            raise ValueError("A user with this register number already exists")

        employee = EmployeeRepository.create_employee(employee_data)
        data["employee"] = employee
        data["password"] = make_password(data["password"])
        return UserRepository.create_user(data)

    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        employee_data = data.pop("employee", None)

        if employee_data:
            EmployeeRepository.update_employee(user.employee, employee_data)

        if "password" in data:
            data["password"] = make_password(data["password"])

        return UserRepository.update_user(user, data)

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        EmployeeRepository.delete_employee(user.employee)
        UserRepository.delete_user(user)

    def generate_register_number():
        while True:
            new_register_number = str(uuid.uuid4().int)[:10]
            if not UserRepository.get_by_register_number(new_register_number):
                return new_register_number
