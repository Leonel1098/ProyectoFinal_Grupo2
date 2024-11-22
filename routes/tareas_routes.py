from flask import Blueprint, jsonify, render_template, request
from models.model_tarea import Tarea
from utils.auth_middleware import role_required

tarea_bp = Blueprint("tareas", __name__)

@tarea_bp.route("/", methods=["POST"])
@role_required("admin_departamento", "empleado")
def crear_tarea():
    data = request.json
    nueva_tarea = Tarea.crear(data)
    return jsonify(nueva_tarea), 201

@tarea_bp.route("/", methods=["GET"])
def get_tareas():
    tareas = ["Tarea 1", "Tarea 2", "Tarea 3"]  # Simulación
    return render_template("tareas.html", tareas=tareas)