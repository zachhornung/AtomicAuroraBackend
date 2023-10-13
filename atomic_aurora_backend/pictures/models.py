from django.db import models
from rest_framework.reverse import reverse

# Create your models here.

class Picture(models.Model):
    """
    Stores pictures in the database.
    Pictures can be for any other model,
    such as show pictures, merch pictures, etc.
    """
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField()

    def __str__(self) -> str:
        return self.description

    def get_absolute_url(self) -> str:
        return reverse("api:picture-detail", kwargs={"pk": self.pk})
