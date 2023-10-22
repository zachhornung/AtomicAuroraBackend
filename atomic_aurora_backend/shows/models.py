from django.db import models
from rest_framework.reverse import reverse

from atomic_aurora_backend.pictures.models import Picture

# Create your models here.


class Show(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    show_date = models.DateTimeField()
    pictures = models.ManyToManyField(Picture, blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.show_date}"

    def get_absolute_url(self) -> str:
        return reverse("api:show-detail", kwargs={"pk": self.pk})

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "show_date"],
                name="unique_show_per_date",
            )
        ]
