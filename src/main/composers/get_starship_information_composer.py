from infra.api_consumer import ApiConsumer
from data.usecase.starships_information_colector import StarshipInformationColector
from presenters.controllers.starship_information_colector_controller import StarshipInformationColectorController


def get_starships_information_composer():
    '''Composer'''
    infra = ApiConsumer()
    usercase = StarshipInformationColector(infra)
    controller = StarshipInformationColectorController(usercase)
    return controller
