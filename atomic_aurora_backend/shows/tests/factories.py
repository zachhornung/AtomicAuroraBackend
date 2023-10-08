from factory import Faker
from factory.django import DjangoModelFactory

from atomic_aurora_backend.shows.models import Show


class ShowFactory(DjangoModelFactory):

    name = Faker("company")
    description = Faker("sentences")
    show_date = Faker("date_time")

    class Meta:
        model = Show
