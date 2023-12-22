from django.contrib import admin

from atomic_aurora_backend.products.models import Product, ProductColor, ProductKind


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product

    filter_horizontal = ["pictures"]


admin.site.register(ProductKind)
admin.site.register(ProductColor)
