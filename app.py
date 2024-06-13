from flask import Flask, request
import os
from controller.user_controller import UserController

controller = UserController()

app = Flask(__name__)
@app.route('/')
def welcome():
    return "welcome page"

@app.route('/home')
def home():
    return 'this is home page'

@app.route('/user/getall')
def user_getall():
    return controller.user_getall_controller()

@app.route('/user/addone', methods = ['POST'])
def user_addone():
    data = request.form
    return controller.user_addone_controller(data)

@app.route('/user/update', methods = ['PUT'])
def user_update():
    data = request.form
    return controller.user_update_controller(data)

@app.route('/user/delete/<id>', methods = ['DELETE'])
def user_delete(id):
    # data = request.form
    return controller.user_delete_controller(id)


@app.route('/user/patch/<id>', methods = ['PATCH'])
def user_patch(id):
    data = request.form
    return controller.user_patch_controller(data, id)

if __name__=='__main__':
    app.run(debug=True)
    
