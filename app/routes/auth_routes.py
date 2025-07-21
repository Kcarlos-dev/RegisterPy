from flask import Blueprint, request, jsonify
from app.models.user import User
from app.extensions import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/users/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')
        user_type = data.get('user_type', 'user')

        if not all([name, email, phone, password]):
            return jsonify({'msg': 'Need of data'}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({'Erro': f"{email} Already in the database"}), 400

        if User.query.filter_by(phone=phone).first():
            return jsonify({'Erro': f"{phone} Already in the database"}), 400

        new_user = User(name=name, email=email, phone=phone, user_type=user_type)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        token = create_access_token(identity={'id': new_user.id, 'user_type': new_user.user_type})
        return jsonify({'msg': 'User registered successfully', 'token': token}), 201
    except Exception as e:
        print(e)
        return "não funciona"
@auth_bp.route('/users/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Need email or password'}), 401

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        token = create_access_token(identity={'id': user.id, 'user_type': user.user_type})
        return jsonify({'msg': 'User return successfully', 'token': token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401

@auth_bp.route('/users/me', methods=['GET'])
@jwt_required()
def auth_user():
    current_user_identity = get_jwt_identity()
    user = User.query.get(current_user_identity['id'])

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'user': {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'user_type': user.user_type
        }
    }), 200
