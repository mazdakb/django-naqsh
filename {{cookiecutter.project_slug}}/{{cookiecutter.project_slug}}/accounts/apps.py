from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "{{cookiecutter.project_slug}}.accounts"
    verbose_name = "Accounts"

    def ready(self):
        """Override this to put in:
            Accounts system checks
            Accounts signal registration
        """
        try:
            import accounts.signals  # noqa F401
        except ImportError:
            pass
