from src.universal_functions.vars import spreadsheet_enums


template_monster_parser_trial_monster_dict = \
    {
        spreadsheet_enums.SpreadsheetKeysEnums.NAME.value :
            'Template Monster, Parser Trial',
        spreadsheet_enums.SpreadsheetKeysEnums.SIZE.value :
            spreadsheet_enums.SizeEnums.MEDIUM.value,
        spreadsheet_enums.SpreadsheetKeysEnums.TYPE.value :
            spreadsheet_enums.CreatureTypesEnums.HUMANOID.value,
        spreadsheet_enums.SpreadsheetKeysEnums.CR.value :
            '????',
        spreadsheet_enums.SpreadsheetKeysEnums.URL.value :
            'https://docs.google.com/document/d/1Cn68O2DB9j-QPiJOO36mgH1ecj1EPC_C1wxkpORb_oA/edit?tab=t.0',
        spreadsheet_enums.SpreadsheetKeysEnums.FONT.value :
            spreadsheet_enums.FontTypesEnums.VIRASCO_2000.value,
        spreadsheet_enums.SpreadsheetKeysEnums.AUTHOR.value :
            spreadsheet_enums.AuthorFontTypesEnums.SHWIFTY_MEME_LORD.value,
        spreadsheet_enums.SpreadsheetKeysEnums.HP.value :
            100,
        spreadsheet_enums.SpreadsheetKeysEnums.AC.value :
            14,
        spreadsheet_enums.SpreadsheetKeysEnums.SPEEDS.value :
            30,
        spreadsheet_enums.SpreadsheetKeysEnums.ALIGN.value :
            'neutral evil',
        spreadsheet_enums.SpreadsheetKeysEnums.STR.value :
            18,
        spreadsheet_enums.SpreadsheetKeysEnums.DEX.value :
            18,
        spreadsheet_enums.SpreadsheetKeysEnums.CON.value :
            18,
        spreadsheet_enums.SpreadsheetKeysEnums.INT.value :
            10,
        spreadsheet_enums.SpreadsheetKeysEnums.WIS.value :
            10,
        spreadsheet_enums.SpreadsheetKeysEnums.CHA.value :
            10,
        spreadsheet_enums.SpreadsheetKeysEnums.SAVING_THROWS.value :
            ", ".join([spreadsheet_enums.SavingThrowsEnums.STR.value, spreadsheet_enums.SavingThrowsEnums.DEX.value]),
        spreadsheet_enums.SpreadsheetKeysEnums.SKILLS.value :
            ", ".join([spreadsheet_enums.SkillsEnums.ACROBATICS.value, spreadsheet_enums.SkillsEnums.STEALTH.value]),
        spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESSES_RESISTANCES_AND_IMMUNITIES.value :
            ", ".join([spreadsheet_enums.WRIEnums.BLUDGEONING_RESISTANT.value, spreadsheet_enums.WRIEnums.SLASHING_RESISTANT.value]),
        spreadsheet_enums.SpreadsheetKeysEnums.SENSES.value :
            spreadsheet_enums.SensesEnums.NORMAL.value,
        spreadsheet_enums.SpreadsheetKeysEnums.LANGUAGES.value :
            spreadsheet_enums.LanguagesEnums.COMMON.value,
        spreadsheet_enums.SpreadsheetKeysEnums.ADDITIONAL.value :
            'None',
        spreadsheet_enums.SpreadsheetKeysEnums.AVERAGE_DAMAGE.value :
            13,
        spreadsheet_enums.SpreadsheetKeysEnums.ATTACK_MODIFIER.value :
            4,
        spreadsheet_enums.SpreadsheetKeysEnums.HAS_LEGENDARY_ACTION.value :
            False,
        spreadsheet_enums.SpreadsheetKeysEnums.LEGENDARY_ACTION_DAMAGE.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.HAS_FLIGHT.value :
            False,
        spreadsheet_enums.SpreadsheetKeysEnums.RESISTANCE_COUNT.value :
            2,
        spreadsheet_enums.SpreadsheetKeysEnums.IMMUNITY_COUNT.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.WEAKNESS_COUNT.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.SAVE_DC.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.IS_SPELLCASTER.value :
            False,
        spreadsheet_enums.SpreadsheetKeysEnums.REGENERATION_PER_ROUND.value :
            6,
        spreadsheet_enums.SpreadsheetKeysEnums.MULTIATTACK_COUNT.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_COUNT.value :
            1,
        spreadsheet_enums.SpreadsheetKeysEnums.ABILITY_CR_WEIGHT.value :
            1,
        spreadsheet_enums.SpreadsheetKeysEnums.RECHARGE_DAMAGE.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.LIMITED_USE_DAMAGE.value :
            0,
        spreadsheet_enums.SpreadsheetKeysEnums.BONUS_ACTION_DAMAGE.value :
            0,
        "actions" :
            [{'name': 'action \\- tonfa strike', 'action_type': 'action', 'attack_type': 'melee_attack', 'hit_modifier': 4, 'damage': '2d8 + 4', 'damage_type': 'bludgening', 'range': 5}, {'name': 'reaction \\- tonfa block', 'action_type': 'reaction', 'notes': 'as a reaction he can make the attacker have disadvantage and have to re-roll their attack. “blocking” them.'}, {'name': 'passive \\- regeneration', 'action_type': 'passive', 'notes': '1d8 regeneration per turn. if anybody notices, do a investigation check. he has a Stockman pathogen inside him.'}],
    }
