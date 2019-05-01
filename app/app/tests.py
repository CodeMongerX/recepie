from django.test import TestCase

from app.app.calc import add


class CalcTests(TestCase):

    def tests_add_numbers(self):
        """2 nums are added """
        self.assertEqual(add(3, 8), 11) 