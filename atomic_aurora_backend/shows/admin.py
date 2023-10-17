from django.contrib import admin

from atomic_aurora_backend.shows.models import Show

class ShowAdmin(admin.ModelAdmin):
    filter_horizontal = ["pictures"]

admin.site.register(Show, ShowAdmin)
