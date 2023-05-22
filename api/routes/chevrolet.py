from flask import Blueprint, request, jsonify, current_app

from api.models.entities.Login import Login
from api.models.ChevroletModel import ChevroletModel

chevrolet = Blueprint('chevrolet', __name__)

@chevrolet.route('/api/v1/chevrolet', methods=['GET'])
def get_all(self):

    return jsonify({'message': 'successfully'})


@chevrolet.route('/api/v1/login/<usuario>/<contrasena>', methods=['GET'])
def login_chevrolet(usuario, contrasena):
    try:
        movie = ChevroletModel.login_chevrolet(usuario, contrasena)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@chevrolet.route('/api/v1/login/add-user', methods=['POST'])
def add_user():
    try:
        requestData = request.json[0];
        usuario = requestData['usuario']
        contrasena = requestData['contrasena']
        tipo_usuario = requestData['tipo_usuario']
        login = Login(usuario, contrasena, tipo_usuario)
        
        print(login)

        affected_rows = ChevroletModel.create_user(login)
        print(affected_rows)

        if affected_rows == 1:
            return jsonify(login.usuario)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        print("fff")
        print(ex)
        return jsonify({'message': str(ex)}), 500