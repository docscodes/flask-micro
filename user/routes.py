from flask import Blueprint, jsonify, request, make_response
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user


user_blueprint = Blueprint('user_api_routes', __name__, url_prefix='/api/user')


@user_blueprint.route('/all', methods=['GET'])
def get_all_users():
    """
    get_all_users
    ---
    tags:
      - Users
    summary: Get all users
    description: Fetch a list of all registered users in the system.
    responses:
      200:
        description: A list of users retrieved successfully.
        schema:
          type: object
          properties:
            message:
              type: string
              example: success
            result:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    example: 1
                  username:
                    type: string
                    example: johndoe
                  api_key:
                    type: string
                    example: 1$xdclRoO2NkSoLGGJ$c90c354c1e151b0f348d4ad474ca58fe0618e
                  is_admin:
                    type: boolean
                    example: false  
                  is_active:
                    type: boolean
                    example: true
    """
    users = User.query.all()
    result = [user.serialize() for user in users]
    
    response = {
        'message': 'success',
        'result': result
    }
    
    return jsonify(response)


@user_blueprint.route('/create', methods=['POST'])
def create_user():
    """
    create_user
    ---
    tags:
      - Users
    summary: Create a new user
    description: Create a new user by providing a username and password. Password is securely hashed using scrypt.
    consumes:
      - multipart/form-data
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: The username for the new user.
      - name: password
        in: formData
        type: string
        required: true
        description: The password for the new user.
    responses:
      200:
        description: User successfully created
        schema:
          type: object
          properties:
            message:
              type: string
              example: User Created
            result:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                username:
                  type: string
                  example: johndoe
                is_admin:
                  type: boolean
                  example: false
      500:
        description: Error in creating response
        schema:
          type: object
          properties:
            message:
              type: string
              example: Error in creating response
    """
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


@user_blueprint.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    
    if not user:
        response = {'message': 'username does not exists'}
        return make_response(jsonify(response), 401)
    
    if check_password_hash(user.password, password):
        user.update_api_key()
        db.session.commit()
        
        login_user(user)
        
        response = {'message': 'logged in ', 'api_key': user.api_key}
        return make_response(jsonify(response), 200)

    response = {'message': 'Access denied'}
    return make_response(jsonify(response), 401)


@user_blueprint.route('/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({'message': 'logged out'})
    return jsonify({'message': 'No user logged in'}), 401


@user_blueprint.route('/<username>/exists', methods=['GET'])
def user_exists(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"result": True}), 200

    return jsonify({"result": False}), 404


@user_blueprint.route('/', methods=['GET'])
def get_current_user():
    if current_user.is_authenticated:
        return jsonify({'result': current_user.serialize()}), 200
    else:
        return jsonify({'message': "User not logged in"}), 401
