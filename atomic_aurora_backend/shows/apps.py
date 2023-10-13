from django.apps import AppConfig


class ShowsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "atomic_aurora_backend.shows"

    def ready(self):
        try:
            import atomic_aurora_backend.shows.signals #noqa: F401
        except ImportError:
            pass
