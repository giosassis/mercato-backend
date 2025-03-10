from core.domain.models.sale_item import SaleItem

class SaleItemRepository:
    
    @staticmethod
    def get_all_sale_items():
        return SaleItem.objects.all()
    
    def create_sale_item(data):
        return SaleItem.objects.create(**data)