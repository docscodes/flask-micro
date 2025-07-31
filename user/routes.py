from flask import Blueprint, jsonify, request
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash


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


@user_blueprint.route('/create', methods=['POST'])
def create_user():
    try:
        user = User()
        user.username = request.form["username"]
        user.password = generate_password_hash(request.form['password'], method='scrypt')

        user.is_admin = False

        db.session.add(user)
        db.session.commit()

        response = {'message': 'User Created', 'result': user.serialize()}
    except Exception as e:
        print(str(e))
        response = {'message': 'Error in creating response'}
    return jsonify(response)
