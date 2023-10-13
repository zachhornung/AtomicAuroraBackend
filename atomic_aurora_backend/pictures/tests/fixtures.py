from atomic_aurora_backend.pictures.models import Picture
from atomic_aurora_backend.pictures.tests.factories import PictureFactory
import pytest

@pytest.fixture
def picture(db) -> Picture:
    """Creates a picture fixture in the database"""
    return PictureFactory()
