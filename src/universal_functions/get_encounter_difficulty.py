"""
calculate monster XP total
M = sigma_n_i=1( XP_i )

calculate monster count multiplier
A = M * k

calculate party threshold
T = sigma_p_j=1( t_j )
"""
from src.universal_functions.get_monster_amount_multiplier import get_monster_amount_multiplier
from src.universal_functions.vars.player_threshold_var import player_threshold_var

def get_encounter_difficulty(player_levels, monster_xp_values,tab_amount="\t"):
    """
    Example usage:

    players = [5, 5, 5, 5]

    # Three CR 2 monsters = 450 XP each
    monsters = [450, 450, 450]

    print(encounter_difficulty(players, monsters))

    :param player_levels:
    :param monster_xp_values:
    :return:
    """
    print(tab_amount,"get_encounter_difficulty")

    total_monster_xp = sum(monster_xp_values)

    adjusted_xp = \
    (
        total_monster_xp *
        get_monster_amount_multiplier(len(monster_xp_values))
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