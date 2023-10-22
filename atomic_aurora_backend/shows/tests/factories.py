from factory import Faker, post_generation
from factory.django import DjangoModelFactory

from atomic_aurora_backend.shows.models import Show


class ShowFactory(DjangoModelFactory):
    name = Faker("company")
    description = Faker("sentences")
    show_date = Faker("date_time")

    class Meta:
        model = Show

    @post_generation
    def pictures(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.pictures.add(*extracted)
