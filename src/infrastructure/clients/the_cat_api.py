import os
import httpx
from typing import List, Dict

class TheCatAPIClient:
    def __init__(self):
        self.base_url = os.getenv("THE_CAT_API_BASE_URL")
        api_key = os.getenv("THE_CAT_API_KEY")
        if not api_key:
            raise EnvironmentError("THE_CAT_API_KEY is not set in environment variables")
        self.headers = {"x-api-key": api_key}

    async def get_breeds(self) -> List[Dict]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/breeds", headers=self.headers)
            response.raise_for_status()
            return response.json()

    async def get_breed_by_id(self, breed_id: str) -> Dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/breeds/{breed_id}", headers=self.headers)
            response.raise_for_status()
            return response.json()

    async def search_breeds(self, query: str) -> List[Dict]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/breeds/search?q={query}", headers=self.headers)
            response.raise_for_status()
            return response.json()
