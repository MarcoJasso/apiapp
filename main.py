from flask import Flask, jsonify, request
from flask_cors import CORS
from core import Auth0
from routes import Escuela
from server.Querys import Querys
query = Querys()

api = Flask(__name__)
CORS(api)

@api.route('/')
def initApi():
    return jsonify({'error': 0, 'message': 'API gestor de asistencia'})

@api.route('/prueba', methods=['GET'])
def prueba():
    return jsonify(query.addData())

@api.route('/main', methods=['GET'])
def mainApi():
    if Auth0.autenticacion() == 1:
        return jsonify({'error': 0, 'message': 'Bienvenido a nuestra API de asistencia.'})
    else:
        return jsonify(Auth0.autenticacion())

@api.route('/main/schools', methods=['GET'])
def schools():
    if Auth0.autenticacion() == 1:
        return jsonify(Escuela.initSchools())
    else:
        return jsonify(Auth0.autenticacion())

@api.route('/main/schools/addschool/<string:data>', methods=['POST'])
def addSchools(data):
    if Auth0.autenticacion() == 1:
        return jsonify(Escuela.addSchools(key=data))
    else:
        return jsonify(Auth0.autenticacion())

@api.route('/main/schools/getschool/<string:key>', methods=['POST'])
def getSchools(key):
    if Auth0.autenticacion() == 1:
        return jsonify(Escuela.getSchools(key=key))
    else:
        return jsonify(Auth0.autenticacion())

@api.route('/main/schools/updateschool/<string:data>', methods=['POST'])
def updateSchools(data):
    if Auth0.autenticacion() == 1:
        return jsonify(Escuela.updateSchools(data=data))
    else:
        return jsonify(Auth0.autenticacion())

@api.route('/main/schools/searchoneschool/<string:key>', methods=['POST'])
def searchOneSchools(key):
    if Auth0.autenticacion() == 1:
        return jsonify(Escuela.searchOneSchools(data=key))
    else:
        return jsonify(Auth0.autenticacion())


@api.route('/main/schools/searchallschool/<string:key>', methods=['POST'])
def searchAllSchools(key):
    if Auth0.autenticacion() == 1:
        return jsonify(Escuela.searchAllSchools(data=key))
    else:
        return jsonify(Auth0.autenticacion())
 

@api.route('/main/schools/deleteschool/<string:data>', methods=['POST'])
def deleteSchools(data):
    if Auth0.autenticacion() == 1:
        return jsonify(Escuela.deleteSchools(key=data))
    else:
        return jsonify(Auth0.autenticacion())


if __name__ == '__main__':
    api.run(debug=True, host='192.168.10.198', port=5000)