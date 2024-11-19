from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://gonzalezleonel1098:Leonel10@cluster0.uapuf.mongodb.net/")
db = client["Gestor_Tareas"]

class Usuario:
    collection = db["Usuarios"]

    @staticmethod
    def crear_usuario(data):
        """Inserta un nuevo usuario en la colección."""
        usuario = {
            "nombre": data["nombre"],
            "email": data["email"],
            "password": data["password"],
            "rol": data["rol"],
            "empresa_id": data.get("empresa_id"),  # Puede ser None
            "departamento_id": data.get("departamento_id")  # Puede ser None
        }
        result = Usuario.collection.insert_one(usuario)
        return str(result.inserted_id)

    @staticmethod
    def obtener_usuario_por_email(email):
        """Busca un usuario por su email."""
        return Usuario.collection.find_one({"email": email})

    @staticmethod
    def obtener_usuario_por_id(user_id):
        """Busca un usuario por su ID."""
        return Usuario.collection.find_one({"_id": ObjectId(user_id)})
