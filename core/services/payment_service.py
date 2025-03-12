from core.repositories.payment_repository import PaymentRepository
from core.repositories.sale_repository import SaleRepository


class PaymentService:
    @staticmethod
    def get_payments_by_sale(sale_id):
        sale = SaleRepository.get_by_id(sale_id)
        if not sale:
            raise ValueError("Sale not found")
        return PaymentRepository.get_by_sale(sale)

    @staticmethod
    def process_payment(sale_id, payment_data):
        sale = SaleRepository.get_by_id(sale_id)
        if not sale:
            raise ValueError("Sale not found.")

        total_paid = sum(p.amount for p in PaymentRepository.get_by_sale(sale))
        new_total = total_paid + payment_data["amount"]
        if new_total > sale.total:
            raise ValueError(
                f"Payment exceeds the sale amount! Total allowed: R$ {sale.total - total_paid:.2f}"
            )

        payment = PaymentRepository.create_payment(
            {
                "sale": sale,
                "payment_method": payment_data["payment_method"],
                "amount": payment_data["amount"],
            }
        )

        return payment
