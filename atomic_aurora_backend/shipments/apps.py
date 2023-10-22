from django.apps import AppConfig


class ShipmentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "atomic_aurora_backend.shipments"

    def ready(self):
        try:
            import atomic_aurora_backend.shipments.signals  # noqa: F401
        except ImportError:
            pass
