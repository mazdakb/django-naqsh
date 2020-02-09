from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    """Database Utilities command

    This command provides helper codes and tools for database operations
    """

    help = """
    This command provides helper codes and tools for database operations
    """

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--reset-db",
            action="store_true",
            dest="reset-db",
            help="Perform all initialization actions",
        )

    def reset_database_tables(self):
        """Reset database tables

        This command drops all database tables and recreates them
        by running django migrations.

        Notes:
            - It does not remove postgis related table(s).

        :return:
        """
        # drop the tables
        with connection.cursor() as cursor:
            cursor.execute(
                # language=sql
                """
                DO $$ DECLARE
                    r RECORD;
                BEGIN
                    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema() AND tablename != 'spatial_ref_sys') LOOP  -- # noqa
                        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                    END LOOP;
                END $$;
                """
            )

    def handle(self, *args, **options):
        """Handle command

        The entry point of the command

        :param args:
        :param options:
        :return:
        """
        # reset the database if the appropriate argument is passed
        if options["reset-db"]:
            self.reset_database_tables()
