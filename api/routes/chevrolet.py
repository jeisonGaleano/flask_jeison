from flask import Blueprint, request, jsonify, current_app



chevrolet = Blueprint('chevrolet', __name__)

@chevrolet.route('/api/v1/chevrolet', methods=['GET'])
def get_all(self):

    return jsonify({'message': 'successfully'})