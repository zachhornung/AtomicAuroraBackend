from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Product, ProductColor, ProductKind
from .serializers import ProductColorSerializer, ProductKindSerializer, ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductKindViewSet(ReadOnlyModelViewSet):
    queryset = ProductKind.objects.all()
    serializer_class = ProductKindSerializer
    permission_classes = [AllowAny]


class ProductColorViewSet(ReadOnlyModelViewSet):
    queryset = ProductColor.objects.all()
    serializer_class = ProductColorSerializer
    permission_classes = [AllowAny]
