"""
Django command to wait for db to be available
"""
import time

from django.core.management import BaseCommand
from django.db import OperationalError
from psycopg2 import OperationalError as Psycop2Error

class Command(BaseCommand):
    """Django Command to wait for db"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for db...")
        db_up = False
        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycop2Error, OperationalError):
                self.stdout.write(self.style.ERROR("DB unavailable, waiting 1 second..."))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("DB available!"))
