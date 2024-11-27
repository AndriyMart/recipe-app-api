"""
Django command to wait for db to be available
"""
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django Command to wait for db"""

    def handle(self, *args, **options):
        pass