

"""
for en-mass monsters that have to be updated because of balance reasons
this file exists.
i can feed in monster vars and then it updates the spreadsheet based on those.
    kinda backwards? i guess?
        whatever.

our database's header
Name	Size	Type	CR	URL	Font	Author	HP	AC	Speeds	Align.	STR	DEX	CON	INT	WIS	CHA	Sav. Throws	Skills	WRI	Senses	Languages	Additional	average_damage	attack_modifier	has_legendary_action	legendary_action_damage	has_flight	resistance_count	immunity_count	weakness_count	save_dc	is_spellcaster	regeneration_per_round	multiattack_count	ability_count	ability_cr_weight	recharge_damage	limited_use_damage	bonus_action_damage
"""
from src.dungeons.intro.monster_related.monster_dict_files.intro_foot_clan_ninjas.intro_blue_foot_clan_ninja_monster_dict import \
    intro_blue_foot_clan_ninja_monster_dict
from src.dungeons.intro.monster_related.monster_dict_files.intro_foot_clan_ninjas.intro_green_foot_clan_ninja_monster_dict import \
    intro_green_foot_clan_ninja_monster_dict
from src.dungeons.intro.monster_related.monster_dict_files.intro_foot_clan_ninjas.intro_orange_foot_clan_ninja_monster_dict import \
    intro_orange_foot_clan_ninja_monster_dict
from src.dungeons.intro.monster_related.monster_dict_files.intro_foot_clan_ninjas.intro_pink_foot_clan_ninja_monster_dict import \
    intro_pink_foot_clan_ninja_monster_dict
from src.dungeons.intro.monster_related.monster_dict_files.intro_foot_clan_ninjas.intro_purple_foot_clan_ninja_monster_dict import \
    intro_purple_foot_clan_ninja_monster_dict
from src.dungeons.intro.monster_related.monster_dict_files.intro_foot_clan_ninjas.intro_white_foot_clan_ninja_monster_dict import \
    intro_white_foot_clan_ninja_monster_dict
from src.dungeons.intro.monster_related.monster_dict_files.intro_foot_clan_ninjas.intro_yellow_foot_clan_ninja_monster_dict import \
    intro_yellow_foot_clan_ninja_monster_dict
from src.universal_functions.spreadsheet_stuff.spreadsheet_updaters.update_homebrew_monster_spreadsheet import \
    update_homebrew_monster_spreadsheet


def update_ninjas_into_intro_ninjas(tab_amount="\t"):
    print(tab_amount,"update_ninjas_into_intro_ninjas")
    tab_amount += "\t"

    monster_spreadsheet_updates_file_path_to_csv_file = "../../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

    list_of_intro_ninjas_to_update = \
        [
            intro_purple_foot_clan_ninja_monster_dict,
            intro_blue_foot_clan_ninja_monster_dict,
            intro_pink_foot_clan_ninja_monster_dict,
            intro_orange_foot_clan_ninja_monster_dict,
            intro_white_foot_clan_ninja_monster_dict,
            intro_yellow_foot_clan_ninja_monster_dict,
            intro_green_foot_clan_ninja_monster_dict
        ]

    for intro_ninja in list_of_intro_ninjas_to_update:
        (update_homebrew_monster_spreadsheet
        (
            monster_dict=intro_ninja,
            path_to_csv_file=monster_spreadsheet_updates_file_path_to_csv_file,
            tab_amount=tab_amount
        ))

if __name__ == "__main__":
    tab_amount = "\t"
    update_ninjas_into_intro_ninjas(tab_amount=tab_amount)