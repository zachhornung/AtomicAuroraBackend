from django.apps import AppConfig


class VenuesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "atomic_aurora_backend.venues"

    def ready(self):
        try:
            import atomic_aurora_backend.venues.signals #noqa: F401
        except ImportError:
            pass
