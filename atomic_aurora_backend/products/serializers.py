from rest_framework import serializers

from atomic_aurora_backend.products.models import Product, ProductColor, ProductType


class ProductColorSerializer(serializers.ModelSerializer[ProductColor]):

    class Meta:
        model = ProductColor
        fields = "__all__"


class ProductTypeSerializer(serializers.ModelSerializer[ProductType]):

    class Meta:
        model = ProductType
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer[Product]):

    class Meta:
        model = Product
        fields = "__all__"

