from src.universal_functions.display.print_dictionary_nicely import print_dictionary_nicely
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty import get_encounter_difficulty

#TODO: make the searching of the database more applicable on this program in general. it's more convent to cntrl+F on the spreadsheet on google sheets

def intro_the_magic_castle(tab_amount="\t"):
    print(tab_amount,"intro_the_magic_castle")
    tab_amount += "\t"

    player_levels = [3,3,3,3]

    skeleton_cr = get_cr_from_precise_monster_search(param_type="Name",
                                                     string="Skeleton",
                                                     tab_amount=tab_amount)
    skeleton_war_horse_cr = get_cr_from_precise_monster_search(param_type="Name",
                                                               string="Skeleton, Warhorse",
                                                               tab_amount=tab_amount)
    skeleton_xp = get_xp_from_single_enemy_cr(cr=skeleton_cr,
                                              tab_amount=tab_amount)
    skeleton_war_horse_xp = get_xp_from_single_enemy_cr(cr=skeleton_war_horse_cr,
                                                        tab_amount=tab_amount)
    inner_castle_enemies = [skeleton_xp,skeleton_xp,skeleton_xp,
                            skeleton_war_horse_xp,skeleton_war_horse_xp,
                            skeleton_xp]
    inner_castle_difficulty = get_encounter_difficulty(player_levels=player_levels,
                                                       monster_xp_values=inner_castle_enemies,
                                                       tab_amount=tab_amount)

    skeleton_minotaur_cr = get_cr_from_precise_monster_search(param_type="Name",
                                                              string="Skeleton, Minotaur",
                                                              tab_amount=tab_amount)
    skeleton_minotaur_xp = get_xp_from_single_enemy_cr(cr=skeleton_minotaur_cr,
                                                       tab_amount=tab_amount)
    tower_of_power_enemies = [skeleton_minotaur_xp]
    tower_of_power_difficulty = get_encounter_difficulty(player_levels=player_levels,
                                                         monster_xp_values=tower_of_power_enemies,
                                                         tab_amount=tab_amount)

    giant_skeleton_cr = get_cr_from_precise_monster_search(param_type="Name",
                                                           string="Skeleton, Giant",
                                                           tab_amount=tab_amount)
    giant_skeleton_xp = get_xp_from_single_enemy_cr(cr=giant_skeleton_cr,
                                                    tab_amount=tab_amount)
    tower_of_faith_enemies = [giant_skeleton_xp,
                              skeleton_xp,skeleton_xp,
                              skeleton_xp,skeleton_xp,
                              skeleton_xp,skeleton_xp,
                              skeleton_xp,skeleton_xp]
    tower_of_faith_difficulty = get_encounter_difficulty(player_levels=player_levels,
                                                         monster_xp_values=tower_of_faith_enemies,
                                                         tab_amount=tab_amount)

    print(tab_amount,"calculations complete :-3")

    print(tab_amount,"inner_castle_difficulty")
    print_dictionary_nicely(dict_in_question=inner_castle_difficulty, tab_amount=tab_amount+"\t")
    print(tab_amount,"tower_of_power_difficulty")
    print_dictionary_nicely(dict_in_question=tower_of_power_difficulty, tab_amount=tab_amount+"\t")
    print(tab_amount,"tower_of_faith_difficulty")
    print_dictionary_nicely(dict_in_question=tower_of_faith_difficulty,tab_amount=tab_amount+"\t")

if __name__ == "__main__":
    intro_the_magic_castle()