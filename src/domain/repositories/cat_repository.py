from abc import ABC, abstractmethod
from typing import List
from domain.models.cat import CatBreed

class CatRepository(ABC):

    @abstractmethod
    def get_all_breeds(self) -> List[CatBreed]:
        pass

    @abstractmethod
    def get_breed_by_id(self, breed_id: str) -> CatBreed:
        pass

    @abstractmethod
    def search_breeds(self, query: str) -> List[CatBreed]:
        pass
