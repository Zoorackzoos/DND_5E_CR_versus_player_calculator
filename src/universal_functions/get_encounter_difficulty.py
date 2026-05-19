"""
calculate monster XP total
M = sigma_n_i=1( XP_i )

calculate monster count multiplier
A = M * k

calculate party threshold
T = sigma_p_j=1( t_j )
"""
from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.get_monster_amount_multiplier import get_monster_amount_multiplier
from src.universal_functions.vars.player_threshold_var import player_threshold_var

def get_encounter_difficulty(player_levels, monster_xp_values, get_encounter_difficulty_tab_amount="\t"):
    """
    Example usage: \n

    players = [5, 5, 5, 5]

    # Three CR 2 monsters = 450 XP each \n
    monster = [450, 450, 450]

    print(encounter_difficulty(players, monsters))

    :param player_levels:
    :param monster_xp_values:
    :param get_encounter_difficulty_tab_amount
    :return:
    """
    print(get_encounter_difficulty_tab_amount, "get_encounter_difficulty")
    get_encounter_difficulty_tab_amount += "\t"

    total_monster_xp = sum(monster_xp_values)

    adjusted_xp = \
    (
        total_monster_xp *
        get_monster_amount_multiplier(monster_count=len(monster_xp_values), tab_amount=get_encounter_difficulty_tab_amount)
    )

    party_thresholds = \
    {
        "easy": 0,
        "medium": 0,
        "hard": 0,
        "deadly": 0
    }

    for level in player_levels:
        for difficulty in party_thresholds:
            party_thresholds[difficulty] += player_threshold_var[level][difficulty]

    if adjusted_xp < party_thresholds["easy"]:
        difficulty = "trivial"
    elif adjusted_xp < party_thresholds["medium"]:
        difficulty = "easy"
    elif adjusted_xp < party_thresholds["hard"]:
        difficulty = "medium"
    elif adjusted_xp < party_thresholds["deadly"]:
        difficulty = "hard"
    else:
        difficulty = "deadly"

    return \
    {
        "adjusted_xp": adjusted_xp,
        "thresholds": party_thresholds,
        "difficulty": difficulty
    }

if __name__ == "__main__":
    tab_amount = "\t"

    players = [5, 5, 5, 5]

    # Three CR 2 monsters = 450 XP each
    monsters = [450, 450, 450]

    encounter_difficulty = get_encounter_difficulty(players, monsters, get_encounter_difficulty_tab_amount=tab_amount)
    print_dictionary_nicely(dict_in_question=encounter_difficulty, tab_amount=tab_amount)