from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource
from .helpers.response import APIResponse

import os

app = Flask(__name__)
api = Api(app)
CORS(app)

from .routes import route

if __name__ == '__main__':
    app.run(debug=True)
