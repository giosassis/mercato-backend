from rest_framework import serializers
from core.domain.models.payment import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "sale", "payment_method", "amount"]