from rest_framework import serializers
from core.domain.models.fake_invoice import FakeInvoice


class FakeInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeInvoice
        fields = "__all__"
