from flask import Blueprint, request, jsonify
from app.models.order import Order
from app.models.menu_item import MenuItem
from app.extensions import db
from app.middleware.auth import user_type_required
from flask_jwt_extended import get_jwt_identity

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders/register', methods=['POST'])
@user_type_required('user', 'admin')
def register_order():
    data = request.get_json()
    current_user = get_jwt_identity()
    user_id = current_user['id']
    item_id = data.get('item_id')
    quantity = data.get('quantity')

    if not all([item_id, quantity]):
        return jsonify({"msg": "Missing item_id or quantity"}), 400

    item = MenuItem.query.get(item_id)

    if not item:
        return jsonify({"msg": "Item not found"}), 404

    if not item.is_available or item.stock_quantity < quantity:
        return jsonify({"msg": "Item not available or insufficient stock"}), 400
    
    # Calcula o preço do pedido
    order_price = item.price * quantity

    new_order = Order(
        user_id=user_id,
        item_id=item_id,
        quantity=quantity,
        order_price=order_price,
        status='process'
    )

    # Atualiza o estoque
    item.stock_quantity -= quantity
    if item.stock_quantity == 0:
        item.is_available = False

    db.session.add(new_order)
    db.session.add(item)
    db.session.commit()

    return jsonify({"msg": "Order registered successfully", "order_id": new_order.order_id}), 201


@order_bp.route('/orders', methods=['GET'])
@user_type_required('admin')
def get_orders():
    orders = Order.query.all()
    # Para uma aplicação real, você criaria um schema para serializar isso
    result = [
        {
            "order_id": order.order_id,
            "user_id": order.user_id,
            "item_id": order.item_id,
            "quantity": order.quantity,
            "order_price": str(order.order_price),
            "status": order.status,
            "created_at": order.created_at.isoformat()
        } for order in orders
    ]
    return jsonify(result), 200