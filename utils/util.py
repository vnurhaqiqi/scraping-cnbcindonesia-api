from ..app import *


class HelloWorld(Resource):
    def get(self):
        return {"Hello": "World"}
