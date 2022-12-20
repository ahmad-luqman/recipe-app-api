"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Tests the calc module"""

    def test_add_numbers(self):
        """Tests adding number together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
