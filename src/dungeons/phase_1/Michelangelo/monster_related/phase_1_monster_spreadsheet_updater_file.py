from src.dungeons.phase_1.Michelangelo.monster_related.monster_dict_files.bosses.Tokka_the_evil_blue_turtle import \
    tokka_the_evil_blue_turtle_monster_dict
from src.dungeons.phase_1.Michelangelo.monster_related.monster_dict_files.phase_1_foot_clan_ninjas.phase_1_blue_foot_clan_ninja import \
    phase_1_blue_foot_clan_ninja_monster_dict
from src.dungeons.phase_1.Michelangelo.monster_related.monster_dict_files.phase_1_foot_clan_ninjas.phase_1_green_foot_clan_ninja import \
    phase_1_green_foot_clan_ninja_monster_dict
from src.dungeons.phase_1.Michelangelo.monster_related.monster_dict_files.phase_1_foot_clan_ninjas.phase_1_orange_foot_clan_ninja import \
    phase_1_orange_foot_clan_ninja_monster_dict
from src.dungeons.phase_1.Michelangelo.monster_related.monster_dict_files.phase_1_foot_clan_ninjas.phase_1_purple_foot_clan_ninja import \
    phase_1_purple_foot_clan_ninja_monster_dict
from src.dungeons.phase_1.Michelangelo.monster_related.monster_dict_files.phase_1_foot_clan_ninjas.phase_1_white_foot_clan_ninja import \
    phase_1_white_foot_clan_ninja_monster_dict
from src.dungeons.phase_1.Michelangelo.monster_related.monster_dict_files.phase_1_foot_clan_ninjas.phase_1_yellow_foot_clan_ninja import \
    phase_1_yellow_foot_clan_ninja_monster_dict
from src.dungeons.phase_1.Michelangelo.monster_related.monster_dict_files.bosses.Rahzar_the_evil_puppy_monster import rahzar_the_evil_puppy_monster_monster_dict
from src.universal_functions.spreadsheet_stuff.convert_csv_file_into_tsv_file import convert_csv_file_into_tsv_file
from src.universal_functions.spreadsheet_stuff.spreadsheet_updaters.update_homebrew_monster_spreadsheet import \
    update_homebrew_monster_spreadsheet

path_to_monster_spreadsheet_file = \
    "../../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

def update_DMV_monsters_onto_spreadsheet(tab_amount="\t"):
    print(tab_amount,"update_DMV_monsters_onto_spreadsheet")
    tab_amount += "\t"

    phase_1_monster_and_boss_dicts = \
    [
        phase_1_blue_foot_clan_ninja_monster_dict,
        phase_1_green_foot_clan_ninja_monster_dict,
        phase_1_orange_foot_clan_ninja_monster_dict,
        phase_1_purple_foot_clan_ninja_monster_dict,
        phase_1_white_foot_clan_ninja_monster_dict,
        phase_1_yellow_foot_clan_ninja_monster_dict,
        rahzar_the_evil_puppy_monster_monster_dict,
        tokka_the_evil_blue_turtle_monster_dict
    ]

    for monster_dict in phase_1_monster_and_boss_dicts:
        update_homebrew_monster_spreadsheet(
            monster_dict=monster_dict,
            path_to_csv_file=path_to_monster_spreadsheet_file,
            tab_amount=tab_amount,
        )

    convert_csv_file_into_tsv_file(
        path_to_csv_file=path_to_monster_spreadsheet_file,
        tab_amount=tab_amount
    )

if __name__ == "__main__":
    tab_amount = "\t"
    update_DMV_monsters_onto_spreadsheet(tab_amount=tab_amount)