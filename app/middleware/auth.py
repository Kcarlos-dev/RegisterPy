from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

def user_type_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_identity()
            user_type = claims.get('user_type')

            if user_type not in roles:
                return jsonify(msg="No access for this user type!"), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper