from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://gonzalezleonel1098:Leonel10@cluster0.uapuf.mongodb.net/?tls=true")
db = client["Gestor_Tareas"]
class Empresa:
    collection = db["Empresas"]

    @staticmethod
    def crear_empresa(data):
        """Inserta una nueva empresa en la colección."""
        empresa = {
            "nombre": data["nombre"],
            "admin_id": ObjectId(data["admin_id"])
        }
        result = Empresa.collection.insert_one(empresa)
        return str(result.inserted_id)

    @staticmethod
    def obtener_todas():
        """Obtiene todas las empresas."""
        return list(Empresa.collection.find())
