import pytest
from domain.models.user import User
from domain.services.user_service import UserService
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_login_success():
    mock_repo = AsyncMock()
    user = User(id="1", first_name="Ana", last_name="Gomez", email="ana@g.com", password="abc123", username="ana.gomez")
    mock_repo.find_by_credentials.return_value = user

    service = UserService(mock_repo)
    result = await service.login("ana.gomez", "abc123")

    assert result.username == "ana.gomez"

@pytest.mark.asyncio
async def test_login_fail():
    mock_repo = AsyncMock()
    mock_repo.find_by_credentials.return_value = None

    service = UserService(mock_repo)
    result = await service.login("nope", "fail")

    assert result is None
