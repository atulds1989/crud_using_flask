from flask import Flask, request
import os

from flask import request, render_template, url_for
# from model.user_model import User_model
# from controller.user_controller import UserController

# obj = User_model()
# obj = UserController()

app = Flask(__name__)
@app.route('/')
def welcome():
    return "welcome page"



from controller import *


if __name__=='__main__':
    app.run(debug=True)
    
