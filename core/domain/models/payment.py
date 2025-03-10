import uuid
from django.db import models
from core.domain.models.sale import Sale

class Payment(models.Model):
    CASH = "cash"
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PIX = "pix"

    CHOICE_PAYMENT_METHODS = [
        (CASH, "Cash"),
        (CREDIT_CARD, "Credit Card"),
        (DEBIT_CARD, "Debit Card"),
        (PIX, "Pix"),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="payments")
    payment_method = models.CharField(max_length=15, choices=CHOICE_PAYMENT_METHODS)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment #{self.id} - {self.payment_method} - R$ {self.amount}"
