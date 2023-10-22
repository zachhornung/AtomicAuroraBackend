from django.contrib import admin

from atomic_aurora_backend.shows.models import Show


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    filter_horizontal = ["pictures"]
