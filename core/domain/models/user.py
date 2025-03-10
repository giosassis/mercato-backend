import uuid
from django.db import models
from core.domain.models.employee import Employee
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CASHIER = "cashier"
    MANAGER = "manager"
    
    CHOICE_ROLES = [
        (CASHIER, "Cashier"),
        (MANAGER, "Manager"),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    register_number = models.CharField(max_length=10, unique=True)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True, blank=False)
    role = models.CharField(max_length=10, choices=CHOICE_ROLES, default=CASHIER)

    def __str__(self):
        return f"{self.username} - {self.role}"
