import pytest
from employee import EmployeeManager

@pytest.fixture
def manager():
    return EmployeeManager()

def test_add_employee_returns_id(manager):
    assert manager.add_employee('Asha', 'IT', 50000) == 1

def test_get_employee(manager):
    emp_id = manager.add_employee('Ravi', 'HR', 40000)
    assert manager.get_employee(emp_id)['name'] == 'Ravi'

def test_update_salary(manager):
    emp_id = manager.add_employee('Asha', 'IT', 50000)
    manager.update_salary(emp_id, 60000)
    assert manager.get_employee(emp_id)['salary'] == 60000

def test_delete_employee(manager):
    emp_id = manager.add_employee('Asha', 'IT', 50000)
    manager.delete_employee(emp_id)
    with pytest.raises(KeyError):
        manager.get_employee(emp_id)

def test_list_by_department(manager):
    manager.add_employee('A', 'IT', 1000)
    manager.add_employee('B', 'HR', 2000)
    assert len(manager.list_by_department('IT')) == 1

def test_total_payroll(manager):
    manager.add_employee('A', 'IT', 1000)
    manager.add_employee('B', 'HR', 2000)
    assert manager.total_payroll() == 3000

@pytest.mark.parametrize('name,salary', [('', 1000), ('   ', 1000), ('Asha', -1)])
def test_invalid_input_rejected(manager, name, salary):
    with pytest.raises(ValueError):
        manager.add_employee(name, 'IT', salary)

def test_get_unknown_employee(manager):
    with pytest.raises(KeyError):
        manager.get_employee(99)
