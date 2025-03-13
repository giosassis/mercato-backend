from core.domain.models import Employee


class EmployeeRepository:
    @staticmethod
    def get_all_employees():
        return Employee.objects.all()

    @staticmethod
    def get_by_id(employee_id):
        return Employee.objects.filter(id=employee_id).first()

    @staticmethod
    def create_employee(data):
        return Employee.objects.create(**data)

    @staticmethod
    def update_employee(employee, data):
        for key, value in data.items():
            setattr(employee, key, value)
        employee.save()
        return employee

    @staticmethod
    def delete_employee(employee):
        employee.delete()
