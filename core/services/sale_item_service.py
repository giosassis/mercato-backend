from core.repositories.sale_item_repository import SaleItemRepository
from core.repositories.sale_repository import SaleRepository
from core.repositories.product_repository import ProductRepository
from core.domain.models import SaleItem

class SaleItemService:
    @staticmethod
    def get_items_by_sale(sale_id):
        sale = SaleRepository.get_by_id(sale_id)
        if not sale:
            raise ValueError("Sale not found")
        return SaleItemRepository.get_items_by_sale(sale)

    @staticmethod
    def add_item_to_sale(sale_id, item_data):
        sale = SaleRepository.get_by_id(sale_id)
        if not sale:
            raise ValueError("Sale not found")

        product = ProductRepository.get_by_id(item_data["product"].id)
        if not product:
            raise ValueError(f"Produto {item_data['product']} não encontrado")

        subtotal = product.price * item_data["quantity"]

        sale_item = SaleItemRepository.create_sale_item({
            "sale": sale,
            "product": product,
            "quantity": item_data["quantity"],
            "subtotal": subtotal
        })
        
        product.stock -= item_data["quantity"]
        product.save()

        sale.total += subtotal
        sale.save()

        return sale_item

    @staticmethod
    def remove_item_from_sale(item_id):
        sale_item = SaleItemRepository.get_by_id(item_id)
        if not sale_item:
            raise ValueError("Item não encontrado na venda")

        product = sale_item.product
        product.stock += sale_item.quantity
        product.save()

        sale = sale_item.sale
        sale.total -= sale_item.subtotal
        sale.save()

        SaleItemRepository.delete_sale_item(sale_item)
