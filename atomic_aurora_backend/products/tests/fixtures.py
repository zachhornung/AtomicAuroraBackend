import pytest

from atomic_aurora_backend.products.tests.factories import ProductColorFactory, ProductFactory, ProductKindFactory


@pytest.fixture
def product(db):
    """Create a product fixture."""
    return ProductFactory()


@pytest.fixture
def product_with_color(db):
    """Create a product with a color."""
    return ProductFactory(color=ProductColorFactory())


@pytest.fixture
def products(db):
    """Create many products fixture."""
    return ProductFactory.create_batch(50)


@pytest.fixture
def products_with_pictures(db, pictures):
    """Create many products fixture."""
    return ProductFactory.create_batch(50, pictures=pictures)


@pytest.fixture
def product_kind(db):
    """Create a product kind fixture."""
    return ProductKindFactory()
