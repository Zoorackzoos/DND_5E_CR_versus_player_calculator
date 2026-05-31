from src.universal_functions import get_xp_from_single_enemy_CR
from src.universal_functions.get_encounter_difficulty.get_encounter_difficulty_from_xp_values import \
    get_encounter_difficulty_from_xp_values
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr


def get_encounter_difficulty_from_cr_values(player_levels, monster_cr_values, tab_amount="\t"):
    print(tab_amount, "get_encounter_difficulty_from_cr_values")
    tab_amount += "\t"

    monster_xp_values = []

    for cr in monster_cr_values:
        monster_xp_values.append(
            get_xp_from_single_enemy_cr(cr=cr,tab_amount=tab_amount)
        )

    return get_encounter_difficulty_from_xp_values(
        player_levels=player_levels,
        monster_xp_values=monster_xp_values,
        tab_amount=tab_amount
    )