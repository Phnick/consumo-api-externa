from domain.usecase.starships_information_colector import StarshipInformationColectorInterface
from typing import Type, Dict
from data.interface.api_consumer import ApiConsumerInterface
from errors.http_not_found import HttpNotFoundError
from errors.http_unprocessable_entity import HttpUnprocessableEntityError


class StarshipInformationColector(StarshipInformationColectorInterface):
    '''StarshipInformationColector UseCase'''

    def __init__(self, api_consumer: Type[ApiConsumerInterface]):
        self.__api_consumer = api_consumer

    # return dict
    def find_starship(self, starship_id: int, page: int, limit: int):
        starship_information = self.__search_starships(
            starship_id, page, limit)

        print(starship_information)
        starship_formated_list = self.__format_api_response_starship(
            starship_information.response.get("result").get("properties")
        )
        return starship_formated_list

    def __search_starships(self, starship_id: int, page: int, limit: int):
        self.__validate_params(starship_id, page, limit)
        api_response = self.__api_consumer.get_starships_by_id(
            starship_id, page, limit)
        return api_response

    def __validate_params(self, starship_id: int, page: int, limit: int):
        if not starship_id:
            raise HttpNotFoundError('Id inválido')
        if starship_id < 2 or starship_id > 75:
            raise HttpUnprocessableEntityError('id deve ser entre 2 a 75')
        if page > 35:
            raise HttpUnprocessableEntityError('Page deve ser de 1 a 35')
        if limit > 10:
            raise HttpUnprocessableEntityError('limit deve ser de 1 a 10')

    @classmethod
    def __format_api_response_starship(cls, starships_information: Dict):
        '''Response model'''
        starship = starships_information

        starships_formated = (
            {
                "model": starship.get("model", "Desconhecido"),
                "starship_class": starship.get("starship_class", "Desconhecido"),
                "max_atmosphering_speed": starship.get("max_atmosphering_speed", "Desconhecido"),
            }
        )

        return starships_formated
