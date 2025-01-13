class HttpRequesError(Exception):
    def __init__(self, message: str, status_code: int):
        ''' Http error '''

        super().__init__(message)
        self.message = message
        self.status_code = status_code
