from django.contrib import admin

from atomic_aurora_backend.pictures.models import Picture


class PictureInline(admin.TabularInline):
    """Allow for pictures to be added inline."""

    model = Picture
