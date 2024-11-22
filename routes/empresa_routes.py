from flask import Blueprint, render_template, request, jsonify
from models.model_empresa import Empresa
from utils.auth_middleware import role_required

empresa_bp = Blueprint("empresas", __name__)

@empresa_bp.route("/", methods=["POST"])
@role_required("superadmin")
def crear_empresa():
    data = request.json
    nueva_empresa = Empresa.crear(data)
    return jsonify(nueva_empresa), 201


@empresa_bp.route("/", methods=["GET"])
def get_empresas():
    empresas = ["Empresa A", "Empresa B", "Empresa C"]  # Simulación
    return render_template("empresas.html", empresas=empresas)