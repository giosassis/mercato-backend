from core.repositories.sale_repository import SaleRepository
from core.repositories.sale_item_repository import SaleItemRepository
from core.repositories.product_repository import ProductRepository
from core.domain.models import SaleItem


class SaleService:

    @staticmethod
    def get_all_sales():
        return SaleRepository.get_all_sales()

    @staticmethod
    def get_sale_by_id(sale_id):
        return SaleRepository.get_by_id(sale_id)

    @staticmethod
    def get_sales_by_cashier(cashier):
        return SaleRepository.get_by_cashier(cashier)

    def get_sales_total_per_day():
        return SaleRepository.get_sales_total_per_day()
    
    def create_sale(data):
        items_data = data.pop("items")
        sale = SaleRepository.create_sale(data)

        sale.status = Sale.PENDING
        sale.save()

        total = 0
        for item_data in items_data:
            product = ProductRepository.get_by_id(item_data["product"].id)
            if not product:
                raise ValueError(f"Product {item_data['product']} not found")

            if product.stock < item_data["quantity"]:
                raise ValueError(
                    f"Insufficient stock for product {item_data['product']}"
                )

            subtotal = product.price * item_data["quantity"]

            SaleItemRepository.create_sale_item(
                {
                    "sale": sale,
                    "product": product,
                    "quantity": item_data["quantity"],
                    "subtotal": subtotal,
                }
            )

            product.stock -= item_data["quantity"]
            product.save()

            total += subtotal

        sale.total = total
        sale.save()
        return sale

    @staticmethod
    def update_sale(sale_id, data):
        sale = SaleRepository.get_by_id(sale_id)
        if not sale:
            raise ValueError("Sale not found.")

        items_data = data.pop("items", None)

        for attr, value in data.items():
            setattr(sale, attr, value)

        sale.save()

        if items_data:
            SaleItemRepository.delete_items_by_sale(sale)
            total = 0
            for item_data in items_data:
                product = ProductRepository.get_by_id(item_data["product"].id)
                if not product:
                    raise ValueError(f"Product {item_data['product']} not found")

                if product.stock < item_data["quantity"]:
                    raise ValueError(
                        f"Insufficient stock for product {item_data['product']}"
                    )

                subtotal = product.price * item_data["quantity"]

                SaleItemRepository.create_sale_item(
                    {
                        "sale": sale,
                        "product": product,
                        "quantity": item_data["quantity"],
                        "subtotal": subtotal,
                    }
                )

                product.stock -= item_data["quantity"]
                product.save()
                total += subtotal

            sale.total = total
            sale.save()

        return sale

    @staticmethod
    def delete_sale(sale_id):
        sale = SaleRepository.get_by_id(sale_id)
        if not sale:
            raise ValueError("Sale not found.")
        SaleRepository.delete_sale(sale)

    @staticmethod
    def cancel_sale(sale_id):
        sale = SaleRepository.get_by_id(sale_id)
        if not sale:
            raise ValueError("Sale not found.")
        sale.delete()
