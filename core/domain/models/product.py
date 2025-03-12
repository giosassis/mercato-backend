from django.db import models
import uuid
from core.domain.models.category import Category
from django.core.validators import MinValueValidator, RegexValidator

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    barcode = models.CharField(
        max_length=20, 
        unique=True,
        validators=[RegexValidator(r'^\d{12,13}$', 'Barcode must be 12 or 13 digits')]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items", null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name} - {self.barcode}"
