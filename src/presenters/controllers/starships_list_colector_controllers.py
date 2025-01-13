from domain.usecase.starships_list_colector import StarshipsColectorInterface
from presenters.interface.controllers import ControllersInterface
from typing import Dict, Type


class StarshipsListColectorController(ControllersInterface):
    '''Controller to list Starships'''

    def __init__(self, starships_colector: Type[StarshipsColectorInterface]):
        self.use_case = starships_colector

    def handler(self, http_request: Dict):
        page = http_request["query_params"]["page"]
        limit = http_request["query_params"]["limit"]
        starships_list = self.use_case.list(int(page), int(limit))
        http_response = {"status_code": 200, "data": {"data": starships_list}}
        return http_response
