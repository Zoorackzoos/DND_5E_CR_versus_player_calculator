import unittest


def get_numeric_stat_from_modifier(modifier):
    return (modifier * 2) + 10

class Test_get_numeric_stat_from_modifier(unittest.TestCase):
    def test_one_negative_five(self):
        #good enough
        self.assertEqual(0, get_numeric_stat_from_modifier(modifier=-5))
    def test_fourteen(self):
        self.assertEqual(14, get_numeric_stat_from_modifier(modifier=2))
    def test_thirty(self):
        self.assertEqual(30, get_numeric_stat_from_modifier(modifier=10))