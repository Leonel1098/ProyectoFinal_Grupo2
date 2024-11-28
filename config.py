import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://gonzalezleonel1098:Leonel10@cluster0.uapuf.mongodb.net/Gestion_Tareas")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret_key")


from flask_socketio import SocketIO
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

socket_io = SocketIO()  # Inicialización diferida
mongo = PyMongo()
jwt = JWTManager()