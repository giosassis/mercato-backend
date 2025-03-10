from rest_framework import serializers
from core.domain.models import SaleItem, Product
from core.domain.serializers.product_serializer import ProductSerializer

class SaleItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all()) 
    class Meta:
        model = SaleItem
        fields = ["id", "sale", "product", "quantity", "subtotal"]
