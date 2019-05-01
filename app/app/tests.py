from django import tests.TestCase

from app.calc import add


class CalcTests(TestCase):

    def tests_add_numbers(self):
        """2 nums are added """
        self.assertEqual(add(3, 8), 11) 