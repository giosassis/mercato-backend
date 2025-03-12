from core.repositories.category_repository import CategoryRepository

class CategoryService:
    @staticmethod
    def get_all_categories():
        return CategoryRepository.get_all_categories()

    @staticmethod
    def get_category_by_id(category_id):
        category = CategoryRepository.get_by_id(category_id)
        if not category:
            raise ValueError("Category not found")
        return category

    @staticmethod
    def create_category(data):
        if CategoryRepository.get_by_name(data["name"]):
            raise ValueError("A category with this name already exists")
        return CategoryRepository.create_category(data)

    @staticmethod
    def update_category(category_id, data):
        category = CategoryRepository.get_by_id(category_id)
        if not category:
            raise ValueError("Category not found")
        
        return CategoryRepository.update_category(category, data)

    @staticmethod
    def delete_category(category_id):
        category = CategoryRepository.get_by_id(category_id)
        if not category:raise ValueError("Category not found")

        CategoryRepository.delete_category(category)
