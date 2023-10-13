from factory import Faker, post_generation, SubFactory
from factory.fuzzy import FuzzyFloat
from factory.django import DjangoModelFactory

from atomic_aurora_backend.products.models import Product, ProductColor, ProductType


class ProductColorFactory(DjangoModelFactory):

    color = Faker("color")

    class Meta:
        model = ProductColor


class ProductTypeFactory(DjangoModelFactory):

    name = Faker("sentence")

    class Meta:
        model = ProductType


class ProductFactory(DjangoModelFactory):

    type = SubFactory(ProductTypeFactory)
    name = Faker("sentence")
    description = Faker("sentence")
    color = SubFactory(ProductColorFactory)
    price = FuzzyFloat(0.99, 99.99)

    class Meta:
        model = Product

