from fastapi import FastAPI
from infrastructure.clients.the_cat_api import TheCatAPIClient
from infrastructure.database.mongo import MongoDB
from infrastructure.repositories.cat_repository_impl import CatRepositoryImpl
from infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from domain.services.cat_service import CatService
from domain.services.user_service import UserService
from application.use_cases.cat_use_case import CatUseCase
from application.use_cases.user_use_case import UserUseCase
from interfaces.controllers import cat_controller, user_controller
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

MONGO_URI = "mongodb://localhost:27017"
MONGO_DB = "catdb"

mongo = MongoDB(MONGO_URI, MONGO_DB)
cat_repo = CatRepositoryImpl(TheCatAPIClient())
user_repo = UserRepositoryImpl(mongo)

cat_service = CatService(cat_repo)
user_service = UserService(user_repo)

cat_use_case = CatUseCase(cat_service)
user_use_case = UserUseCase(user_service)

cat_controller.use_case = cat_use_case
user_controller.use_case = user_use_case

app.include_router(cat_controller.router)
app.include_router(user_controller.router)
