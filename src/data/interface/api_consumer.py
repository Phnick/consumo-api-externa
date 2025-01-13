from abc import ABC, abstractmethod


class ApiConsumerInterface(ABC):
    '''ApiConsumer interface'''
    @abstractmethod
    def get_starships(self, page: int, limit: int):
        pass

    @abstractmethod
    def get_starships_by_id(self, starship_id: int, limit: int, page: int):
        pass
