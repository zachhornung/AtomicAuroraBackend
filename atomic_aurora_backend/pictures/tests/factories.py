from factory import Faker
from factory.django import DjangoModelFactory, ImageField

from atomic_aurora_backend.pictures.models import Picture


class PictureFactory(DjangoModelFactory):
    description = Faker("sentences")
    picture = ImageField(filename="sample_image.jpg")

    class Meta:
        model = Picture
