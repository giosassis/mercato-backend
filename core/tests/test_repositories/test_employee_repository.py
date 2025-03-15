import pytest
from core.domain.models.employee import Employee
from core.repositories.employee_repository import EmployeeRepository
from mixer.backend.django import mixer


@pytest.mark.django_db
def test_create_employee():
    """Should create an employee correctly"""
    employee_data = {
        "name": "John Doe",
        "birth_date": "1990-01-01",
        "address": "123 Main St",
        "phone": "1234567890",
        "email": "johndoe@example.com",
    }

    employee = EmployeeRepository.create_employee(employee_data)

    assert employee.id is not None
    assert employee.name == "John Doe"
    assert employee.birth_date == "1990-01-01"
    assert employee.address == "123 Main St"
    assert employee.phone == "1234567890"
    assert employee.email == "johndoe@example.com"


@pytest.mark.django_db
def test_create_employee_without_name():
    """It should raise an exception if the name is not provided"""
    employee_data = {
        "name": "",
        "birth_date": "1990-01-01",
        "address": "123 Main St",
        "phone": "1234567890",
        "email": "johndoe@example.com",
    }

    with pytest.raises(Exception):
        employee = EmployeeRepository.create_employee(employee_data)
        employee.full_clean()


@pytest.mark.django_db
def test_get_all_employees():
    """Should return all employees"""
    mixer.cycle(5).blend(Employee)

    employees = EmployeeRepository.get_all_employees()

    assert employees.count() == 5


@pytest.mark.django_db
def test_update_employee():
    """Should update an employee correctly"""
    employee = mixer.blend(Employee, email="johndoe@example.com")

    update_data = {"email": "john@example.com"}
    updated_employee = EmployeeRepository.update_employee(employee, update_data)

    assert updated_employee.email == "john@example.com"


@pytest.mark.django_db
def test_get_by_id():
    """Should return an employee by its id"""
    employee = mixer.blend(Employee)

    retrieved_employee = EmployeeRepository.get_by_id(employee.id)

    assert retrieved_employee is not None
    assert retrieved_employee.id == employee.id


@pytest.mark.django_db
def test_delete_employee():
    """Should delete an employee correctly"""
    employee = mixer.blend(Employee)

    EmployeeRepository.delete_employee(employee)

    assert Employee.objects.filter(id=employee.id).count() == 0
