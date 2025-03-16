from core.repositories.product_repository import ProductRepository

class ProductService:
    
    @staticmethod
    def get_all_products():
        return ProductRepository.get_all_products()
    
    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_by_id(product_id)

    @staticmethod
    def get_products_by_category(category_id):
        return ProductRepository.get_by_category(category_id)
    
    @staticmethod
    def get_product_by_barcode(barcode):
        product = ProductRepository.get_by_barcode(barcode)
        if not product:
            raise ValueError("Product not found")
        return product
    
    @staticmethod
    def search_products(query):
        return ProductRepository.search_products(query)
    
    @staticmethod
    def create_product(data):
        if ProductRepository.get_by_barcode(data["barcode"]):
            raise ValueError("Barcode already exists")
        return ProductRepository.create_product(data)

    @staticmethod
    def update_product(product_id, data):
        product = ProductRepository.get_by_id(product_id)
        return ProductRepository.update_product(product, data)

    @staticmethod
    def delete_product(product_id):
        product = ProductRepository.get_by_id(product_id)
        ProductRepository.delete_product(product)
