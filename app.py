from flask import Flask, request
import os

# app = Flask(__name__)
# @app.route('/')
# def welcome():
#     return "welcome page"



# from controller import *

# @app.route('/home')
# def home():
#     return 'this is home page'


# from controller import user_controller
# from controller import product_controller


# if __name__=='__main__':
#     app.run(debug=True)
    


from flask import Flask
from controller.user_controller import UserController

app = Flask(__name__)

# Create an instance of UserController and pass the app object
user_controller = UserController(app)

# Define routes
@app.route('/')
def welcome():
    return "welcome page"

@app.route('/user/getall')
def user_getall():
    return user_controller.user_getall_controller()

@app.route('/user/addone', methods=['POST'])
def user_addone():
    return user_controller.user_addone_controller(request.form)

@app.route('/user/update', methods=['PUT'])
def user_update():
    return user_controller.user_update_controller(request.form)

@app.route('/user/delete/<id>', methods=['DELETE'])
def user_delete(id):
    return user_controller.user_delete_controller(id)

@app.route('/user/patch/<id>', methods=['PATCH'])
def user_patch(id):
    return user_controller.user_patch_controller(request.form, id)

if __name__ == '__main__':
    app.run()
