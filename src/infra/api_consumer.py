import requests
from requests import Request
from typing import Type
from collections import namedtuple
from errors.http_request_error import HttpRequesError
from data.interface.api_consumer import ApiConsumerInterface


class ApiConsumer(ApiConsumerInterface):
    '''Class to consume Api with http requests'''

    def __init__(self):
        # heare i standardized my response for the request
        self.get_starships_response = namedtuple(
            'GET_starships', 'status_code request response')
        self.get_starships_by_id_response = namedtuple(
            'GET_starships_info', 'status_code request response')

    def get_starships(self, page: int, limit: int):
        url = 'https://www.swapi.tech/api/starships'

        params = {
            "page": page,
            "limit": limit
        }

        req = requests.Request(
            method='GET',
            url=url,
            params=params
        )

        # I'm preparing my request to be sent via http
        req_preper = req.prepare()
        print(f"URL gerada: {req_preper.url}")

        response = self.send_http_request(req_preper)
        status_code = response.status_code

        if (status_code >= 200 and status_code <= 299):
            return self.get_starships_response(
                status_code=status_code, request=req, response=response.json()
            )
        else:
            raise HttpRequesError(
                message=response.json()["message"], status_code=status_code
            )

    def get_starships_by_id(self, starship_id: int, limit: int, page: int):

        url = f'https://www.swapi.tech/api/starships/{starship_id}'
        params = {
            "page": page,
            "limit": limit
        }
        req = requests.Request(
            method='GET',
            url=url,
            params=params
        )
        req_preper = req.prepare()
        print(f"URL gerada: {req_preper.url}")

        response = self.send_http_request(req_preper)
        status_code = response.status_code

        if (status_code >= 200 and status_code <= 299):
            return self.get_starships_by_id_response(
                status_code=status_code, request=req, response=response.json()
            )
        else:
            raise HttpRequesError(
                message=response.json()["message"], status_code=status_code
            )

    # A God situation is when you have many request. If there were not multiple requests or high control, a good situation would be faster with only one (request.get)

    @classmethod
    def send_http_request(cls, req_preper: Type[Request]):
        '''
            Prepare a session and send Http request
            :param - req_prepared : Request object with all params
            :response - http response raw
        '''
        http_session = requests.Session()
        response = http_session.send(req_preper)
        return response
