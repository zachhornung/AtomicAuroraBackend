from django.db import models
from rest_framework.reverse import reverse

# Create your models here.


class Product(models.Model):
    """
    represents different merchandise products in the database
    """

    type = models.ForeignKey("products.ProductType", on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    color = models.ForeignKey("products.ProductColor", on_delete=models.CASCADE)
    price = models.FloatField()

    def get_absolute_url(self) -> str:
        return reverse("api:product-detail", kwargs={"pk": self.pk})


class ProductType(models.Model):
    """
    represents different kinds of products in the databse
    """

    name = models.CharField(max_length=256)

    def get_absolute_url(self) -> str:
        return reverse("api:producttype-detail", kwargs={"pk": self.pk})


class ProductColor(models.Model):
    """
    different colors for products
    """

    color = models.CharField(max_length=128)

    def get_absolute_url(self) -> str:
        return reverse("api:productcolor-detail", kwargs={"pk": self.pk})
