@departamento_bp.route("/", methods=["POST"])
@role_required("admin_empresa")
def crear_departamento():
    data = request.json
    nuevo_departamento = Departamento.crear(data)
    return jsonify(nuevo_departamento), 201

