from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymongo

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000
mongo_uri="mongodb://"+ MONGO_HOST+":"+ MONGO_PUERTO

MONGO_BASEDATOS="Escuela"
MONGO_COLECCION="Alumnos"

try:
  cliente=pymongo.MongoClient(mongo_uri,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
  basedatos=cliente[MONGO_BASEDATOS]
  coleccion=basedatos[MONGO_COLECCION]
  for documento in coleccion.find():
    print(documento["nombre"]+" "+documento["sexo"])
  cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo extendido"+ errorTiempo)
except pymongo.errors.ConectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb"+ errorConexion)      

