from flask import Blueprint, jsonify
from models import User


user_blueprint = Blueprint('user_api_routes', __name__, url_prefix='/api/user')


@user_blueprint.route('/all', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = [user.serialize() for user in users]
    
    response = {
        'message': 'success',
        'result': result
    }
    
    return jsonify(response)
