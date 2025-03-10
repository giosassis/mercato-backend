from rest_framework import serializers
from core.domain.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    sale = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Payment
        fields = ["id", "sale", "payment_method", "amount"]
