# from app import app
from flask import request, render_template, url_for
from model.user_model import User_model

class UserController:
    def __init__(self, app):
        self.app = app
        self.obj = User_model()

    def user_getall_controller(self):
        return self.obj.user_getall_model()

    def user_addone_controller(self, data):
        return self.obj.user_addone_model(data)

    def user_update_controller(self, data):
        return self.obj.user_update_model(data)

    def user_delete_controller(self, id):
        return self.obj.user_delete_model(id)

    def user_patch_controller(self, data, id):
        return self.obj.user_patch_model(data, id)
