from django.contrib import admin

from atomic_aurora_backend.products.models import Product


class PictureInline(admin.TabularInline):
    model = Product.pictures.through
