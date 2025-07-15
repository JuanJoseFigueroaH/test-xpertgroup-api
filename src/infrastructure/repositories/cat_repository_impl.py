from typing import List
from domain.models.cat import CatBreed
from domain.repositories.cat_repository import CatRepository
from infrastructure.clients.the_cat_api import TheCatAPIClient

class CatRepositoryImpl(CatRepository):
    def __init__(self, api_client: TheCatAPIClient):
        self.api_client = api_client

    async def get_all_breeds(self) -> List[CatBreed]:
        data = await self.api_client.get_breeds()
        return [CatBreed(**breed) for breed in data]

    async def get_breed_by_id(self, breed_id: str) -> CatBreed:
        data = await self.api_client.get_breed_by_id(breed_id)
        return CatBreed(**data)

    async def search_breeds(self, query: str) -> List[CatBreed]:
        data = await self.api_client.search_breeds(query)
        return [CatBreed(**breed) for breed in data]
