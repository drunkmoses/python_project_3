from flask import Flask, request
import db_connector


app = Flask(__name__)

@app.route('/users/get_user_data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def get_user_data(user_id):
    user_name = db_connector.select_db(user_id)
    return f"""
    <h1 style='color: red;'> <id=user> {user_name} </h1>
    <p>User found!</p>
    """


# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5001)