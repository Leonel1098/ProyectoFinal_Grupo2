from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.model_usuario import Usuario
from utils.hash_util import check_password

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    usuario = Usuario.find_by_email(data["email"])
    if not usuario or not check_password(data["password"], usuario["password"]):
        return jsonify({"msg": "Credenciales inválidas"}), 401

    token = create_access_token(identity={
        "id": str(usuario["_id"]),
        "rol": usuario["rol"],
        "empresa_id": usuario.get("empresa_id"),
        "departamento_id": usuario.get("departamento_id")
    })
    return jsonify({"token": token})
