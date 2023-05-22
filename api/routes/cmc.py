from flask import Blueprint, request, jsonify, current_app

from api.models.entities.Cmc import Cmc
from api.models.entities.PeticionesPqr import PeticionesPqr
from api.models.CmcModel import CmcModel
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

cmc = Blueprint('cmc', __name__)

@cmc.route('/api/v1/cmc', methods=['GET'])
def get_all():

    try:            
        chevrolet = CmcModel.get_data_cmc()
        return jsonify(chevrolet)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500 
    
@cmc.route('/api/v1/add/cmc', methods=['POST'])
def add_data():

    try:
        requestData = request.json[0];
        edad_esposa = requestData['edad_esposa']
        educ_de_la_esposa = requestData['educ_de_la_esposa']
        educ_del_esposo = requestData['educ_del_esposo']
        num_de_hijos_nacidos = requestData['num_de_hijos_nacidos']
        religion_de_la_esposa = requestData['religion_de_la_esposa']
        la_esposa_trabaja_ahora = requestData['la_esposa_trabaja_ahora']
        ocupa_del_esposo = requestData['ocupa_del_esposo']       
        indice_de_nivel_de_vida = requestData['indice_de_nivel_de_vida']
        exposicion_a_los_medios = requestData['exposicion_a_los_medios']
        metodo_anticonceptivo_utilizado = requestData['metodo_anticonceptivo_utilizado']

        cmc = Cmc(edad_esposa, educ_de_la_esposa, educ_del_esposo, num_de_hijos_nacidos
                                , religion_de_la_esposa, la_esposa_trabaja_ahora, ocupa_del_esposo, 
                                indice_de_nivel_de_vida, exposicion_a_los_medios, metodo_anticonceptivo_utilizado)
        
        affected_rows = CmcModel.add_data_cmc(cmc)
        print(affected_rows)

        if affected_rows == 1:
            return jsonify(cmc)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        print("ex")
        return jsonify({'message': str(ex)}), 500   
    
@cmc.route('/api/v1/algorithm', methods=['GET'])
def get_all_algorithm():

    try:            
        chevrolet = CmcModel.get_data_cmc()
        
        return jsonify(chevrolet)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500 

@cmc.route('/api/v1/add/pqr', methods=['POST'])
def add_data_pqr():

    try:
        requestData = request.json[0];
        usuario = requestData['usuario']
        correo = requestData['correo']
        mensaje = requestData['mensaje']

        peticiones = PeticionesPqr(usuario, correo, mensaje)
        
        affected_rows = CmcModel.add_data_peticiones(peticiones)
        print(affected_rows)

        if affected_rows == 1:
            return jsonify(peticiones)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        print("ex")
        return jsonify({'message': str(ex)}), 500       
    
    
@cmc.route('/api/v1/pqr', methods=['GET'])
def get_all_pqr():

    try:            
        chevrolet = CmcModel.get_data_pqr()
        return jsonify(chevrolet)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500 