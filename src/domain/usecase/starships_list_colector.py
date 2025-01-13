from abc import ABC, abstractmethod
from typing import Dict, List


class StarshipsColectorInterface(ABC):
    '''Starships colector interfaces'''
    @abstractmethod
    def list(self, page: int, limit: int):
        '''Must implement'''
        pass
