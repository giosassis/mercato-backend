from django.shortcuts import get_object_or_404
from core.domain.models import Product

class ProductRepository:
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_by_id(product_id):
        return get_object_or_404(Product, id=product_id)

    @staticmethod
    def get_by_category(category_id):
        return Product.objects.filter(category__id=category_id)
    
    @staticmethod
    def get_by_barcode(barcode):
        return Product.objects.filter(barcode=barcode).first()

    @staticmethod
    def create_product(data):
        return Product.objects.create(**data)

    @staticmethod
    def update_product(product, data):
        for key, value in data.items():
            setattr(product, key, value)
        product.save()
        return product

    @staticmethod
    def delete_product(product):
        product.delete()
