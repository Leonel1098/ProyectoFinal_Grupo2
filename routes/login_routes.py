from flask import Blueprint, flash, redirect, render_template, request, jsonify, session, url_for
from flask_jwt_extended import create_access_token
from models.model_usuario import Usuario
from utils.hash_util import check_password, hash_password
from config import socket_io

usuario_bp = Blueprint("login", __name__)

@usuario_bp.route("/", methods=["GET", "POST"])
def root():
    # Redirigir la raíz a la página de login
    return redirect(url_for('login.login'))  # Redirige a la ruta /login

@usuario_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # Renderiza el formulario de login
        return render_template("login.html")

    elif request.method == "POST":
        # Captura datos enviados desde el formulario
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return render_template("login.html", error="Todos los campos son obligatorios.")

        # Busca al usuario en la base de datos
        usuario = Usuario.obtener_usuario_por_email(email)
        if not usuario or not check_password(password, usuario["password"]):
            return render_template("login.html", error="Credenciales inválidas.")

        # Genera el token si las credenciales son válidas
        token = create_access_token(identity={
            "id": str(usuario["_id"]),
            "rol": usuario["rol"],
            "empresa_id": usuario.get("empresa_id"),
            "departamento_id": usuario.get("departamento_id")
        })

        # Guarda el usuario en la sesión para usarlo en el dashboard
        session["usuario"] = {
            "id": str(usuario["_id"]),
            "nombre": usuario["nombre"],
            "rol": usuario["rol"],
            "email": usuario["email"]
        }

        # Redirige al dashboard tras el inicio de sesión exitoso
        return redirect(url_for("login.dashboard"))

@usuario_bp.route("/dashboard")
def dashboard():
    # Verifica si el usuario está autenticado
    if "usuario" not in session:
        return redirect(url_for("login.login"))  # Redirigir al login si no hay sesión

    # Obtiene los datos del usuario desde la sesión
    usuario = session["usuario"]

    # Renderiza la página del dashboard
    return render_template("dashboard.html", usuario=usuario)

@usuario_bp.route("/registrar", methods=["GET", "POST"])
def registrar_usuario():
    if request.method == "GET":
        # Renderiza la plantilla de registro de usuarios
        return render_template("registro.html")

    if request.method == "POST":
        # Obtén los datos del formulario
        data = request.form
        nombre = data.get("nombre")
        email = data.get("email")
        password = data.get("password")
        rol = data.get("rol", "empleado")  # Rol por defecto: "empleado"
        departamento_id = data.get("departamento_id")  # Nuevo campo: departamento al que pertenece

        # Validar datos
        if not nombre or not email or not password or not departamento_id:
            flash("Faltan campos requeridos", "error")
            return render_template("registro.html")

        # Hashea la contraseña
        hashed_password = hash_password(password)

        # Crear el usuario en la base de datos
        nuevo_usuario = Usuario(
            nombre=nombre,
            email=email,
            password=hashed_password,
            rol=rol,
            departamento_id=departamento_id
        )
        resultado = Usuario.crear_usuario(nuevo_usuario)
        socket_io.emit('nuevo_usuario', {'nombre': 'Nuevo Usuario', 'email': 'nuevo@email.com'})
        if resultado:
            #return jsonify({"msg": "Usuario registrado con éxito"}), 201
            return redirect(url_for("login.login"))
        else:
            #return jsonify({"msg": "Error al registrar el usuario"}), 500
            return render_template("registro.html")

@usuario_bp.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login.login"))
