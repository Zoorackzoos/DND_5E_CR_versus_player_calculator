import math
import unittest

def get_modifier_from_numeric_stat(stat):
    return math.floor((stat - 10) / 2)

class TestGetNumericStatToModifier(unittest.TestCase):
    def test_one_negative_five(self):
        self.assertEqual(-5, get_modifier_from_numeric_stat(stat=1))
    def test_fourteen(self):
        self.assertEqual(2, get_modifier_from_numeric_stat(stat=14))
    def test_fifteen(self):
        self.assertEqual(2, get_modifier_from_numeric_stat(stat=15))
    def test_thirty(self):
        self.assertEqual(10, get_modifier_from_numeric_stat(stat=30))