from src.libraries.response.response_builder import ResponseBuilder

class BaseService:
    def __init__(self):
        self.response_builder = ResponseBuilder()