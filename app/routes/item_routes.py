from flask import Blueprint, request, jsonify
from app.models.menu_item import MenuItem
from app.extensions import db
from app.middleware.auth import user_type_required

item_bp = Blueprint('item_bp', __name__)

@item_bp.route('/items/register', methods=['POST'])
@user_type_required('admin', 'stockist')
def register_items():
    data = request.get_json()
    # ... lógica de validação e criação do item ...
    # Exemplo:
    new_item = MenuItem(**data)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"msg": "Items registered successfully"}), 201

@item_bp.route('/items', methods=['GET'])
@user_type_required('user', 'admin')
def get_items():
    name = request.args.get('name')
    if name:
        items = MenuItem.query.filter_by(name=name).all()
    else:
        items = MenuItem.query.all()
    # ... lógica para serializar os itens e retornar ...
    return jsonify({"msg": "Items found successfully", "data": [item_schema(item) for item in items]}), 200

# ... outras rotas (Update, Delete) ...

def item_schema(item):
    return {
        "item_id": item.item_id,
        "name": item.name,
        "description": item.description,
        "price": str(item.price),
        "category": item.category,
        "stock_quantity": item.stock_quantity,
        "is_available": item.is_available
    }