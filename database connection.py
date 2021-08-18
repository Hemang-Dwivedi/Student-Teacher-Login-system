import bcrypt
import mongoengine as mongoDB
from flask import Flask, jsonify, request, make_response
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from pymongo import MongoClient
from flask_socketio import SocketIO, send, emit
import random

app = Flask(__name__)
DB_URI = 'mongodb+srv://Admin:admin%40123@cluster0.1lkj9.mongodb.net/csproject?retryWrites=true&w=majority'
mongoDB.connect("csproject", host=DB_URI)
app = Flask(__name__)
CORS(app)
users = MongoClient(DB_URI)


class users(mongoDB.Document):
    userid = mongoDB.StringField(required=True)
    password = mongoDB.StringField(required=True)

    def __init__(self, userid, password, *args, **kwargs):
        super(mongoDB.Document, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.password = password
        self.userid = userid

    def __str__(self):
        return f'userid: {self.userid}, password: {self.password} '


@app.route('/login/<userid>/<password>', methods=['GET'])
def login(userid, password):
    user = users.objects(userid=userid).first()
    if not userid or not password:
        return make_response('Email or password Not Found', 401)
    if not user:
        return make_response('User not found, Please enter a valid user', 402)
    if user['password'] != password:
        return make_response('Incorrect Password', 403)
    return make_response('Success', 200)


# if condition to check name is equal to main to generate a script
if __name__ == '__main__':
    # debug=True is used when we didn't saved changes by need output to
    app.run(debug=True)
