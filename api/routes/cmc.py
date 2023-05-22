from flask import Blueprint, request, jsonify, current_app


cmc = Blueprint('cmc', __name__)

@cmc.route('/api/v1/cmc', methods=['GET'])
def get_all():

    return jsonify({'message': 'successfully'})