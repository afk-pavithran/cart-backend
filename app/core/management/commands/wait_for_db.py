import time
from psycopg2 import OperationalError as psycopgError
from django.db.utils import OperationalError

from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for DB")
        DB_CONNECTED = False
        while DB_CONNECTED is False:
            try:
                self.check(databases=['default'])
                DB_CONNECTED = True
            except (psycopgError, OperationalError):
                time.sleep(2)

        self.stdout.write("DB Connected")
