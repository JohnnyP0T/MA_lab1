from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример данных о клиентах в виде словаря
customers_data = {
    1: {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
    2: {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"},
}

# Эндпоинт для получения всех клиентов
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(list(customers_data.values()))

# Эндпоинт для получения информации о конкретном клиенте
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = customers_data.get(customer_id)
    if customer:
        return jsonify(customer)
    else:
        return jsonify({"error": "Customer not found"}), 404

# Эндпоинт для добавления нового клиента
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer_id = max(customers_data.keys()) + 1
    data["id"] = new_customer_id
    customers_data[new_customer_id] = data
    return jsonify(data), 201

# Эндпоинт для удаления клиента
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    if customer_id in customers_data:
        del customers_data[customer_id]
        return jsonify({"message": f"Customer {customer_id} deleted"}), 200
    else:
        return jsonify({"error": "Customer not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
