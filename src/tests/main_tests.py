#src/tests/main_tests.py
import unittest

from src.universal_functions.get_damage_per_round import get_damage_per_round_no_print
from src.universal_functions.stats.get_modifier_from_numeric_stat import get_modifier_from_numeric_stat
from src.universal_functions.stats.get_numeric_stat_from_modifier import get_numeric_stat_from_modifier


class TestGetNumericStatFromModifier(unittest.TestCase):
    def test_one_negative_five(self):
        #good enough
        self.assertEqual(0, get_numeric_stat_from_modifier(modifier=-5))
    def test_fourteen(self):
        self.assertEqual(14, get_numeric_stat_from_modifier(modifier=2))
    def test_thirty(self):
        self.assertEqual(30, get_numeric_stat_from_modifier(modifier=10))

class TestGetNumericStatToModifier(unittest.TestCase):
    def test_one_negative_five(self):
        self.assertEqual(-5, get_modifier_from_numeric_stat(stat=1))
    def test_fourteen(self):
        self.assertEqual(2, get_modifier_from_numeric_stat(stat=14))
    def test_fifteen(self):
        self.assertEqual(2, get_modifier_from_numeric_stat(stat=15))
    def test_thirty(self):
        self.assertEqual(10, get_modifier_from_numeric_stat(stat=30))

class TestGetDamagePerRound(unittest.TestCase):

    def test_two_six_dice(self):
        dice_dict = {6: 2}
        self.assertEqual(
            get_damage_per_round_no_print(dice_dict),
            7.0
        )

    def test_two_d4_one_d8(self):
        dice_dict = {
            4: 2,
            8: 1
        }

        self.assertEqual(
            get_damage_per_round_no_print(dice_dict),
            9.5
        )

    def test_constant_damage(self):
        dice_dict = {
            4: 5,
            "constant": 2
        }

        self.assertEqual(
            get_damage_per_round_no_print(dice_dict),
            14.5
        )