from rest_framework import serializers
from core.domain.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "barcode", "category", "price", "stock"]
        