import unittest

from src.universal_functions.craft_cr_from_monster_stat_block import (
    CR_TABLE,
    craft_cr_from_monster_stat_block,
    get_defensive_cr,
    get_offensive_cr,
    plug_monster_var_values_into_get_cr_from_monster,
)


class TestCraftCrFromMonsterStatBlock(unittest.TestCase):
    def test_cr_table_supports_cr_thirty(self):
        self.assertEqual(30, CR_TABLE[-1]["CR"])
        self.assertEqual(30, get_defensive_cr(850))
        self.assertEqual(30, get_offensive_cr(320))

    def test_recharge_damage_is_averaged_over_three_rounds(self):
        regular_damage = craft_cr_from_monster_stat_block(
            hit_points=20,
            armor_class=13,
            damage_per_round=4,
            attack_modifier=3,
        )

        recharge_damage = craft_cr_from_monster_stat_block(
            hit_points=20,
            armor_class=13,
            damage_per_round=4,
            attack_modifier=3,
            recharge_damage=30,
        )

        self.assertGreater(recharge_damage, regular_damage)

    def test_save_dc_can_raise_offensive_cr(self):
        attack_only = craft_cr_from_monster_stat_block(
            hit_points=20,
            armor_class=13,
            damage_per_round=9,
            attack_modifier=3,
        )

        with_save_dc = craft_cr_from_monster_stat_block(
            hit_points=20,
            armor_class=13,
            damage_per_round=9,
            attack_modifier=3,
            save_dc=17,
        )

        self.assertGreater(with_save_dc, attack_only)

    def test_plugger_accepts_new_optional_fields(self):
        monster_var = {
            "hp": 60,
            "ac": 11,
            "average_damage": 10,
            "attack_bonus": 5,
            "has_flight": True,
            "save_dc": 13,
            "recharge_damage": 20,
            "ability_count": 1,
        }

        result = plug_monster_var_values_into_get_cr_from_monster(monster_var)

        self.assertIsInstance(result, (int, float))


if __name__ == "__main__":
    unittest.main()
