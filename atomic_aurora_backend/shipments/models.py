from django.db import models
from rest_framework.reverse import reverse

from atomic_aurora_backend.orders.models import Order

# Create your models here.


class Shipment(models.Model):
    """represents a shipment in the database"""

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date_shipped = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"order: {self.order}, shipped: {self.date_shipped}"

    def get_absolute_url(self) -> str:
        return reverse("api:shipment-detail", kwargs={"pk": self.pk})
