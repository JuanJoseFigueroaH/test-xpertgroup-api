from fastapi import APIRouter
from domain.models.cat import CatBreed
from application.use_cases.cat_use_case import CatUseCase

router = APIRouter()
use_case: CatUseCase = None

@router.get("/breeds", response_model=list[CatBreed])
async def get_breeds():
    return await use_case.get_all_breeds()

@router.get("/breeds/{breed_id}", response_model=CatBreed)
async def get_breed(breed_id: str):
    return await use_case.get_breed_by_id(breed_id)

@router.get("/breeds/search", response_model=list[CatBreed])
async def search_breeds(q: str):
    return await use_case.search_breeds(q)
