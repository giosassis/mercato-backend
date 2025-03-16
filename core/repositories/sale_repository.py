from core.domain.models.sale import Sale
from django.db.models.functions import TruncDate
from django.db.models import Sum, DateField

class SaleRepository:

    @staticmethod
    def get_all_sales():
        return Sale.objects.all()

    @staticmethod
    def get_by_id(sale_id):
        return Sale.objects.filter(id=sale_id).first()

    @staticmethod
    def get_by_cashier(cashier):
        return Sale.objects.filter(cashier=cashier)

    @staticmethod
    def get_sales_total_per_day():
        return (
            Sale.objects.annotate(sale_date=TruncDate("date"))
            .values("sale_date")
            .annotate(total_sales=Sum("total"))  
            .order_by("date")
        )
        
    @staticmethod
    def create_sale(data):
        return Sale.objects.create(**data)

    @staticmethod
    def update_sale(sale, data):
        for key, value in data.items():
            setattr(sale, key, value)
        sale.save()
        return sale

    @staticmethod
    def delete_sale(sale):
        sale.delete()
