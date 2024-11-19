from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from functools import wraps

def role_required(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            usuario = get_jwt_identity()
            if usuario["rol"] not in roles:
                return jsonify({"msg": "No autorizado"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator
