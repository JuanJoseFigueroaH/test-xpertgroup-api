from typing import List
from domain.models.cat import CatBreed
from domain.repositories.cat_repository import CatRepository

class CatService:
    def __init__(self, repository: CatRepository):
        self.repository = repository

    def get_all_breeds(self) -> List[CatBreed]:
        return self.repository.get_all_breeds()

    def get_breed_by_id(self, breed_id: str) -> CatBreed:
        return self.repository.get_breed_by_id(breed_id)

    def search_breeds(self, query: str) -> List[CatBreed]:
        return self.repository.search_breeds(query)
