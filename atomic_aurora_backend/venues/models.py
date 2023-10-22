from django.db import models
from django.db.models.functions import Lower
from rest_framework.reverse import reverse

# Create your models here.


class Venue(models.Model):
    """
    models a venue in the database
    """

    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("api:venue-detail", kwargs={"pk": self.pk})

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique_name_per_venue",
            )
        ]
