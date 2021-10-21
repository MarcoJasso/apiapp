
from server import Server

class Querys():

    cursor = None
    connection = Server.conectar()

    def __init__(self):

        if self.connection != None:
            self.cursor = self.connection.cursor()
    
    def addData(self):

        if self.cursor != None:

            return {"error": 0, "message": "exito de conexión"}

        return {"error": 1, "message": "error en la conexion"}


    def getData(self, data):
        pass

    def deleteData(self, data):
        pass

    def searchData(self, data):
        pass

    def validateData(self, data):
        pass
