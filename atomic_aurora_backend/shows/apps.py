# from django.apps import AppConfig
# from django.utils.translation import gettext_lazy as _
#
#
# class UsersConfig(AppConfig):
#     name = "atomic_aurora_backend.users"
#     verbose_name = _("Users")
#
#     def ready(self):
#         try:
#             import atomic_aurora_backend.users.signals  # noqa: F401
#         except ImportError:
#             pass

from django.apps import AppConfig


class ShowsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "atomic_aurora_backend.shows"

    def ready(self):
        try:
            import atomic_aurora_backend.users.signals #noqa: F401
        except ImportError:
            pass
