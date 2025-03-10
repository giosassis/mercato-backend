from rest_framework import serializers
from core.domain.models import SaleItem, Product
from core.domain.serializers.product_serializer import ProductSerializer

class SaleItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())  
    sale = serializers.PrimaryKeyRelatedField(read_only=True)   
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)  

    class Meta:
        model = SaleItem
        fields = ["id", "sale", "product", "quantity", "subtotal"]
