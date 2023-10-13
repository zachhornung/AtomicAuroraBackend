from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from atomic_aurora_backend.users.api.views import UserViewSet
from atomic_aurora_backend.shows.views import ShowViewSet
from atomic_aurora_backend.pictures.views import PictureViewSet
from atomic_aurora_backend.products.views import ProductViewSet, ProductColorViewSet, ProductTypeViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("shows", ShowViewSet)
router.register("pictures", PictureViewSet)
router.register("products", ProductViewSet)
router.register("productcolors", ProductColorViewSet)
router.register("producttypes", ProductTypeViewSet)


app_name = "api"
urlpatterns = router.urls
