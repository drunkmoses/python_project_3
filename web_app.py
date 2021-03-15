from flask import Flask, request
import db_connector
import os
import signal


app = Flask(__name__)

@app.route('/users/get_user_data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def get_user_data(user_id):
    user_name = db_connector.select_db(user_id) # checks to see if user_name exists in DB, otherwise, display no user found.
    if user_name is not None:
        return f"""
        <div id="a">
        <h1 style='color: red;'> {user_name}
        <id user= {user_name} ></h1>
        </div>
        """
    else:
        return "<h1 style='color: red;'> <id='user'> No user found!</h1>"

@app.route('/stop_server')
def stop_server():
   os.kill(os.getpid(), signal.CTRL_C_EVENT)
   return 'Server stopped'

# host is pointing at local machine address
# # debug is used for more detailed logs + hot swaping
# # the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5001)
