import pymongo
my_client = pymongo.MongoClient('mongodb+srv://mgonzalez90402:HKfnRDbrIHaNX55O@cluster0.zip0yki.mongodb.net/')

def mostrardatos():
    try:
        print(my_client.server_info()['version'])
        my_database=my_client.Tarea03
        my_collection=my_database.congelados
        print(my_database)
        print(my_collection)
        for documento in my_collection.find():
            print(documento)
            print(documento["nombre"])
        my_client.close()

    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo extendido"+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb"+errorConexion)  



mostrardatos()