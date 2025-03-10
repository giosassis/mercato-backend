import uuid
from django.db import models
from core.domain.models.user import User

class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cashier = models.ForeignKey(User, on_delete=models.CASCADE)  
    date = models.DateTimeField(auto_now_add=True) 
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  

    def __str__(self):
        return f"Sale #{self.id} - {self.cashier.username} - {self.date}"
