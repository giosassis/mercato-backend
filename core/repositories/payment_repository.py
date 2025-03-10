from core.domain.models import Payment


class PaymentRepository:
    @staticmethod
    def get_by_sale(sale):
        return Payment.objects.filter(sale=sale)

    @staticmethod
    def create_payment(data):
        return Payment.objects.create(**data)
