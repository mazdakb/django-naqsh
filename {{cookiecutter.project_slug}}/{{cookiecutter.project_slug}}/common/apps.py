from django.apps import AppConfig


class CommonAppConfig(AppConfig):
    name = "{{cookiecutter.project_slug}}.common"
    verbose_name = "Common"

    def ready(self):
        """Override this to put in:
            Common system checks
            common signal registration
        """
        try:
            import {{cookiecutter.project_slug}}.common.signals  # noqa F401
        except ImportError:
            pass
