from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from atomic_aurora_backend.users.api.views import UserViewSet
from atomic_aurora_backend.shows.views import ShowViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("shows", ShowViewSet)


app_name = "api"
urlpatterns = router.urls
