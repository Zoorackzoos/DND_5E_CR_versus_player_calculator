from src.monster_dict_files.michelangelo_bosses.the_warehouse.Bebop_the_Warthog import \
    bebop_the_warthog_monster_dict
from src.monster_dict_files.michelangelo_bosses.the_dmv.Metalhead import metalhead_monster_dict
from src.monster_dict_files.michelangelo_bosses.the_dmv.Tokka_the_evil_blue_turtle import \
    tokka_the_evil_blue_turtle_monster_dict
from src.monster_dict_files.michelangelo_phase_1_foot_clan_ninjas.phase_1_blue_foot_clan_ninja import \
    phase_1_blue_foot_clan_ninja_monster_dict
from src.monster_dict_files.michelangelo_phase_1_foot_clan_ninjas.phase_1_green_foot_clan_ninja import \
    phase_1_green_foot_clan_ninja_monster_dict
from src.monster_dict_files.michelangelo_phase_1_foot_clan_ninjas.phase_1_orange_foot_clan_ninja import \
    phase_1_orange_foot_clan_ninja_monster_dict
from src.monster_dict_files.michelangelo_phase_1_foot_clan_ninjas.phase_1_pink_foot_clan_ninja import \
    phase_1_pink_foot_clan_ninja_monster_dict
from src.monster_dict_files.michelangelo_phase_1_foot_clan_ninjas.phase_1_purple_foot_clan_ninja import \
    phase_1_purple_foot_clan_ninja_monster_dict
from src.monster_dict_files.michelangelo_phase_1_foot_clan_ninjas.phase_1_white_foot_clan_ninja import \
    phase_1_white_foot_clan_ninja_monster_dict
from src.monster_dict_files.michelangelo_phase_1_foot_clan_ninjas.phase_1_yellow_foot_clan_ninja import \
    phase_1_yellow_foot_clan_ninja_monster_dict
from src.monster_dict_files.michelangelo_bosses.the_dmv.Rahzar_the_evil_puppy_monster import rahzar_the_evil_puppy_monster_monster_dict
from src.monster_dict_files.michelangelo_rouge_monsters.Roadkill_Rodney import \
    roadkill_rodney_monster_dict
from src.monster_dict_files.michelangelo_rouge_monsters.evil_foot_clan_ninja_cyborg import \
    evil_foot_clan_ninja_cyborg_monster_dict
from src.universal_functions.spreadsheet_stuff.convert_csv_file_into_tsv_file import convert_csv_file_into_tsv_file
from src.universal_functions.spreadsheet_stuff.spreadsheet_updaters.update_homebrew_monster_spreadsheet import \
    update_homebrew_monster_spreadsheet
from src.universal_functions.stat_block_interpreter.interpret_markdown_stat_block import \
    interpret_markdown_stat_block_into_python_file

path_to_monster_spreadsheet_file = \
    "../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

def nuclear_interpret_phase_1_michelangelo_monster_files(tab_amount="\t"):
    """
    #TODO: if you want to update the values in this funciton. update the strings. becuase they're hardcoded

    :param tab_amount:
    :return:
    """
    print(tab_amount,"interpret_phase_1_michelangelo_monster_files")
    tab_amount += "\t"

    phase_1_michelangelo_boss_markdown_and_python_paths = \
    [
        [
            "monster_dict_files/michelangelo_bosses/Rahzar_the_evil_puppy_monster.md",
            "monster_dict_files/michelangelo_bosses/Rahzar_the_evil_puppy_monster.py"
        ],
        [
            "monster_dict_files/michelangelo_bosses/Tokka_the_evil_blue_turtle.md",
            "monster_dict_files/michelangelo_bosses/Tokka_the_evil_blue_turtle.py"
        ],
        [
            "monster_dict_files/michelangelo_bosses/Metalhead.md",
            "monster_dict_files/michelangelo_bosses/Metalhead.py"
        ],
        [
            "monster_dict_files/michelangelo_bosses/Bebop_the_Warthog.md",
            "monster_dict_files/michelangelo_bosses/Bebop_the_Warthog.py"
        ],
        [
            "monster_dict_files/michelangelo_bosses/Rocksteady_the_Rhinovirus.md",
            "monster_dict_files/michelangelo_bosses/Rocksteady_the_Rhinovirus.py"
        ],
    ]

    phase_1_michelangelo_phase_1_foot_clan_ninjas_markdown_and_python_paths = \
    [
        [
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_blue_foot_clan_ninja.md",
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_blue_foot_clan_ninja.py"
        ],
        [
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_green_foot_clan_ninja.md",
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_green_foot_clan_ninja.py"
        ],
        [
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_orange_foot_clan_ninja.md",
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_orange_foot_clan_ninja.py"
        ],
        [
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_pink_foot_clan_ninja.md",
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_pink_foot_clan_ninja.py"
        ],
        [
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_purple_foot_clan_ninja.md",
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_purple_foot_clan_ninja.py"
        ],
        [
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_white_foot_clan_ninja.md",
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_white_foot_clan_ninja.py"
        ],
        [
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_yellow_foot_clan_ninja.md",
            "monster_dict_files/michelangelo_phase_1_foot_clan_ninjas/phase_1_yellow_foot_clan_ninja.py"
        ]
    ]

    phase_1_michelangelo_rouge_enemies_markdown_and_python_paths = \
    [
        [
            "monster_dict_files/michelangelo_rouge_monsters/Roadkill_Rodney.md",
            "monster_dict_files/michelangelo_rouge_monsters/Roadkill_Rodney.py"
        ],
        [
            "monster_dict_files/michelangelo_rouge_monsters/evil_foot_clan_ninja_cyborg.md",
            "monster_dict_files/michelangelo_rouge_monsters/evil_foot_clan_ninja_cyborg.py"
        ],
        [
            "monster_dict_files/michelangelo_rouge_monsters/evil_foot_clan_ninja_cyborg.md",
            "monster_dict_files/michelangelo_rouge_monsters/evil_foot_clan_ninja_cyborg.py"
        ]
    ]

    print(tab_amount, "phase_1_michelangelo_boss_markdown_and_python_paths")
    for markdown_and_python_file_list in phase_1_michelangelo_boss_markdown_and_python_paths:
        interpret_markdown_stat_block_into_python_file(
            path_to_markdown_file=markdown_and_python_file_list[0],
            path_to_python_file=markdown_and_python_file_list[1],
            tab_amount=tab_amount+"\t"
        )

    print(tab_amount,"phase_1_michelangelo_phase_1_foot_clan_ninjas_markdown_and_python_paths")
    for markdown_and_python_file_list in phase_1_michelangelo_phase_1_foot_clan_ninjas_markdown_and_python_paths:
        interpret_markdown_stat_block_into_python_file(
            path_to_markdown_file=markdown_and_python_file_list[0],
            path_to_python_file=markdown_and_python_file_list[1],
            tab_amount=tab_amount+"\t"
        )

    print(tab_amount,"phase_1_michelangelo_rouge_enemies_markdown_and_python_paths")
    for markdown_and_python_file_list in phase_1_michelangelo_rouge_enemies_markdown_and_python_paths:
        interpret_markdown_stat_block_into_python_file(
            path_to_markdown_file=markdown_and_python_file_list[0],
            path_to_python_file=markdown_and_python_file_list[1],
            tab_amount=tab_amount+"\t"
        )

