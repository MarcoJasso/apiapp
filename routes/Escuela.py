import json
from server import Server

server = Server.conectar()


def initSchools():
    return {'error': 0, 'message': 'Apartado de escuelas registradas'}


def addSchools(key):

    datos = json.loads(key)

    if server != None:

        if validateKey(datos) == 0:
            cursor = server.cursor()

            cursor.execute(""" INSERT INTO schools(key_school, name_school, key_user) VALUES ('{}', '{}', '{}') """.format(
                datos['key_school'], datos['name_school'], datos['key_user']))

            server.commit()

            return {"error": 0, "message": "Datos Guardados exitosamente."}
        else:
            return {"error": 1, "message": f"La escuela con la clave {datos['key_school']} ya se encuentra registrada."}
    else:

        return {"error": 1, "message": "Oops!, No se ha encontrado conexion a la base de datos."}


def getSchools(key):
    
    if server != None:

        cursor = server.cursor()

        cursor.execute(f""" SELECT * FROM schools WHERE key_user = '{key}'; """)

        if cursor.rowcount == 0:

            return {"error": 1, "message": "Oops!, No se han encontrado escuelas registradas"}

        else:

            lista_escuelas = []
            respuesta = cursor.fetchall()

            for escuela in respuesta:
                datos = {
                    'key_': escuela[1],
                    'name_': escuela[2]
                }

                lista_escuelas.append(datos)

            return {'error': 0, 'message': lista_escuelas}
    else:
        return {"error": 1, "message": "Oops!, No se ha encontrado conexion a la base de datos."}


def deleteSchools(data):
    
    if server != None:

        data = json.loads(data)

        if validateKey(data) == 0:

            cursor = server.cursor()

            cursor.execute(""" DELETE FROM schools WHERE key_school = '{}';""".format(data['key_school']))

            if  server.commit() :
                return {"error": 0, "message": "La escuela ha sido eliminada."}
            else:
                return {"error": 1, "message": "La escuela no pudo ser eliminada."}

        else:
            return {"error": 1, "message": "Oops!, No se ha encontrado registros."}

    else:
       return {"error": 1, "message": "Oops!, No se ha encontrado conexion a la base de datos."}


def updateSchools(data):
    
    if server != None:

        data = json.loads(data)

        cursor = server.cursor()

        if validateKey(data) == 1:

            cursor.execute(""" UPDATE schools SET name_school = '{}' WHERE key_school = '{}' AND key_user = '{}'; """.format(data['name_school'], data['key_school'], data['key_user']))

            if  server.commit() :
                return {"error": 1, "message": "Oops!, No se fue posible actualizar los datos."}
            else:
                return {"error": 0, "message": "Se ha actualizado correctamente los datos."}

        else:
            
            return {"error": 1, "message": f"Oops!, No se ha encontrado la escuela para modificar. {data['key_school']}"}
    else:
       return {"error": 1, "message": "Oops!, No se ha encontrado conexion a la base de datos."}


def searchOneSchools(data):
    
    if server != None:

        data = json.loads(data)

        if validateKey(data) == 1:

            cursor = server.cursor()
            cursor.execute(""" SELECT * FROM schools WHERE key_school = '{}' AND key_user = '{}'; """.format(data['key_school'], data['key_user']))

            escuela = cursor.fetchone()

            return {"error": 0, "message": escuela}
            
        else:
            return {"error": 1, "message": "Oops!, No se ha encontrado la escuela solicitada."}

    else:
       return {"error": 1, "message": "Oops!, No se ha encontrado conexion a la base de datos."}     

def searchAllSchools(data):
    
    if server != None:

        data = json.loads(data)
        all_schools = []

        cursor = server.cursor()

        cursor.execute(""" SELECT * FROM schools WHERE name_school ILIKE '%{}%' AND key_user = '{}'; """.format(data['name_school'], data['key_user']))

        if cursor.rowcount == 0:
            return {"error": 1, "message": "Oops!, Sin coincidencia de resultados."}
        else:
            respuesta = cursor.fetchall()

            for school in respuesta:

                item = {
                    'key': school[1],
                    'name': school[2],
                }

                all_schools.append(item)

            return {"error": 0, "message": all_schools}
    else:
        return {"error": 1, "message": "Oops!, No se ha encontrado conexion a la base de datos."}

def validateKey(data):

    if server != None:

        cursor = server.cursor()

        cursor.execute(""" SELECT key_school FROM schools WHERE key_school = '{}' AND key_user = '{}'; """.format(data['key_school'], data['key_user']))

        respuesta = cursor.rowcount

        if respuesta > 0:
            return 1
        else:
            return 0
    else:
        return 1
