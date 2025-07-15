import pytest
from domain.models.user import User
from domain.services.user_service import UserService
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_create_user_generates_unique_username():
    mock_repo = AsyncMock()
    mock_repo.username_exists.side_effect = [True, False]
    mock_repo.create_user = AsyncMock()

    user = User(id=None, first_name="Juan", last_name="Lopez", email="a@a.com", password="123", username="")
    mock_repo.create_user.return_value = user

    service = UserService(mock_repo)
    created = await service.create_user(user)

    assert created.username == "juan.lopez1"
