from domain.usecase.starships_list_colector import StarshipsColectorInterface
from typing import Type, Dict, List
from data.interface.api_consumer import ApiConsumerInterface
from errors.http_unprocessable_entity import HttpUnprocessableEntityError


class StarshipsColector(StarshipsColectorInterface):
    '''StarshipsColector usecase'''

    def __init__(self, api_consumer: Type[ApiConsumerInterface]):
        self.__api_consumer = api_consumer

    # retunr list dict
    def list(self, page: int, limit: int):
        starship_list = self.__search_list(page, limit)
        print(starship_list)
        starship_formated_list = self.__format_api_response_list(
            starship_list.response.get("results", [])
        )

        return starship_formated_list

    def __search_list(self, page: int, limit: int):
        self.__validate_params(page, limit)
        api_response = self.__api_consumer.get_starships(page, limit)
        return api_response

    def __validate_params(self, page: int, limit: int):
        if page > 35:
            raise HttpUnprocessableEntityError('Page deve ser de 1 a 35')
        if limit > 10:
            raise HttpUnprocessableEntityError('limit deve ser de 1 a 10')

    @classmethod
    def __format_api_response_list(cls, results: List[Dict]):
        '''Response model'''
        starships_formated_list = []

        for starship in results:

            starships_formated_list.append(
                {
                    "name": starship.get("name", "Desconhecido"),
                    "url": starship.get("url", "Desconhecido"),
                    "uid": starship.get("uid", "Desconhecido"),
                }
            )

        return starships_formated_list
