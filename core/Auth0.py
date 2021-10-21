from flask import jsonify, request
from config import Config

def autenticacion():

    if 'x-access-tokens' in request.headers:

        token = request.headers['x-access-tokens']

        if token == Config.key:
            
            return 1
        else:
            return {'error': 1, 'message': f'El key-api {token} es incorrecto'}
    else:
        return {'error': 1, 'message': 'Falta key-api para el acceso.'}