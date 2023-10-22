import pytest

from atomic_aurora_backend.shows.models import Show
from atomic_aurora_backend.shows.tests.factories import ShowFactory


@pytest.fixture
def show(db) -> Show:
    """Creates a show fixture for testing"""
    return ShowFactory()


@pytest.fixture
def shows(db) -> list[Show]:
    """creates 5 shows for testing"""
    return ShowFactory.create_batch(5)


@pytest.fixture
def show_with_picture(db, picture) -> Show:
    """Creates a show with a picture"""
    return ShowFactory(pictures=[picture])
