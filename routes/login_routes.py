from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.model_usuario import Usuario
from utils.hash_util import check_password

usuario_bp = Blueprint("login", __name__)

@usuario_bp.route("/", methods=['GET', 'POST'])
def login():
    data = request.get_json()
    usuario = Usuario.obtener_usuario_por_email(data["email"])
    if not usuario or not check_password(data["password"], usuario["password"]):
        return jsonify({"msg": "Credenciales inválidas"}), 401

    token = create_access_token(identity={
        "id": str(usuario["_id"]),
        "rol": usuario["rol"],
        "empresa_id": usuario.get("empresa_id"),
        "departamento_id": usuario.get("departamento_id")
    })
    return jsonify({"token": token})
