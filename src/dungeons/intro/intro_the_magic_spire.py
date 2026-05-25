from src.universal_functions.craft_cr_from_monster_stat_block import craft_cr_from_monster_stat_block, \
    plug_monster_var_values_into_get_cr_from_monster
from src.universal_functions.get_average_damage import get_average_damage_no_print


def intro_the_magic_spire(tab_amount="\t"):
    #TODO: finishing getting CR calculations for the magic spire

    print(tab_amount,"intro_the_magic_spire")
    player_levels = [3,3,3,3]

    calculus_monster_limit_damage_dice = \
        {
            12 : 1
        }
    #some of these keys are useless to the CR crafter. that means I should make my own and use wizards of the coast as test cases.
    #TODO: make my own stat-block to CR crafter.
    calculus_monster_limit_stat_block = \
        {
            "hp": 15,
            "ac": 15,
            "speed_ground": 15,
            "str": 14,
            "dex": 6,
            "con": 10,
            "int": 14,
            "wis": 6,
            "cha": 2,
            "attack_bonus": 2,
            "has_legendary_action": False,
            "has_flight": False,
            "resistance_count": 1,
            "immunity_count": 0,
            "weakness_count": 2,
            "save_dc": 0,
            "is_spellcaster": False,
            "regeneration_per_round": 0,
            "multiattack_count": 0,
            "ability_count": 0,
            "average_damage": get_average_damage_no_print(dice_dict=calculus_monster_limit_damage_dice)
        }
    calculus_monster_limit_cr = plug_monster_var_values_into_get_cr_from_monster(monster_var=calculus_monster_limit_stat_block,tab_amount=tab_amount)
    print(calculus_monster_limit_cr)

if __name__ == "__main__":
    intro_the_magic_spire()