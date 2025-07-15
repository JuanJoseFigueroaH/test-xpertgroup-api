from domain.services.cat_service import CatService
from domain.models.cat import CatBreed
from typing import List

class CatUseCase:
    def __init__(self, service: CatService):
        self.service = service

    async def get_all_breeds(self) -> List[CatBreed]:
        return await self.service.get_all_breeds()

    async def get_breed_by_id(self, breed_id: str) -> CatBreed:
        return await self.service.get_breed_by_id(breed_id)

    async def search_breeds(self, query: str) -> List[CatBreed]:
        return await self.service.search_breeds(query)
