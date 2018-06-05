from django.apps import AppConfig


class CommonAppConfig(AppConfig):
    name = "{{cookiecutter.project_slug}}.common"
    verbose_name = "Common"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        try:
            import {{cookiecutter.project_slug}}.common.signals  # noqa F401
        except ImportError:
            pass
