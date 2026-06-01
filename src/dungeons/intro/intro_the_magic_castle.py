from src.universal_functions.display.print_encounter_difficulty_concisely import print_encounter_difficulty_concisely
from src.universal_functions.get_xp_from_single_enemy_CR import get_xp_from_single_enemy_cr
from src.universal_functions.get_cr_from_precise_monster_search import get_cr_from_precise_monster_search
from src.universal_functions.get_encounter_difficulty.get_encounter_difficulty_from_xp_values import get_encounter_difficulty_from_xp_values
from src.universal_functions.spreadsheet_stuff.spreadsheet_updaters.update_encounter_feedback_spreadsheet import \
    update_encounter_feedback_spreadsheet


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
    intro_magic_castle_inner_castle_difficulty = get_encounter_difficulty_from_xp_values(
        player_levels=player_levels,
        monster_xp_values=inner_castle_enemies,
        encounter_name="intro_magic_castle_inner_castle_difficulty",
        tab_amount=tab_amount
    )

    skeleton_minotaur_cr = get_cr_from_precise_monster_search(param_type="Name",
                                                              string="Skeleton, Minotaur",
                                                              tab_amount=tab_amount)
    skeleton_minotaur_xp = get_xp_from_single_enemy_cr(cr=skeleton_minotaur_cr,
                                                       tab_amount=tab_amount)
    tower_of_power_enemies = [skeleton_minotaur_xp]
    intro_magic_castle_tower_of_power_difficulty = get_encounter_difficulty_from_xp_values(
        player_levels=player_levels,
        monster_xp_values=tower_of_power_enemies,
        encounter_name="intro_magic_castle_tower_of_power_difficulty",
        tab_amount=tab_amount
    )

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
    intro_magic_castle_tower_of_faith_difficulty = get_encounter_difficulty_from_xp_values(
        player_levels=player_levels,
        monster_xp_values=tower_of_faith_enemies,
        encounter_name="intro_magic_castle_tower_of_faith_difficulty",
        tab_amount=tab_amount
    )

    print(tab_amount,"calculations complete :-3")

    print(tab_amount,"intro_magic_castle_inner_castle_difficulty")
    print_encounter_difficulty_concisely(dict_in_question=intro_magic_castle_inner_castle_difficulty,
                            tab_amount=tab_amount+"\t")
    print(tab_amount,"intro_magic_castle_tower_of_power_difficulty")
    print_encounter_difficulty_concisely(dict_in_question=intro_magic_castle_tower_of_power_difficulty,
                            tab_amount=tab_amount+"\t")
    print(tab_amount,"intro_magic_castle_tower_of_faith_difficulty")
    print_encounter_difficulty_concisely(dict_in_question=intro_magic_castle_tower_of_faith_difficulty,
                            tab_amount=tab_amount+"\t")

    #============= update section =============
    print("\nupdate section")
    update_encounter_feedback_spreadsheet(encounter_dict=intro_magic_castle_inner_castle_difficulty,
                                          tab_amount=tab_amount+"\t")
    update_encounter_feedback_spreadsheet(encounter_dict=intro_magic_castle_tower_of_power_difficulty,
                                          tab_amount=tab_amount + "\t")
    update_encounter_feedback_spreadsheet(encounter_dict=intro_magic_castle_tower_of_faith_difficulty,
                                          tab_amount=tab_amount + "\t")


if __name__ == "__main__":
    intro_the_magic_castle()