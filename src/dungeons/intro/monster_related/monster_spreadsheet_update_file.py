

"""
for en-mass monsters that have to be updated because of balance reasons
this file exists.
i can feed in monster vars and then it updates the spreadsheet based on those.
    kinda backwards? i guess?
        whatever.

our database's header
Name	Size	Type	CR	URL	Font	Author	HP	AC	Speeds	Align.	STR	DEX	CON	INT	WIS	CHA	Sav. Throws	Skills	WRI	Senses	Languages	Additional	average_damage	attack_modifier	has_legendary_action	legendary_action_damage	has_flight	resistance_count	immunity_count	weakness_count	save_dc	is_spellcaster	regeneration_per_round	multiattack_count	ability_count	ability_cr_weight	recharge_damage	limited_use_damage	bonus_action_damage
"""
from src.dungeons.intro.intro_the_magic_spire import into_the_magic_spire_path_to_csv_file
from src.universal_functions.get_average_damage import get_average_damage
from src.universal_functions.spreadsheet_stuff.spreadsheet_updaters.update_homebrew_monster_spreadsheet import \
    update_homebrew_monster_spreadsheet
from src.universal_functions.vars import spreadsheet_enums
from src.universal_functions.vars.get_stringified_list_of_enums import get_stringified_list_of_enums
from src.universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums


