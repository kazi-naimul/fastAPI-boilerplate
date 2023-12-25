from typing import List, Optional, Union

class ApiServiceResponse:
    def __init__(
        self,
        status: bool,
        code: int,
        message: str,
        data: Optional[Union[List, dict]] = None,
        errors: Optional[Union[List, dict]] = None,
    ):
        self.status = status
        self.code = code
        self.message = message
        self.data = data
        self.errors = errors

class ResponseBuilder:
    def __init__(self):
        self.response = ApiServiceResponse(
            status=True,
            code=200,
            message='Successful',
        )

    def status(self, response_status: bool):
        self.response.status = response_status
        return self

    def code(self, response_code: int):
        self.response.code = response_code
        return self

    def message(self, response_message: str):
        self.response.message = response_message
        return self

    def data(self, response_data: Optional[Union[List, dict]]):
        if response_data is not None:
            self.response.data = response_data
        return self

    def errors(self, response_errors: Optional[Union[List, dict]]):
        self.response.status = False
        if response_errors is not None:
            self.response.errors = response_errors
        return self

    def build(self):
        response = self.response
        self.reset()
        return response

    def reset(self):
        self.response = ApiServiceResponse(
            status=True,
            code=200,
            message='Successful',
        )

    @staticmethod
    def get_instance():
        return ResponseBuilder()
