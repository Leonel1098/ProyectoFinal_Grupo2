from flask import Flask, redirect, url_for
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS


# Inicializar aplicación
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
# Inicializar extensiones
mongo = PyMongo(app)
jwt = JWTManager(app)

# Registrar rutas
from routes.login_routes import usuario_bp
from routes.empresa_routes import empresa_bp
from routes.departamento_routes import departamento_bp
from routes.tareas_routes import tarea_bp


app.register_blueprint(usuario_bp, url_prefix="/usuarios")
app.register_blueprint(empresa_bp, url_prefix="/empresas")
app.register_blueprint(departamento_bp, url_prefix="/departamento")
app.register_blueprint(tarea_bp, url_prefix="/tareas")


@app.route('/')
def home():
    return redirect(url_for('login.login.html')) 



if __name__ == "__main__":
    app.run(debug=True)
