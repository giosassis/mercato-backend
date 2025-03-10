from rest_framework import serializers
from core.domain.models import Sale, SaleItem, Product
from core.domain.serializers.sale_item_serializer import SaleItemSerializer
from core.domain.serializers.payment_serializer import PaymentSerializer


class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = ["id", "cashier", "date", "total", "items", "payments"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        sale = Sale.objects.create(**validated_data)

        total = 0
        sale_items = []

        for item_data in items_data:
            product = Product.objects.get(id=item_data["product"].id)
            subtotal = product.price * item_data["quantity"]

            sale_item = SaleItem(
                sale=sale,
                product=product,
                quantity=item_data["quantity"],
                subtotal=subtotal,
            )
            sale_items.append(sale_item)

            total += subtotal
            product.stock -= item_data["quantity"]
            product.save()

        SaleItem.objects.bulk_create(sale_items)

        sale.total = total
        sale.save()
        return sale
