from core.domain.models.user import User

class UserRepository:
    @staticmethod
    def get_all_users():
        return User.objects.all()

    @staticmethod
    def get_by_id(user_id):
        return User.objects.filter(id=user_id).first()

    @staticmethod
    def get_by_register_number(register_number):
        return User.objects.filter(register_number=register_number).first()

    @staticmethod
    def create_user(data):
        return User.objects.create(**data)

    @staticmethod
    def update_user(user, data):
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def delete_user(user):
        user.delete()
