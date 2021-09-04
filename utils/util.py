from ..app import *


class HelloWorld(Resource, APIResponse):
    def get(self):
        self.set_status(200)
        self.set_content({"Hello": "World"})

        return self.get_response()
