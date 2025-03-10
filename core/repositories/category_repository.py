from core.domain.models import Category

class CategoryRepository:
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_by_id(category_id):
        return Category.objects.filter(id=category_id).first()
    
    def get_by_name(category_name):
        return Category.objects.filter(name=category_name).first()

    @staticmethod
    def create_category(data):
        return Category.objects.create(**data)

    @staticmethod
    def update_category(category, data):
        for key, value in data.items():
            setattr(category, key, value)
        category.save()
        return category

    @staticmethod
    def delete_category(category):
        category.delete()
