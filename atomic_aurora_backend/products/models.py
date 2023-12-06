from django.db import models
from rest_framework.reverse import reverse

from atomic_aurora_backend.pictures.models import Picture

# Create your models here.


class Product(models.Model):
    """
    represents different merchandise products in the database
    """

    kind = models.ForeignKey("products.ProductKind", on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=256)
    description = models.TextField()
    color = models.ForeignKey(
        "products.ProductColor",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.FloatField()
    pictures = models.ManyToManyField(Picture, related_name="products")

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("api:product-detail", kwargs={"pk": self.pk})


class ProductKind(models.Model):
    """
    represents different kinds of products in the databse
    """

    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("api:productkind-detail", kwargs={"pk": self.pk})


class ProductColor(models.Model):
    """
    different colors for products
    """

    color = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.color

    def get_absolute_url(self) -> str:
        return reverse("api:productcolor-detail", kwargs={"pk": self.pk})
