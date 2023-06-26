from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymongo

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000
mongo_uri="mongodb://"+ MONGO_HOST+":"+ MONGO_PUERTO
print(mongo_uri)
MONGO_BASEDATOS="Escuela"
MONGO_COLECCION="Alumnos"

try:
  cliente=pymongo.MongoClient(mongo_uri,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
  basedatos=cliente[MONGO_BASEDATOS]
  coleccion=basedatos[MONGO_COLECCION]
  cliente.server_info()
  print("Conexion a Mongo exitosa")
  cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo extendido"+ errorTiempo)
except pymongo.errors.OperationFailure as error:
    print(error)
    quit(1) 