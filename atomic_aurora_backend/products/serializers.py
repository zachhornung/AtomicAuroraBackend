from rest_framework import serializers

from atomic_aurora_backend.pictures.serializers import PictureSerializer
from atomic_aurora_backend.products.models import Product, ProductColor, ProductKind


class ProductColorSerializer(serializers.ModelSerializer[ProductColor]):
    class Meta:
        model = ProductColor
        fields = "__all__"


class ProductKindSerializer(serializers.ModelSerializer[ProductKind]):
    class Meta:
        model = ProductKind
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer[Product]):
    pictures = PictureSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
