import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.domain.models import User
from mixer.backend.django import mixer

@pytest.mark.django_db
def test_list_users():
    """It should list all users"""
    mixer.cycle(3).blend(User)
    client = APIClient()

    response = client.get(reverse("user-list"))
    
    assert response.status_code == 200
    assert len(response.json()) == 3

@pytest.mark.django_db
def test_create_user():
    """It should """
    client = APIClient()
    data = {
        "username": "testuser",
        "register_number": "1234567890",
        "role": "cashier",
        "password": "securepassword",
        "employee": {"name": "John Doe"},
    }

    response = client.post(reverse("user-list"), data, format="json")
    
    assert response.status_code == 201
    assert response.json()["register_number"] == "1234567890"

@pytest.mark.django_db
def test_create_user_with_duplicate_register_number():
    """Deve falhar ao tentar criar um usuário com register_number já existente"""
    mixer.blend(User, register_number="1234567890")

    client = APIClient()
    data = {
        "username": "user2",
        "register_number": "1234567890",
        "role": "manager",
        "password": "securepassword",
        "employee": {"name": "John Doe"},
    }

    response = client.post(reverse("user-list"), data, format="json")
    
    assert response.status_code == 400
    assert "error" in response.json()
