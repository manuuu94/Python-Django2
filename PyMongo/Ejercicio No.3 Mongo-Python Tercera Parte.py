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

cliente=pymongo.MongoClient(mongo_uri,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
basedatos=cliente[MONGO_BASEDATOS]
coleccion=basedatos[MONGO_COLECCION]

def mostrardatos(tabla):
    try:
        registros=tabla.get_children()
        for registro in registros:
            tabla.delete(registro)
        for documento in coleccion.find():
            tabla.insert('',0,text=documento["sexo"],values=documento["nombre"])
        cliente.close()
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo extendido"+errorTiempo)
    except pymongo.errors.ConectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb"+errorConexion)  
ventana =Tk()
tabla=ttk.Treeview(ventana,columns=2)
tabla.grid(row=1,column=0,columnspan=2)
tabla.heading("#0",text="SEXO")
tabla.heading("#1",text="NOMBRE")
mostrardatos(tabla)
ventana.mainloop()


