from factory import Faker, SubFactory, post_generation
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyFloat

from atomic_aurora_backend.products.models import Product, ProductColor, ProductKind


class ProductColorFactory(DjangoModelFactory):
    color = Faker("color")

    class Meta:
        model = ProductColor


class ProductKindFactory(DjangoModelFactory):
    name = Faker("sentence")

    class Meta:
        model = ProductKind


class ProductFactory(DjangoModelFactory):
    kind = SubFactory(ProductKindFactory)
    name = Faker("sentence")
    description = Faker("sentence")
    color = SubFactory(ProductColorFactory)
    price = FuzzyFloat(0.99, 99.99)

    class Meta:
        model = Product

    @post_generation
    def pictures(self, create, extracted, **kwargs):
        if extracted:
            self.pictures.set(extracted)
