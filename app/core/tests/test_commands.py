"""
Test custom Django management commands
"""
from unittest.mock import patch

from django.core.management import call_command
from django.db import OperationalError
from django.test import SimpleTestCase
from psycopg2 import OperationalError as Psycop2Error


@patch("core.management.commands.wait_for_db.Command.check")
class CommandsTestCase(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self, patched_check):
        patched_check.return_value = True

        call_command("wait_for_db")

        patched_check.assert_called_once_with(database=["default"])

    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for db when getting operational error"""
        patched_check.side_effect = [Psycop2Error] * 2 + [OperationalError] * 3 + [True]

        call_command("wait_for_db")

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(database=["default"])