def nuclear_update_phase_1_michelangelo_monsters_onto_spreadsheet(tab_amount="\t"):
    print(tab_amount,"update_phase_1_michelangelo_monsters_onto_spreadsheet")
    tab_amount += "\t"

    phase_1_monster_and_boss_dicts = \
    [
        phase_1_blue_foot_clan_ninja_monster_dict,
        phase_1_green_foot_clan_ninja_monster_dict,
        phase_1_orange_foot_clan_ninja_monster_dict,
        phase_1_purple_foot_clan_ninja_monster_dict,
        phase_1_white_foot_clan_ninja_monster_dict,
        phase_1_yellow_foot_clan_ninja_monster_dict,
        phase_1_pink_foot_clan_ninja_monster_dict,
        rahzar_the_evil_puppy_monster_monster_dict,
        tokka_the_evil_blue_turtle_monster_dict,
        roadkill_rodney_monster_dict,
        evil_foot_clan_ninja_cyborg_monster_dict,
        metalhead_monster_dict
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

def interp_forest_rouge_monsters(tab_amount="\t"):
    forest_rouge_monster_markdown_and_python_paths = \
    [
        [
            "forest_rouge_monsters/bowling_ball_monster.md",
            "forest_rouge_monsters/bowling_ball_monster.py"
        ],
        [
            "forest_rouge_monsters/evil_generator_poison_flesh_turret.md",
            "forest_rouge_monsters/evil_generator_poison_flesh_turret.py"
        ]
    ]

    for markdown_and_python_file in forest_rouge_monster_markdown_and_python_paths:
        interpret_markdown_stat_block_into_python_file(
            path_to_markdown_file=markdown_and_python_file[0],
            path_to_python_file=markdown_and_python_file[1],
            tab_amount=tab_amount+"\t"
        )

def interp_calculus_monsters(tab_amount="\t"):

    calculus_monster_markdown_and_python_paths = \
        [
            [
                "calculus_monsters/calculus_monster_continuity.md",
                "calculus_monsters/calculus_monster_continuity.py"
            ],
            [
                "calculus_monsters/calculus_monster_cra.md",
                "calculus_monsters/calculus_monster_cra.py"
            ],
            [
                "calculus_monsters/calculus_monster_midterm.md",
                "calculus_monsters/calculus_monster_midterm.py"
            ],
            [
                "calculus_monsters/calculus_monster_polynomial.md",
                "calculus_monsters/calculus_monster_polynomial.py"
            ],
            [
                "calculus_monsters/calculus_monster_product_rule.md",
                "calculus_monsters/calculus_monster_product_rule.py"
            ],
        ]

    for markdown_and_python_file in calculus_monster_markdown_and_python_paths:
        interpret_markdown_stat_block_into_python_file(
            path_to_markdown_file=markdown_and_python_file[0],
            path_to_python_file=markdown_and_python_file[1],
            tab_amount=tab_amount + "\t"
        )

if __name__ == "__main__":
    tab_amount = "\t"
