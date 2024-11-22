from flask import Blueprint, jsonify, request
from models.model_departamento import Departamento
from utils.auth_middleware import role_required

departamento_bp = Blueprint("departamento", __name__)
@departamento_bp.route("/", methods=["POST"])
@role_required("admin_empresa")
def crear_departamento():
    data = request.json
    nuevo_departamento = Departamento.crear(data)
    return jsonify(nuevo_departamento), 201

