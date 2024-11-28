from flask_socketio import SocketIO
from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from config import Config, mongo,jwt,socket_io
from flask_cors import CORS


# Inicializar aplicación
app = Flask(__name__)

app.config.from_object(Config)
CORS(app)

# Inicializar extensiones
mongo.init_app(app)
jwt.init_app(app)
socket_io.init_app(app)

# Registrar rutas
from routes.login_routes import usuario_bp
from routes.empresa_routes import empresa_bp
from routes.departamento_routes import departamento_bp
from routes.tareas_routes import tarea_bp


app.register_blueprint(usuario_bp,url_prefix="/usuarios")
app.register_blueprint(empresa_bp, url_prefix="/empresas")
app.register_blueprint(departamento_bp, url_prefix="/departamento")
app.register_blueprint(tarea_bp, url_prefix="/tareas")

@socket_io.on('nuevo_usuario')
def handle_nuevo_usuario(data):
    print('Nuevo usuario registrado:', data)
    # Aquí, puedes emitir un mensaje de confirmación a los clientes
    socket_io.emit('nuevo_usuario', data)

if __name__ == "__main__":
    socket_io.run(app, debug=True)
