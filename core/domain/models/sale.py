import uuid
from django.db import models
from core.domain.models.user import User


class Sale(models.Model):

    CREATED = "created"
    COMPLETED = "completed"
    PENDING = "pending"
    REFUNDED = "refunded"
    CANCELED = "canceled"

    SALE_STATUS_CHOICES = [
        (CREATED, "Criada"),
        (COMPLETED, "Comcluída"),
        (PENDING, "Pendente"),
        (REFUNDED, "Reembolsada"),
        (CANCELED, "Cancelada"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cashier = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # one sale for one user (cashier)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status=models.CharField(max_length=10, choices=SALE_STATUS_CHOICES, default=CREATED)
    def __str__(self):
        return f"Sale #{self.id} - {self.cashier.username} - {self.date}"
