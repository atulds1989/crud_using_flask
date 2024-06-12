from app import app
from flask import request, render_template, url_for
from model.user_model import User_model

obj = User_model()

@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()

@app.route('/user/addone', methods = ['POST'])
def user_addone_controller():
    data = request.form
    return obj.user_addone_model(data)

@app.route('/user/update', methods = ['PUT'])
def user_update_controller():
    data = request.form
    return obj.user_update_model(data)


@app.route('/user/delete/<id>', methods = ['DELETE'])
def user_delete_controller(id):
    # data = request.form
    return obj.user_delete_model(id)


@app.route('/user/patch/<id>', methods = ['PATCH'])
def user_patch_controller(id):
    data = request.form
    return obj.user_patch_model(data, id)