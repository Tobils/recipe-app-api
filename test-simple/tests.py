from django.test import TestCase
from app.calc import add, substract


"""
run unit testing
"""
class CalcTest(TestCase):

    """ test add 2 those number """
    def test_add_numbers(self):
        self.assertEqual(add(3,8), 11)

    """ test subtract 2 those number """
    def test_subtract_number(self):
        self.assertEqual(substract(5,11), 6)