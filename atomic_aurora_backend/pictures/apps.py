from django.apps import AppConfig


class PicturesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "atomic_aurora_backend.pictures"

    def ready(self):
        try:
            import atomic_aurora_backend.pictures.signals  # noqa: F401
        except ImportError:
            pass
