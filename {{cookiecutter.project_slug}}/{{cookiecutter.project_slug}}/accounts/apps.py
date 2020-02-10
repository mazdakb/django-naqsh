from django.apps import AppConfig


class AccountsAppConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.accounts"
    verbose_name = "Accounts"

    def ready(self):
        """Override this to put in:
            Accounts system checks
            Accounts signal registration
        """
        try:
            import {{ cookiecutter.project_slug }}.accounts.receivers  # noqa F401
        except ImportError:
            pass
