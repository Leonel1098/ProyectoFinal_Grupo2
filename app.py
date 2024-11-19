from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from config import Config

# Inicializar aplicación
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar extensiones
mongo = PyMongo(app)
jwt = JWTManager(app)

# Registrar rutas
from routes.login_routes import auth_bp
from routes.empresa_routes import empresa_bp
from routes.departamento_routes import departamento_bp
from routes.tarea_routes import tarea_bp
from routes.usuario_routes import usuario_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(empresa_bp, url_prefix="/empresas")
app.register_blueprint(departamento_bp, url_prefix="/departamentos")
app.register_blueprint(tarea_bp, url_prefix="/tareas")
app.register_blueprint(usuario_bp, url_prefix="/usuarios")

if __name__ == "__main__":
    app.run(debug=True)
