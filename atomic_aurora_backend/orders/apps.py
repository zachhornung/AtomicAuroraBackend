from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "atomic_aurora_backend.orders"

    def ready(self):
        try:
            import atomic_aurora_backend.orders.signals  # noqa: F401
        except ImportError:
            pass
