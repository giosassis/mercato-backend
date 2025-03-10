import uuid
from django.db import models
from core.domain.models.sale import Sale
from core.domain.models.product import Product

# Sale Flow
# A cashier add a product -> One saleItem for each product on sale -> The cashier will end the sale -> Payment method


class SaleItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.product.name} - R$ {self.subtotal}"