def update_ninjas_into_intro_ninjas(tab_amount="\t"):
    print(tab_amount,"update_ninjas_into_intro_ninjas")
    tab_amount += "\t"

    monster_spreadsheet_updates_file_path_to_csv_file = "../../../../sheets/monsters_all_stats_homebrew.csv"

    # for the love of your life.
    # please use mr. intro_purple here as a default for every monster dict here on out
    intro_purple_foot_clan_ninja_monster_dict = \
        {
            spreadsheet_enums.SpreadsheetKeysEnums.NAME.value :
                "intro purple foot clan ninja",
            spreadsheet_enums.SpreadsheetKeysEnums.SIZE.value :
                spreadsheet_enums.SizeEnums.MEDIUM.value,
            spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value :
                spreadsheet_enums.CreatureTypesEnums.HUMANOID.value,
            spreadsheet_enums.SpreadsheetKeysEnums.CR.value :
                spreadsheet_enums.CRTypeEnums.CR_ONE_FORTH_WEAK.value,
            spreadsheet_enums.SpreadsheetKeysEnums.URL.value :
                "https://docs.google.com/document/d/1JUiihzhgPS4Rg1ofP1xjbswx8sFso69X1KWdyWuTT78/edit?tab=t.0",
            spreadsheet_enums.SpreadsheetKeysEnums.FONT.value :
                spreadsheet_enums.FontTypesEnums.VIRASCO_2000.value,
            spreadsheet_enums.SpreadsheetKeysEnums.AUTHOR.value :
                spreadsheet_enums.AuthorFontTypesEnums.SHWIFTY_MEME_LORD.value,
            spreadsheet_enums.SpreadsheetKeysEnums.HP.value :
                20,
            spreadsheet_enums.SpreadsheetKeysEnums.AC.value :
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.SPEEDS.value :
                30,
            spreadsheet_enums.SpreadsheetKeysEnums.ALIGN.value :
                spreadsheet_enums.AlignmentEnums.NEUTRAL_EVIL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.STR.value :
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.DEX.value :
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.CON.value :
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.INT.value :
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.WIS.value :
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.CHA.value :
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVING_THROWS.value :
                spreadsheet_enums.SavingThrowsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.SKILLS.value :
                spreadsheet_enums.SkillsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESSES_RESISTANCES_AND_IMMUNITIES.value :
                spreadsheet_enums.WRIEnums.NONE,
            spreadsheet_enums.SpreadsheetKeysEnums.SENSES :
                spreadsheet_enums.SensesEnums.NORMAL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.LANGUAGES.value :
                get_stringified_list_of_enums
                (
                    list_of_enums=[spreadsheet_enums.LanguagesEnums.COMMON.value,
                                  spreadsheet_enums.LanguagesEnums.THIEVES_CANT.value],
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ADDITIONAL.value :
                "None",
            spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value :
                get_average_damage
                (
                    dice_dict=
                    {
                        6 : 1,
                        "constant" : 2
                    },
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ATTACK_MODIFIER.value :
                3,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_LEGENDARY_ACTION.value :
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.LEGENDARY_ACTION_DAMAGE.value :
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_FLIGHT.value :
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.RESISTANCE_COUNT.value :
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value :
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESS_COUNT.value :
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVE_DC.value :
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IS_SPELLCASTER.value :
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.REGENERATION_PER_ROUND.value :
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.MULTIATTACK_COUNT.value :
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_COUNT.value :
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_CR_WEIGHT.value :
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.RECHARGE_DAMAGE.value :
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.LIMITED_USE_DAMAGE.value :
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.BONUS_ACTION_DAMAGE.value :
                0,
        }

    intro_blue_foot_clan_ninja_monster_dict = \
        {
            spreadsheet_enums.SpreadsheetKeysEnums.NAME.value:
                "intro blue foot clan ninja",
            spreadsheet_enums.SpreadsheetKeysEnums.SIZE.value:
                spreadsheet_enums.SizeEnums.MEDIUM.value,
            spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value:
                spreadsheet_enums.CreatureTypesEnums.HUMANOID.value,
            spreadsheet_enums.SpreadsheetKeysEnums.CR.value:
                spreadsheet_enums.CRTypeEnums.CR_ONE_HALF_MINOR.value,
            spreadsheet_enums.SpreadsheetKeysEnums.URL.value:
                "https://docs.google.com/document/d/1JUiihzhgPS4Rg1ofP1xjbswx8sFso69X1KWdyWuTT78/edit?tab=t.0",
            spreadsheet_enums.SpreadsheetKeysEnums.FONT.value:
                spreadsheet_enums.FontTypesEnums.VIRASCO_2000.value,
            spreadsheet_enums.SpreadsheetKeysEnums.AUTHOR.value:
                spreadsheet_enums.AuthorFontTypesEnums.SHWIFTY_MEME_LORD.value,
            spreadsheet_enums.SpreadsheetKeysEnums.HP.value:
                20,
            spreadsheet_enums.SpreadsheetKeysEnums.AC.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.SPEEDS.value:
                30,
            spreadsheet_enums.SpreadsheetKeysEnums.ALIGN.value:
                spreadsheet_enums.AlignmentEnums.NEUTRAL_EVIL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.STR.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.DEX.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.CON.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.INT.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.WIS.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.CHA.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVING_THROWS.value:
                spreadsheet_enums.SavingThrowsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.SKILLS.value:
                spreadsheet_enums.SkillsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESSES_RESISTANCES_AND_IMMUNITIES.value:
                spreadsheet_enums.WRIEnums.NONE,
            spreadsheet_enums.SpreadsheetKeysEnums.SENSES:
                spreadsheet_enums.SensesEnums.NORMAL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.LANGUAGES.value:
                get_stringified_list_of_enums
                    (
                    list_of_enums=[spreadsheet_enums.LanguagesEnums.COMMON.value,
                                   spreadsheet_enums.LanguagesEnums.THIEVES_CANT.value],
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ADDITIONAL.value:
                "None",
            spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value:
                get_average_damage
                    (
                    dice_dict=
                    {
                        6: 3,
                        "constant": 3
                    },
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ATTACK_MODIFIER.value:
                5,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_LEGENDARY_ACTION.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.LEGENDARY_ACTION_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_FLIGHT.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.RESISTANCE_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESS_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVE_DC.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IS_SPELLCASTER.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.REGENERATION_PER_ROUND.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.MULTIATTACK_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_CR_WEIGHT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.RECHARGE_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.LIMITED_USE_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.BONUS_ACTION_DAMAGE.value:
                0,
        }

    intro_pink_foot_clan_ninja_monster_dict = \
        {
            spreadsheet_enums.SpreadsheetKeysEnums.NAME.value:
                "intro pink foot clan ninja",
            spreadsheet_enums.SpreadsheetKeysEnums.SIZE.value:
                spreadsheet_enums.SizeEnums.MEDIUM.value,
            spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value:
                spreadsheet_enums.CreatureTypesEnums.HUMANOID.value,
            spreadsheet_enums.SpreadsheetKeysEnums.CR.value:
                spreadsheet_enums.CRTypeEnums.CR_ONE_HALF_MINOR.value,
            spreadsheet_enums.SpreadsheetKeysEnums.URL.value:
                "https://docs.google.com/document/d/1JUiihzhgPS4Rg1ofP1xjbswx8sFso69X1KWdyWuTT78/edit?tab=t.0",
            spreadsheet_enums.SpreadsheetKeysEnums.FONT.value:
                spreadsheet_enums.FontTypesEnums.VIRASCO_2000.value,
            spreadsheet_enums.SpreadsheetKeysEnums.AUTHOR.value:
                spreadsheet_enums.AuthorFontTypesEnums.SHWIFTY_MEME_LORD.value,
            spreadsheet_enums.SpreadsheetKeysEnums.HP.value:
                50,
            spreadsheet_enums.SpreadsheetKeysEnums.AC.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.SPEEDS.value:
                30,
            spreadsheet_enums.SpreadsheetKeysEnums.ALIGN.value:
                spreadsheet_enums.AlignmentEnums.NEUTRAL_EVIL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.STR.value:
                14,
            spreadsheet_enums.SpreadsheetKeysEnums.DEX.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.CON.value:
                16,
            spreadsheet_enums.SpreadsheetKeysEnums.INT.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.WIS.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.CHA.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVING_THROWS.value:
                spreadsheet_enums.SavingThrowsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.SKILLS.value:
                spreadsheet_enums.SkillsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESSES_RESISTANCES_AND_IMMUNITIES.value:
                spreadsheet_enums.WRIEnums.NONE,
            spreadsheet_enums.SpreadsheetKeysEnums.SENSES:
                spreadsheet_enums.SensesEnums.NORMAL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.LANGUAGES.value:
                get_stringified_list_of_enums
                    (
                    list_of_enums=[
                        spreadsheet_enums.LanguagesEnums.COMMON.value,
                        spreadsheet_enums.LanguagesEnums.THIEVES_CANT.value
                    ],
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ADDITIONAL.value:
                "None",
            spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value:
                get_average_damage
                    (
                    dice_dict=
                    {
                        8: 1,
                        "constant": 2
                    },
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ATTACK_MODIFIER.value:
                3,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_LEGENDARY_ACTION.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.LEGENDARY_ACTION_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_FLIGHT.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.RESISTANCE_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESS_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVE_DC.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IS_SPELLCASTER.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.REGENERATION_PER_ROUND.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.MULTIATTACK_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_CR_WEIGHT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.RECHARGE_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.LIMITED_USE_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.BONUS_ACTION_DAMAGE.value:
                0,
        }

    intro_orange_foot_clan_ninja_monster_dict = \
        {
            spreadsheet_enums.SpreadsheetKeysEnums.NAME.value:
                "intro orange foot clan ninja",
            spreadsheet_enums.SpreadsheetKeysEnums.SIZE.value:
                spreadsheet_enums.SizeEnums.MEDIUM.value,
            spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value:
                spreadsheet_enums.CreatureTypesEnums.HUMANOID.value,
            spreadsheet_enums.SpreadsheetKeysEnums.CR.value:
                spreadsheet_enums.CRTypeEnums.CR_ONE_HALF_MINOR.value,
            spreadsheet_enums.SpreadsheetKeysEnums.URL.value:
                "https://docs.google.com/document/d/1JUiihzhgPS4Rg1ofP1xjbswx8sFso69X1KWdyWuTT78/edit?tab=t.0",
            spreadsheet_enums.SpreadsheetKeysEnums.FONT.value:
                spreadsheet_enums.FontTypesEnums.VIRASCO_2000.value,
            spreadsheet_enums.SpreadsheetKeysEnums.AUTHOR.value:
                spreadsheet_enums.AuthorFontTypesEnums.SHWIFTY_MEME_LORD.value,
            spreadsheet_enums.SpreadsheetKeysEnums.HP.value:
                20,
            spreadsheet_enums.SpreadsheetKeysEnums.AC.value:
                15,
            spreadsheet_enums.SpreadsheetKeysEnums.SPEEDS.value:
                30,
            spreadsheet_enums.SpreadsheetKeysEnums.ALIGN.value:
                spreadsheet_enums.AlignmentEnums.NEUTRAL_EVIL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.STR.value:
                14,
            spreadsheet_enums.SpreadsheetKeysEnums.DEX.value:
                14,
            spreadsheet_enums.SpreadsheetKeysEnums.CON.value:
                16,
            spreadsheet_enums.SpreadsheetKeysEnums.INT.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.WIS.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.CHA.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVING_THROWS.value:
                spreadsheet_enums.SavingThrowsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.SKILLS.value:
                spreadsheet_enums.SkillsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESSES_RESISTANCES_AND_IMMUNITIES.value:
                spreadsheet_enums.WRIEnums.NONE,
            spreadsheet_enums.SpreadsheetKeysEnums.SENSES:
                spreadsheet_enums.SensesEnums.NORMAL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.LANGUAGES.value:
                get_stringified_list_of_enums
                    (
                    list_of_enums=[
                        spreadsheet_enums.LanguagesEnums.COMMON.value,
                        spreadsheet_enums.LanguagesEnums.THIEVES_CANT.value
                    ],
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ADDITIONAL.value:
                "None",
            spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value:
                get_average_damage
                    (
                    dice_dict=
                    {
                        12: 1,
                        "constant": 4
                    },
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ATTACK_MODIFIER.value:
                4,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_LEGENDARY_ACTION.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.LEGENDARY_ACTION_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_FLIGHT.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.RESISTANCE_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESS_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVE_DC.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IS_SPELLCASTER.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.REGENERATION_PER_ROUND.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.MULTIATTACK_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_CR_WEIGHT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.RECHARGE_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.LIMITED_USE_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.BONUS_ACTION_DAMAGE.value:
                0,
        }

    intro_white_foot_clan_ninja_monster_dict = \
        {
            spreadsheet_enums.SpreadsheetKeysEnums.NAME.value:
                "intro white foot clan ninja",
            spreadsheet_enums.SpreadsheetKeysEnums.SIZE.value:
                spreadsheet_enums.SizeEnums.MEDIUM.value,
            spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value:
                spreadsheet_enums.CreatureTypesEnums.HUMANOID.value,
            spreadsheet_enums.SpreadsheetKeysEnums.CR.value:
                spreadsheet_enums.CRTypeEnums.CR_ONE_HALF_MINOR.value,
            spreadsheet_enums.SpreadsheetKeysEnums.URL.value:
                "https://docs.google.com/document/d/1JUiihzhgPS4Rg1ofP1xjbswx8sFso69X1KWdyWuTT78/edit?tab=t.0",
            spreadsheet_enums.SpreadsheetKeysEnums.FONT.value:
                spreadsheet_enums.FontTypesEnums.VIRASCO_2000.value,
            spreadsheet_enums.SpreadsheetKeysEnums.AUTHOR.value:
                spreadsheet_enums.AuthorFontTypesEnums.SHWIFTY_MEME_LORD.value,
            spreadsheet_enums.SpreadsheetKeysEnums.HP.value:
                25,
            spreadsheet_enums.SpreadsheetKeysEnums.AC.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.SPEEDS.value:
                30,
            spreadsheet_enums.SpreadsheetKeysEnums.ALIGN.value:
                spreadsheet_enums.AlignmentEnums.NEUTRAL_EVIL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.STR.value:
                14,
            spreadsheet_enums.SpreadsheetKeysEnums.DEX.value:
                14,
            spreadsheet_enums.SpreadsheetKeysEnums.CON.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.INT.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.WIS.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.CHA.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVING_THROWS.value:
                spreadsheet_enums.SavingThrowsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.SKILLS.value:
                spreadsheet_enums.SkillsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESSES_RESISTANCES_AND_IMMUNITIES.value:
                spreadsheet_enums.WRIEnums.NONE,
            spreadsheet_enums.SpreadsheetKeysEnums.SENSES:
                spreadsheet_enums.SensesEnums.NORMAL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.LANGUAGES.value:
                get_stringified_list_of_enums
                    (
                    list_of_enums=[
                        spreadsheet_enums.LanguagesEnums.COMMON.value,
                        spreadsheet_enums.LanguagesEnums.THIEVES_CANT.value
                    ],
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ADDITIONAL.value:
                "None",
            spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value:
                get_average_damage
                    (
                    dice_dict=
                    {
                        12: 1,
                        "constant": 4
                    },
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ATTACK_MODIFIER.value:
                3,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_LEGENDARY_ACTION.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.LEGENDARY_ACTION_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_FLIGHT.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.RESISTANCE_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESS_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVE_DC.value:
                18,
            spreadsheet_enums.SpreadsheetKeysEnums.IS_SPELLCASTER.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.REGENERATION_PER_ROUND.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.MULTIATTACK_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_COUNT.value:
                1,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_CR_WEIGHT.value:
                2,
            spreadsheet_enums.SpreadsheetKeysEnums.RECHARGE_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.LIMITED_USE_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.BONUS_ACTION_DAMAGE.value:
                get_average_damage(
                    dice_dict=
                    {
                        12: 1,
                        "constant": 4
                    },
                    tab_amount=tab_amount
                ),
        }

    intro_yellow_foot_clan_ninja_monster_dict = \
        {
            spreadsheet_enums.SpreadsheetKeysEnums.NAME.value:
                "intro yellow foot clan ninja",
            spreadsheet_enums.SpreadsheetKeysEnums.SIZE.value:
                spreadsheet_enums.SizeEnums.MEDIUM.value,
            spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value:
                spreadsheet_enums.CreatureTypesEnums.HUMANOID.value,
            spreadsheet_enums.SpreadsheetKeysEnums.CR.value:
                spreadsheet_enums.CRTypeEnums.CR_ONE_HALF_MINOR.value,
            spreadsheet_enums.SpreadsheetKeysEnums.URL.value:
                "https://docs.google.com/document/d/1JUiihzhgPS4Rg1ofP1xjbswx8sFso69X1KWdyWuTT78/edit?tab=t.0",
            spreadsheet_enums.SpreadsheetKeysEnums.FONT.value:
                spreadsheet_enums.FontTypesEnums.VIRASCO_2000.value,
            spreadsheet_enums.SpreadsheetKeysEnums.AUTHOR.value:
                spreadsheet_enums.AuthorFontTypesEnums.SHWIFTY_MEME_LORD.value,
            spreadsheet_enums.SpreadsheetKeysEnums.HP.value:
                20,
            spreadsheet_enums.SpreadsheetKeysEnums.AC.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.SPEEDS.value:
                30,
            spreadsheet_enums.SpreadsheetKeysEnums.ALIGN.value:
                spreadsheet_enums.AlignmentEnums.NEUTRAL_EVIL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.STR.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.DEX.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.CON.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.INT.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.WIS.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.CHA.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVING_THROWS.value:
                spreadsheet_enums.SavingThrowsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.SKILLS.value:
                spreadsheet_enums.SkillsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESSES_RESISTANCES_AND_IMMUNITIES.value:
                spreadsheet_enums.WRIEnums.NONE,
            spreadsheet_enums.SpreadsheetKeysEnums.SENSES:
                spreadsheet_enums.SensesEnums.NORMAL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.LANGUAGES.value:
                get_stringified_list_of_enums
                    (
                    list_of_enums=[spreadsheet_enums.LanguagesEnums.COMMON.value,
                                   spreadsheet_enums.LanguagesEnums.THIEVES_CANT.value],
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ADDITIONAL.value:
                "None",
            spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value:
                get_average_damage
                    (
                    dice_dict=
                    {
                        8: 1,
                        "constant": 4
                    },
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ATTACK_MODIFIER.value:
                5,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_LEGENDARY_ACTION.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.LEGENDARY_ACTION_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_FLIGHT.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.RESISTANCE_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESS_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVE_DC.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IS_SPELLCASTER.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.REGENERATION_PER_ROUND.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.MULTIATTACK_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_COUNT.value:
                1,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_CR_WEIGHT.value:
                2,
            spreadsheet_enums.SpreadsheetKeysEnums.RECHARGE_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.LIMITED_USE_DAMAGE.value:
                get_average_damage(
                    dice_dict=
                    {
                        6 : 4,
                        "constant" : 4
                    },
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.BONUS_ACTION_DAMAGE.value:
                0,
        }

    intro_green_foot_clan_ninja_monster_dict = \
        {
            spreadsheet_enums.SpreadsheetKeysEnums.NAME.value:
                "intro green foot clan ninja",
            spreadsheet_enums.SpreadsheetKeysEnums.SIZE.value:
                spreadsheet_enums.SizeEnums.MEDIUM.value,
            spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value:
                spreadsheet_enums.CreatureTypesEnums.HUMANOID.value,
            spreadsheet_enums.SpreadsheetKeysEnums.CR.value:
                spreadsheet_enums.CRTypeEnums.CR_ONE_FORTH_WEAK.value,
            spreadsheet_enums.SpreadsheetKeysEnums.URL.value:
                "https://docs.google.com/document/d/1JUiihzhgPS4Rg1ofP1xjbswx8sFso69X1KWdyWuTT78/edit?tab=t.0",
            spreadsheet_enums.SpreadsheetKeysEnums.FONT.value:
                spreadsheet_enums.FontTypesEnums.VIRASCO_2000.value,
            spreadsheet_enums.SpreadsheetKeysEnums.AUTHOR.value:
                spreadsheet_enums.AuthorFontTypesEnums.SHWIFTY_MEME_LORD.value,
            spreadsheet_enums.SpreadsheetKeysEnums.HP.value:
                15,
            spreadsheet_enums.SpreadsheetKeysEnums.AC.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.SPEEDS.value:
                30,
            spreadsheet_enums.SpreadsheetKeysEnums.ALIGN.value:
                spreadsheet_enums.AlignmentEnums.NEUTRAL_EVIL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.STR.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.DEX.value:
                14,
            spreadsheet_enums.SpreadsheetKeysEnums.CON.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.INT.value:
                12,
            spreadsheet_enums.SpreadsheetKeysEnums.WIS.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.CHA.value:
                10,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVING_THROWS.value:
                spreadsheet_enums.SavingThrowsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.SKILLS.value:
                spreadsheet_enums.SkillsEnums.NONE.value,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESSES_RESISTANCES_AND_IMMUNITIES.value:
                spreadsheet_enums.WRIEnums.NONE,
            spreadsheet_enums.SpreadsheetKeysEnums.SENSES:
                spreadsheet_enums.SensesEnums.NORMAL.value,
            spreadsheet_enums.SpreadsheetKeysEnums.LANGUAGES.value:
                get_stringified_list_of_enums
                    (
                    list_of_enums=[spreadsheet_enums.LanguagesEnums.COMMON.value,
                                   spreadsheet_enums.LanguagesEnums.THIEVES_CANT.value],
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ADDITIONAL.value:
                "None",
            spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value:
                get_average_damage
                    (
                    dice_dict=
                    {
                        8: 1,
                        "constant": 4
                    },
                    tab_amount=tab_amount
                ),
            spreadsheet_enums.SpreadsheetKeysEnums.ATTACK_MODIFIER.value:
                4,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_LEGENDARY_ACTION.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.LEGENDARY_ACTION_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.HAS_FLIGHT.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.RESISTANCE_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESS_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.SAVE_DC.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.IS_SPELLCASTER.value:
                False,
            spreadsheet_enums.SpreadsheetKeysEnums.REGENERATION_PER_ROUND.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.MULTIATTACK_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_COUNT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_CR_WEIGHT.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.RECHARGE_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.LIMITED_USE_DAMAGE.value:
                0,
            spreadsheet_enums.SpreadsheetKeysEnums.BONUS_ACTION_DAMAGE.value:
                0,
        }

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