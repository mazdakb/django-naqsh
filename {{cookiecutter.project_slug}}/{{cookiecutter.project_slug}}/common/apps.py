from django.apps import AppConfig


class CommonAppConfig(AppConfig):
    name = "marketplace.common"
    verbose_name = "Common"

    def ready(self):
        """Override this to put in:
            Common system checks
            Common signal registration
        """
        try:
            import marketplace.common.receivers  # noqa F401
        except ImportError:
            pass
