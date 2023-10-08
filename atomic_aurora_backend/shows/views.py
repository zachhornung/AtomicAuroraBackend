from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import ShowSerializer
from .models import Show


class ShowViewSet(ReadOnlyModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    permission_classes = [AllowAny]

