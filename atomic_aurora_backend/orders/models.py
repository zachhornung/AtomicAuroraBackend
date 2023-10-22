from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.reverse import reverse

# Create your models here.

User = get_user_model()


class Order(models.Model):
    """represents an order in the database"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"User: {self.user.email} date placed: {self.date_ordered}"

    def get_absolute_url(self) -> str:
        return reverse("api:order-detail", kwargs={"pk": self.pk})
