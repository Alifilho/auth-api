from flask import Blueprint, jsonify, request

from services.UserService import UserService

# from models import User

routes = Blueprint('user', __name__)
repository = UserService()


@routes.route('/users', methods=['GET'])
def index():
    users_list = list()
    result = repository.get_all_sync()
    for user in result:
        users_list.append(
            {'id': str(user['_id']), 'name': user['name'], 'email': user['email'], 'password': user['password'],
             'age': user['age']})
    return jsonify(users_list)


@routes.route('/users', methods=['POST'])
def store():
    new_user = request.json
    result = repository.save_sync(new_user)
    if result.acknowledged:
        return jsonify({'id': str(result.inserted_id), 'name': new_user['name'], 'email': new_user['email'],
                        'password': new_user['password'],
                        'age': new_user['age']})


@routes.route('/users', methods=['PUT'])
def update():
    user_id = request.args.get('id')
    updates = request.json
    result = repository.update_sync(user_id, updates)
    return jsonify({'id': str(result['_id']), 'name': result['name'], 'email': result['email'],
                    'password': result['password'],
                    'age': result['age']})


@routes.route('/users', methods=['DELETE'])
def destroy():
    user_id = request.args.get('id')
    result = repository.delete_sync(user_id)
    return jsonify({'id': str(result['_id']), 'name': result['name'], 'email': result['email'],
                    'password': result['password'],
                    'age': result['age']})
