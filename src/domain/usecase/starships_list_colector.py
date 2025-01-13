from abc import ABC, abstractmethod
from typing import Dict, List

# classes abstratas a gente nao instacia e so herda


class StarshipsColectorInterface(ABC):
    '''Starships colector interfaces'''
    @abstractmethod
    def list(self, page: int, limit: int):
        '''Must implement'''
        pass
