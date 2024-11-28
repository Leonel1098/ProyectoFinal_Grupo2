from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://gonzalezleonel1098:Leonel10@cluster0.uapuf.mongodb.net/?tls=true")
db = client["Gestion_Tareas"]

class Usuario:
    def __init__(self, nombre, email, password, rol="empleado", departamento_id=None):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.rol = rol
        self.departamento_id = departamento_id

    
    @staticmethod
    def crear_usuario(usuario):
        collection = db["Empleados"]
        try:
            # Inserta el usuario en la base de datos
            resultado = collection.insert_one({
                "nombre": usuario.nombre,
                "email": usuario.email,
                "password": usuario.password,
                "rol": usuario.rol,
                "departamento_id": usuario.departamento_id  # Guarda el departamento
            })
            return resultado.acknowledged
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False

    @staticmethod
    def obtener_usuario_por_email(email):
        try:
            collection = db["Empleados"]
            return collection.find_one({"email": email})
        except Exception as e:
            print(f"Error al buscar usuario: {e}")
            return None

