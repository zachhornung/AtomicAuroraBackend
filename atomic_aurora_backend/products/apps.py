from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "atomic_aurora_backend.products"

    def ready(self):
        try:
            import atomic_aurora_backend.products.signals #noqa: F401
        except ImportError:
            pass
