from flask import Flask
import os

app = Flask(__name__)
@app.route('/')
def welcome():
    return "welcome page"


# @app.route('/home')
# def home():
#     return 'this is home page'


# from controller import user_controller
# from controller import product_controller

from controller import *

# if __name__=='__main__':
#     app.run(debug=True)
    