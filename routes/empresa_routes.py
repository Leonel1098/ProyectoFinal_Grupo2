from flask import Blueprint, request, jsonify
from models.model_empresa import Empresa
from utils.auth_middleware import role_required

empresa_bp = Blueprint("empresa", __name__)

@empresa_bp.route("/", methods=["POST"])
@role_required("superadmin")
def crear_empresa():
    data = request.json
    nueva_empresa = Empresa.crear(data)
    return jsonify(nueva_empresa), 201
