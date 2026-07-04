from src.monster_dict_files.calculus_monsters.calculus_monster_continuity import \
    calculus_monster_continuity_monster_dict
from src.monster_dict_files.calculus_monsters.calculus_monster_cra import calculus_monster_cra_monster_dict
from src.monster_dict_files.calculus_monsters.calculus_monster_midterm import calculus_monster_midterm_monster_dict
from src.monster_dict_files.calculus_monsters.calculus_monster_polynomial import \
    calculus_monster_polynomial_monster_dict
from src.monster_dict_files.calculus_monsters.calculus_monster_product_rule import \
    calculus_monster_product_rule_monster_dict
from src.monster_dict_files.calculus_monsters.calculus_monster_quotient_rule import \
    calculus_monster_quotient_rule_monster_dict
from src.monster_dict_files.forest_rouge_monsters import evil_generator_poison_flesh_turret
from src.monster_dict_files.forest_rouge_monsters.bowling_ball_monster import bowling_ball_monster_monster_dict
from src.monster_dict_files.forest_rouge_monsters.evil_generator_poison_flesh_turret import \
    evil_generator_poison_flesh_turret_monster_dict
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
from src.monster_dict_files.calculus_monsters.calculus_monster_dervative import calculus_monster_derivative_monster_dict

path_to_monsters_csv_spreadsheet_file = \
    "../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"

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

def update_forest_rouge_monsters(tab_amount="\t"):
    forest_rouge_monsters_monster_dict_list = \
    [
        bowling_ball_monster_monster_dict,
        evil_generator_poison_flesh_turret_monster_dict
    ]

    for monster_dict in forest_rouge_monsters_monster_dict_list:
        update_homebrew_monster_spreadsheet(
            monster_dict=monster_dict,
            path_to_monsters_csv_file=path_to_monsters_csv_spreadsheet_file,
            tab_amount=tab_amount
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
            [
                "calculus_monsters/calculus_monster_dervative.md",
                "calculus_monsters/calculus_monster_dervative.py"
            ]
        ]

    for markdown_and_python_file in calculus_monster_markdown_and_python_paths:
        interpret_markdown_stat_block_into_python_file(
            path_to_markdown_file=markdown_and_python_file[0],
            path_to_python_file=markdown_and_python_file[1],
            tab_amount=tab_amount + "\t"
        )

def update_calculus_monsters(tab_amount="\t"):
    calculus_monsters_monster_dict_list = \
        [
            calculus_monster_continuity_monster_dict,
            calculus_monster_cra_monster_dict,
            calculus_monster_derivative_monster_dict,
            calculus_monster_midterm_monster_dict,
            calculus_monster_polynomial_monster_dict,
            calculus_monster_product_rule_monster_dict
        ]

    for monster_dict in calculus_monsters_monster_dict_list:
        update_homebrew_monster_spreadsheet(
            monster_dict=monster_dict,
            path_to_monsters_csv_file=path_to_monsters_csv_spreadsheet_file,
            tab_amount=tab_amount
        )

def manual_interpret_monster(tab_amount="\t"):
    """
    kinda pointless but it makes it cleaner in the if name == main section

    :param tab_amount:
    :return:
    """
    manual_markdown_path = "calculus_monsters/calculus_monster_quotient_rule.md"
    manual_python_path = "calculus_monsters/calculus_monster_quotient_rule.py"
    interpret_markdown_stat_block_into_python_file(
        path_to_markdown_file=manual_markdown_path,
        path_to_python_file=manual_python_path,
        tab_amount=tab_amount
    )

if __name__ == "__main__":
    tab_amount = "\t"
    update_homebrew_monster_spreadsheet(
        monster_dict=calculus_monster_quotient_rule_monster_dict,
        path_to_monsters_csv_file=path_to_monsters_csv_spreadsheet_file,
        tab_amount=tab_amount
    )