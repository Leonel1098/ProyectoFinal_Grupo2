@tarea_bp.route("/", methods=["POST"])
@role_required("admin_departamento", "empleado")
def crear_tarea():
    data = request.json
    nueva_tarea = Tarea.crear(data)
    return jsonify(nueva_tarea), 201
