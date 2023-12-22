from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from atomic_aurora_backend.orders.views import OrderViewSet
from atomic_aurora_backend.pictures.views import PictureViewSet
from atomic_aurora_backend.products.views import ProductColorViewSet, ProductKindViewSet, ProductViewSet
from atomic_aurora_backend.shipments.views import ShipmentViewSet
from atomic_aurora_backend.shows.views import ShowViewSet
from atomic_aurora_backend.users.api.views import UserViewSet
from atomic_aurora_backend.venues.views import VenueViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("shows", ShowViewSet)
router.register("pictures", PictureViewSet)
router.register("products", ProductViewSet)
router.register("productcolors", ProductColorViewSet)
router.register("producttypes", ProductKindViewSet)
router.register("orders", OrderViewSet)
router.register("shipments", ShipmentViewSet)
router.register("venues", VenueViewSet)

url_routes = [
    path("authentication", include("atomic_aurora_backend.authentication.urls")),
    path("music", include("atomic_aurora_backend.music.urls")),
]

app_name = "api"
urlpatterns = router.urls + url_routes
