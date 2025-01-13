from abc import ABC, abstractmethod


class StarshipInformationColectorInterface(ABC):
    '''Starshipsinformation interface'''
    @abstractmethod
    def find_starship(self, starship_id: int, page: int, limit: int):
        '''Must implement'''
        pass
