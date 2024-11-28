from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://gonzalezleonel1098:Leonel10@cluster0.uapuf.mongodb.net/?tls=true")
db = client["Gestor_Tareas"]
class Tarea:
    collection = db["Tareas"]

    @staticmethod
    def crear_tarea(data):
        """Inserta una nueva tarea en la colección."""
        tarea = {
            "titulo": data["titulo"],
            "descripcion": data["descripcion"],
            "estado": "pendiente",  # Por defecto
            "empleado_id": ObjectId(data["empleado_id"]),
            "departamento_id": ObjectId(data["departamento_id"])
        }
        result = Tarea.collection.insert_one(tarea)
        return str(result.inserted_id)

    @staticmethod
    def obtener_por_empleado(empleado_id):
        """Obtiene tareas asignadas a un empleado."""
        return list(Tarea.collection.find({"empleado_id": ObjectId(empleado_id)}))

    @staticmethod
    def actualizar_estado(tarea_id, nuevo_estado):
        """Actualiza el estado de una tarea."""
        result = Tarea.collection.update_one(
            {"_id": ObjectId(tarea_id)},
            {"$set": {"estado": nuevo_estado}}
        )
        return result.modified_count
