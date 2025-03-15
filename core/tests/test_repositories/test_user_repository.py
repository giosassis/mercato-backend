import pytest
from django.contrib.auth.hashers import check_password
from core.domain.models.user import User
from core.domain.models.employee import Employee
from core.repositories.user_repository import UserRepository
from mixer.backend.django import mixer


@pytest.mark.django_db
def test_create_user():
    """Should create a user correctly"""
    employee = mixer.blend(Employee)
    user_data = {
        "username": "testuser",
        "register_number": "1234567890",
        "employee": employee,
        "role": User.CASHIER,
        "password": "secure_password",
    }

    user = UserRepository.create_user(user_data)

    assert user.id is not None
    assert user.username == "testuser"
    assert user.register_number == "1234567890"
    assert user.employee == employee
    assert user.role == User.CASHIER


@pytest.mark.django_db
def test_create_user_with_duplicate_register_number():
    """Should raise an exception if a user with the same register number already exists"""
    mixer.blend(User, register_number="1234567890")

    user_data = {
        "username": "user2",
        "register_number": "1234567890",
        "role": User.MANAGER,
        "password": "secure_password",
    }

    with pytest.raises(Exception):
        UserRepository.create_user(user_data)


@pytest.mark.django_db
def test_get_by_register_number():
    """Should return a user by its register number"""
    user = mixer.blend(User, register_number="1234567890")

    retrieved_user = UserRepository.get_by_register_number("1234567890")

    assert retrieved_user is not None
    assert retrieved_user.id == user.id


@pytest.mark.django_db
def test_get_all_users():
    """Should return all users"""
    mixer.cycle(5).blend(User)
    users = UserRepository.get_all_users()
    assert users.count() == 5

@pytest.mark.django_db
def test_get_user_by_id():
    """Should return a user by its id"""
    user = mixer.blend(User)
    
    retrieved_user = UserRepository.get_by_id(user.id)
    
    assert retrieved_user is not None
    assert retrieved_user.id == user.id
