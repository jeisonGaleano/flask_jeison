from flask import Blueprint, request, jsonify, current_app

from api.models.entities.Cmc import Cmc
from api.models.CmcModel import CmcModel

cmc = Blueprint('cmc', __name__)

@cmc.route('/api/v1/cmc', methods=['GET'])
def get_all():

    try:            
        chevrolet = CmcModel.get_data_cmc()
        return jsonify(chevrolet)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500  