import pytest

from atomic_aurora_backend.pictures.models import Picture
from atomic_aurora_backend.pictures.tests.factories import PictureFactory


@pytest.fixture
def picture(db) -> Picture:
    """Creates a picture fixture in the database"""
    return PictureFactory()


@pytest.fixture
def pictures(db) -> list[Picture]:
    """Creates many picture fixtures in the database"""
    return PictureFactory.create_batch(5)
