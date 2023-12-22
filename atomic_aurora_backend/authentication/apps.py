from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "atomic_aurora_backend.authentication"

    def ready(self):
        try:
            import atomic_aurora_backend.authentication.signals  # noqa: F401
        except ImportError:
            pass
