from django.contrib import admin

from atomic_aurora_backend.products.models import Product, ProductColor, ProductType

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductColor)
