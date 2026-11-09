class EmployeeManager:
    def __init__(self):
        self._employees = {}
        self._next_id = 1

    def add_employee(self, name, department, salary):
        if not name or not name.strip():
            raise ValueError('Name cannot be empty')
        if salary < 0:
            raise ValueError('Salary cannot be negative')
        emp_id = self._next_id
        self._employees[emp_id] = {
            'id': emp_id,
            'name': name.strip(),
            'department': department,
            'salary': salary,
        }
        self._next_id += 1
        return emp_id

    def get_employee(self, emp_id):
        if emp_id not in self._employees:
            raise KeyError('Employee not found')
        return self._employees[emp_id]

    def update_salary(self, emp_id, new_salary):
        if new_salary < 0:
            raise ValueError('Salary cannot be negative')
        self.get_employee(emp_id)['salary'] = new_salary

    def delete_employee(self, emp_id):
        self.get_employee(emp_id)
        del self._employees[emp_id]

    def list_by_department(self, department):
        return [e for e in self._employees.values()
                if e['department'] == department]

    def total_payroll(self):
        return sum(e['salary'] for e in self._employees.values())
