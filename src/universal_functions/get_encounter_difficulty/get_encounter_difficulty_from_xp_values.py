#src/universal_functions/get_encounter_difficulty_from_xp_values.py

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


def get_encounter_difficulty_from_xp_values(player_levels,
                                            monster_xp_values,
                                            encounter_name="unnamed",
                                            tab_amount="\t"):
    """
    Example usage: \n

    players = [5, 5, 5, 5]

    # Three CR 2 monsters = 450 XP each \n
    monster = [450, 450, 450]

    print(encounter_difficulty(players, monsters))

    :param player_levels:
    :param monster_xp_values:
    :param tab_amount
    :return:
    """
    print(tab_amount, "get_encounter_difficulty")
    tab_amount += "\t"

    if len(player_levels) > 1:
        if player_levels[0] != player_levels[1]:
            print(tab_amount,"WARNING: get_encounter_difficulty_from_xp_values: player_levels are not all the same. Will proceed with computation.")

    total_monster_xp = sum(monster_xp_values)

    adjusted_xp = \
    (
        total_monster_xp *
        get_monster_amount_multiplier(monster_count=len(monster_xp_values), tab_amount=tab_amount)
    )

    party_thresholds = \
    {
        "easy": 0,
        "medium": 0,
        "hard": 0,
        "deadly": 0
    }

    for level in player_levels:
        for predicted_difficulty in party_thresholds:
            party_thresholds[predicted_difficulty] += player_threshold_var[level][predicted_difficulty]

    if adjusted_xp < party_thresholds["easy"]:
        predicted_difficulty = "trivial"
    elif adjusted_xp < party_thresholds["medium"]:
        predicted_difficulty = "easy"
    elif adjusted_xp < party_thresholds["hard"]:
        predicted_difficulty = "medium"
    elif adjusted_xp < party_thresholds["deadly"]:
        predicted_difficulty = "hard"
    else:
        predicted_difficulty = "deadly"

    return \
    {
        "encounter_name": encounter_name,
        "party_level": sum(player_levels) / len(player_levels), #average :-D
        "party_size": len(player_levels),
        "predicted_difficulty": predicted_difficulty,
        "actual_difficulty": "???",
        "monster_count": len(monster_xp_values),
        "total_monster_xp": sum(monster_xp_values),
        "adjusted_xp": adjusted_xp, #action economy effects xp values
        "rounds": "???", #in session deduction
        "lasted_too_long": "???", #in session deduction
        "players_downed": "???", #in session deduction
        "players_killed": "???", #in session deduction
        "major_resource_drain": "???", #in session deduction
        "terrain_helped_players": "???", #TODO: implement a parameter for terrain_helped_players
        "terrain_helped_monsters": "???", #TODO: implement a parameter for terrain_helped_monsters
        "player_synergy_tags": "???", #in session deduction
        "monster_weakness_tags": "???", #TODO: implement a parameter for monster_weakness_tags
        "notes": "???", #in session deduction
        "party_thresholds": party_thresholds,
    }

if __name__ == "__main__":
    tab_amount = "\t"

    players = [5, 5, 5, 5]

    # Three CR 2 monsters = 450 XP each
    monsters = [450, 450, 450]

    encounter_difficulty = get_encounter_difficulty_from_xp_values(players, monsters, tab_amount=tab_amount)
    print_dictionary_nicely(dict_in_question=encounter_difficulty, tab_amount=tab_amount)