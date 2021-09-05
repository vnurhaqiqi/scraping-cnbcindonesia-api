from flask import Response
from .helpers import *
import json


class APIResponse(Response):
    """
    ============ EXAMPLE ============
    1. set_status(200)
    2. set_content({"Hello": "World"})
    3. get_response()
    """

    def __init__(self):
        super().__init__()
        self.data_response = {
            "data": [],
            "status": None,
            "message": "",
        }

    # set response status first given by code
    # then you will get status message by automatically
    def set_status(self, code):
        status_code = code
        self.data_response['status'] = status_code
        self.set_message()

    # call in set_status() function
    def set_message(self):
        message = STATUS_CODE[self.data_response['status']]
        self.data_response['message'] = message

    # use this function to add the data to response
    def set_content(self, content):
        self.data_response['data'] = content

    # last function to call, getting response json
    def get_response(self):
        response = Response(
            response=json.dumps(self.data_response),
            status=self.status_code,
            mimetype='application/json'
        )

        return response
