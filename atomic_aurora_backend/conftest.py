import pytest
from rest_framework.test import APIClient

from atomic_aurora_backend.users.models import User
from atomic_aurora_backend.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def unauthenticated_client():
    return APIClient()
