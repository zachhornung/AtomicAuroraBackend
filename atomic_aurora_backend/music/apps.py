from django.apps import AppConfig


class MusciConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "atomic_aurora_backend.music"

    def ready(self):
        try:
            import atomic_aurora_backend.music.signals  # noqa: F401
        except ImportError:
            pass
