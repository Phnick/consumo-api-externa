from infra.api_consumer import ApiConsumer
from data.usecase.starships_list_colector import StarshipsColector
from presenters.controllers.starships_list_colector_controllers import StarshipsListColectorController


def get_starships_composer():
    '''Composer'''
    infra = ApiConsumer()
    usercase = StarshipsColector(infra)
    controller = StarshipsListColectorController(usercase)
    return controller
