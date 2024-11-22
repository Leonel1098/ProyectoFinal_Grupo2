from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb+srv://gonzalezleonel1098:Leonel10@cluster0.uapuf.mongodb.net/")
db = client["Gestor_Tareas"]

class Departamento:
    collection = db["departamentos"]

    @staticmethod
    def crear_departamento(data):
        """Inserta un nuevo departamento en la colección."""
        departamento = {
            "nombre": data["nombre"],
            "empresa_id": ObjectId(data["empresa_id"]),
            "admin_id": ObjectId(data["admin_id"])
        }
        result = Departamento.collection.insert_one(departamento)
        return str(result.inserted_id)

    @staticmethod
    def obtener_por_empresa(empresa_id):
        """Obtiene departamentos por empresa."""
        return list(Departamento.collection.find({"empresa_id": ObjectId(empresa_id)}))
