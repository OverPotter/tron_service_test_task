from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from src.database.repositories.manager import OrmRepositoryManager
from src.rest_main import app


@pytest.fixture()
def test_client():
    return TestClient(app)


@pytest.fixture()
def mock_repository_manager():
    return MagicMock(spec=OrmRepositoryManager)


@pytest.fixture()
def mock_wallet_service(mock_repository_manager):
    service_mock = AsyncMock()
    mock_repository_manager.get_wallet_query_repository.return_value = (
        service_mock
    )
    return service_mock
