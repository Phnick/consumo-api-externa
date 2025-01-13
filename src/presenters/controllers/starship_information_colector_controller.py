from presenters.interface.controllers import ControllersInterface
from domain.usecase.starships_information_colector import StarshipInformationColectorInterface
from typing import Dict, Type


class StarshipInformationColectorController(ControllersInterface):
    '''Controller to strashipsInformationColector'''

    def __init__(self, starshipe_information_colector: Type[StarshipInformationColectorInterface]):
        self.__use_case = starshipe_information_colector

    def handler(self, http_request: Dict):
        page = http_request["query_params"]["page"]
        limit = http_request["query_params"]["limit"]
        starship_id = http_request["body"]["starship_id"]

        starship_information = self.__use_case.find_starship(
            int(starship_id), int(page), int(limit))
        http_response = {"status_code": 200,
                         "data": {"data": starship_information}}
        return http_response
