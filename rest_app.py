from flask import Flask, request
import db_connector
import pymysql
import os
import signal

app = Flask(__name__)

# local users storage
users = {}
# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):

    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        does_user_exist = db_connector.select_db(user_id) # check if user exists before adding
        if does_user_exist is None:
            db_connector.insert_db(user_id,user_name)
            return {'status': 'ok', 'user_added': user_name}, 200 # status code
        else:
            return {'status': 'error', 'reason': 'id already exists'}, 500 # error status code

    elif request.method == 'GET':
        user_name = db_connector.select_db(user_id)
        if user_name is not None:
            return {'status': 'ok', 'user_name': user_name}, 200 # status code
        else:
            return {'status': 'error', 'reason': 'id not found'}, 500 # error status code

    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        does_user_exist = db_connector.select_db(user_id)
        if does_user_exist is not None:
            db_connector.update_db(user_id, user_name)
            return {'user_id': user_id, 'user_updated': users[user_id]}, 200 # status code
        else:
            return {'status': 'error', 'reason': 'no such id'}, 500 # error status code

    elif request.method == 'DELETE':
        does_user_exist = db_connector.select_db(user_id)
        if does_user_exist is not None:
            db_connector.delete_db(user_id)
            return {'user_id': user_id, 'user_deleted': user_id}, 200 # status code
        else:
            return {'status': 'error', 'reason': 'no such id'}, 500 # error status code


@app.route('/stop_server')
def stop_server():
   os.kill(os.getpid(), signal.CTRL_C_EVENT)
   return 'Server stopped'

# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5000)
