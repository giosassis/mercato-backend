from rest_framework import serializers
from core.domain.models import Sale
from core.domain.serializers.sale_item_serializer import SaleItemSerializer
from core.domain.serializers.payment_serializer import PaymentSerializer

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True, read_only=True)  
    payments = PaymentSerializer(many=True, read_only=True)  

    class Meta:
        model = Sale
        fields = ["id", "cashier", "date", "total", "items", "payments"]
