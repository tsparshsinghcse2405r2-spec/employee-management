from flask import Flask, jsonify, request
from employee import EmployeeManager

app = Flask(__name__)
manager = EmployeeManager()

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    try:
        emp_id = manager.add_employee(
            data['name'], data['department'], data['salary'])
    except ValueError as err:
        return jsonify({'error': str(err)}), 400
    return jsonify({'id': emp_id}), 201

@app.route('/employees/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    try:
        return jsonify(manager.get_employee(emp_id))
    except KeyError:
        return jsonify({'error': 'Employee not found'}), 404

@app.route('/payroll', methods=['GET'])
def payroll():
    return jsonify({'total': manager.total_payroll()})

@app.route('/health', methods=['GET'])
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)
