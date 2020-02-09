from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """General Utilities command

    This command provides general helper codes and tools
    """

    help = """
    This command provides general helper codes and tools
    """

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--create-superuser",
            action="store_true",
            dest="create-superuser",
            help="Perform all initialization actions",
        )

    def create_superuser(
        self,
        email: str = "admin@example.com",
        password: str = "password",
        first_name: str = "Jane",
        last_name: str = "Doe",
    ):
        # import user here for isolation
        from marketplace.accounts.models import User

        # create the initial superuser for test purposes
        User.objects.create_superuser(
            email=email, password=password, first_name=first_name, last_name=last_name
        )

    def handle(self, *args, **options):
        """Handle command

        The entry point of the command

        :param args:
        :param options:
        :return:
        """
        # create a sample superuser if the appropriate argument is passed
        if options["create-superuser"]:
            self.create_superuser()
