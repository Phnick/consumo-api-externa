from typing import Type, Dict
from errors.http_not_found import HttpNotFoundError
from errors.http_unprocessable_entity import HttpUnprocessableEntityError


def handler_error(error: Type[Exception]) -> Dict:
    if isinstance(error, HttpNotFoundError):
        return {
            "data": {"error": error.message},
            "status_code": error.status_code
        }
    elif isinstance(error, HttpUnprocessableEntityError):
        return {
            "data": {"error": error.message},
            "status_code": error.status_code
        }
    else:
        return {
            "data": {"error": str(error)},
            "status_code": 500
        }
