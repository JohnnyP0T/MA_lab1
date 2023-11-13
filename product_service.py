from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример данных о продуктах в виде словаря
products_data = {
    1: {"id": 1, "name": "Product A", "price": 20.0},
    2: {"id": 2, "name": "Product B", "price": 30.0},
}

# Эндпоинт для получения всех продуктов
@app.route('/products', methods=['GET'])
def get_products():
    try:
        return jsonify(list(products_data.values()))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Эндпоинт для получения информации о конкретном продукте
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = products_data.get(product_id)
        if product:
            return jsonify(product)
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Эндпоинт для добавления нового продукта
@app.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.get_json()
        new_product_id = max(products_data.keys()) + 1
        data["id"] = new_product_id
        products_data[new_product_id] = data
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Эндпоинт для удаления продукта
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        if product_id in products_data:
            del products_data[product_id]
            return jsonify({"message": f"Product {product_id} deleted"}), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
