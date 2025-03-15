import pytest
from core.services.user_service import UserService
from core.repositories.user_repository import UserRepository
from core.domain.models.user import User
from core.domain.models.employee import Employee
from unittest.mock import patch
from mixer.backend.django import mixer

@pytest.mark.django_db
def test_create_user():
    """It should create a user correctly"""
    employee = mixer.blend(Employee)
    
    user_data = {
        "username": "testuser",
        "register_number": "1234567890",
        "employee": {"name": "John Doe"},
        "role": User.CASHIER,
        "password": "secure_password",
    }

    with patch("core.repositories.employee_repository.EmployeeRepository.create_employee", return_value=employee):
        user = UserService.create_user(user_data)

    assert user.id is not None
    assert user.username == "testuser"
    assert user.register_number == "1234567890"
    assert user.role == User.CASHIER
    assert user.employee == employee

@pytest.mark.django_db
def test_create_user_with_existing_register_number():
    """It should raise an exception if a user with the same register number already exists"""
    mixer.blend(User, register_number="1234567890")

    user_data = {
        "username": "user2",
        "register_number": "1234567890",
        "role": User.MANAGER,
        "password": "securepassword",
        "employee": {"name": "John Doe"},
    }

    with pytest.raises(ValueError, match="A user with this register number already exists"):
        UserService.create_user(user_data)

@pytest.mark.django_db
def test_get_user_by_id():
    """It should return a user by its ID"""
    user = mixer.blend(User)

    retrieved_user = UserService.get_user_by_id(user.id)
    
    assert retrieved_user is not None
    assert retrieved_user.id == user.id
