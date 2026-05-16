# =====================================================
# D&D 5E Monster CR Calculator
# Based loosely on 2014 DMG rules
# =====================================================


CR_TABLE = [
    {
        "CR": 0,
        "hp_min": 1,
        "hp_max": 6,
        "dpr_min": 0,
        "dpr_max": 1,
        "ac": 13,
        "attack_bonus": 3
    },
    {
        "CR": 0.125,
        "hp_min": 7,
        "hp_max": 35,
        "dpr_min": 2,
        "dpr_max": 3,
        "ac": 13,
        "attack_bonus": 3
    },
    {
        "CR": 0.25,
        "hp_min": 36,
        "hp_max": 49,
        "dpr_min": 4,
        "dpr_max": 5,
        "ac": 13,
        "attack_bonus": 3
    },
    {
        "CR": 0.5,
        "hp_min": 50,
        "hp_max": 70,
        "dpr_min": 6,
        "dpr_max": 8,
        "ac": 13,
        "attack_bonus": 3
    },
    {
        "CR": 1,
        "hp_min": 71,
        "hp_max": 85,
        "dpr_min": 9,
        "dpr_max": 14,
        "ac": 13,
        "attack_bonus": 3
    },
    {
        "CR": 2,
        "hp_min": 86,
        "hp_max": 100,
        "dpr_min": 15,
        "dpr_max": 20,
        "ac": 13,
        "attack_bonus": 3
    },
    {
        "CR": 3,
        "hp_min": 101,
        "hp_max": 115,
        "dpr_min": 21,
        "dpr_max": 26,
        "ac": 13,
        "attack_bonus": 4
    },
    {
        "CR": 4,
        "hp_min": 116,
        "hp_max": 130,
        "dpr_min": 27,
        "dpr_max": 32,
        "ac": 14,
        "attack_bonus": 5
    },
    {
        "CR": 5,
        "hp_min": 131,
        "hp_max": 145,
        "dpr_min": 33,
        "dpr_max": 38,
        "ac": 15,
        "attack_bonus": 6
    },
    {
        "CR": 6,
        "hp_min": 146,
        "hp_max": 160,
        "dpr_min": 39,
        "dpr_max": 44,
        "ac": 15,
        "attack_bonus": 6
    },
    {
        "CR": 7,
        "hp_min": 161,
        "hp_max": 175,
        "dpr_min": 45,
        "dpr_max": 50,
        "ac": 15,
        "attack_bonus": 6
    },
    {
        "CR": 8,
        "hp_min": 176,
        "hp_max": 190,
        "dpr_min": 51,
        "dpr_max": 56,
        "ac": 16,
        "attack_bonus": 7
    },
    {
        "CR": 9,
        "hp_min": 191,
        "hp_max": 205,
        "dpr_min": 57,
        "dpr_max": 62,
        "ac": 16,
        "attack_bonus": 7
    },
    {
        "CR": 10,
        "hp_min": 206,
        "hp_max": 220,
        "dpr_min": 63,
        "dpr_max": 68,
        "ac": 17,
        "attack_bonus": 7
    }
]


# =====================================================
# Utility Functions
# =====================================================


def get_defensive_CR(hit_points,tab_amount="\t"):
    print(tab_amount,"get_defensive_CR")
    tab_amount += "\t"

    for row in CR_TABLE:
        if row["hp_min"] <= hit_points <= row["hp_max"]:
            return row["CR"]

    return CR_TABLE[-1]["CR"]



def get_offensive_CR(damage_per_round,tab_amount="\t"):
    print(tab_amount,"get_offensive_CR")
    tab_amount += "\t"

    for row in CR_TABLE:
        if row["dpr_min"] <= damage_per_round <= row["dpr_max"]:
            return row["CR"]

    return CR_TABLE[-1]["CR"]



def get_expected_values_from_CR(CR,tab_amount="\t"):
    print(tab_amount,"get_expected_values_from_CR")
    tab_amount += "\t"

    for row in CR_TABLE:
        if row["CR"] == CR:
            return row

    return CR_TABLE[-1]


# =====================================================
# Main CR Calculator
# =====================================================
def get_CR_from_monster(
        hit_points,
        armor_class,
        damage_per_round,
        attack_bonus,
        has_legendary_action,
        has_flight,
        resistance_count,
        immunity_count,
        save_dc,
        is_spellcaster,
        regeneration_per_round,
        multiattack_count,
        ability_count,
        tab_amount="\t"
):
    print(tab_amount,"get_CR_from_monster")
    tab_amount += "\t"

    # -------------------------------
    # Defensive CR
    # -------------------------------
    if resistance_count > 0:
        print(tab_amount+"\t","resistance count =",resistance_count)
        print(tab_amount+"\t","before: hit_points =",hit_points)
        hit_points *= 1 + (0.25 * resistance_count)
        print(tab_amount+"\t","after: hit_points =",hit_points)

    if immunity_count > 0:
        print(tab_amount+"\t","immunity_count = ",immunity_count)
        print(tab_amount+"\t","before: hit_points =",hit_points)
        hit_points *= 1 + (0.5 * immunity_count)
        print(tab_amount+"\t","after: hit_points =",hit_points)

    if has_flight:
        print(tab_amount+"\t","has_flight = ",has_flight)
        print(tab_amount+"\t","before: hit_points =",hit_points)
        hit_points *= 1.25
        print(tab_amount+"\t","after: hit_points =",hit_points)

    if regeneration_per_round > 0:
        print(tab_amount+"\t","regeneration_per_round = ",regeneration_per_round)
        print(tab_amount+"\t","before: hit_points =",hit_points)
        hit_points += regeneration_per_round * 3
        print(tab_amount+"\t","after: hit_points =",hit_points)

    defensive_CR = get_defensive_CR(hit_points=hit_points,tab_amount=tab_amount)
    print(tab_amount,"defensive_CR =",defensive_CR)

    defensive_stats = get_expected_values_from_CR(CR=defensive_CR,tab_amount=tab_amount)
    print(tab_amount,"defensive_stats =",defensive_stats)

    expected_ac = defensive_stats["ac"]
    ac_difference = armor_class - expected_ac
    defensive_CR += ac_difference / 2


    # -------------------------------
    # Offensive CR
    # -------------------------------
    if save_dc > 0:
        print(tab_amount+"\t","save_dc = ",save_dc)
        print(tab_amount+"\t","before: damage_per_round =",damage_per_round)
        damage_per_round *= 1.15
        print(tab_amount+"\t","after: damage_per_round =",damage_per_round)

    if is_spellcaster:
        print(tab_amount+"\t","is_spellcaster = ",is_spellcaster)
        print(tab_amount+"\t","before: damage_per_round =",damage_per_round)
        damage_per_round *= 1.3
        print(tab_amount+"\t","after: damage_per_round =",damage_per_round)

    if has_legendary_action:
        print(tab_amount+"\t","has_legendary_action = ",has_legendary_action)
        print(tab_amount+"\t","before: damage_per_round =",damage_per_round)
        damage_per_round *= 1.5
        print(tab_amount+"\t","after: damage_per_round =",damage_per_round)

    if multiattack_count > 0:
        print(tab_amount+"\t","multiattack_count = ",multiattack_count)
        print(tab_amount+"\t","before: damage_per_round =",damage_per_round)
        damage_per_round *= multiattack_count
        print(tab_amount+"\t", "after: damage_per_round =", damage_per_round)

    if ability_count > 0:
        print(tab_amount+"\t","ability_count = ",ability_count)
        print(tab_amount+"\t","before: damage_per_round =",damage_per_round)
        damage_per_round += ability_count
        print(tab_amount+"\t","after: damage_per_round =",damage_per_round)

    offensive_CR = get_offensive_CR(damage_per_round=damage_per_round,tab_amount=tab_amount)
    print(tab_amount,"offensive_CR =",offensive_CR)

    offensive_stats = get_expected_values_from_CR(CR=offensive_CR,tab_amount=tab_amount)
    print(tab_amount,"offensive_stats =",offensive_stats)

    expected_attack_bonus = offensive_stats["attack_bonus"]
    print(tab_amount,"expected_attack_bonus =",expected_attack_bonus)

    attack_difference = attack_bonus - expected_attack_bonus
    print(tab_amount,"attack_difference =",attack_difference)

    offensive_CR += attack_difference / 2
    print(tab_amount,"offensive_CR =",offensive_CR)
    print()

    # -------------------------------
    # Final CR
    # -------------------------------

    final_CR = (defensive_CR + offensive_CR) / 2

    print(tab_amount,"defensive_CR =",defensive_CR)
    print(tab_amount,"offensive_CR =",offensive_CR)
    print(tab_amount,"final_CR =",final_CR)

    if final_CR >= 1:
        final_CR = int(round(final_CR, 0))
    else:
        final_CR = round(final_CR, 2)

    return final_CR


def plug_monster_var_values_into_get_CR_from_monster(monster_var,tab_amount="\t"):
    print(tab_amount,"plug_monster_var_values_into_get_CR")
    tab_amount += "\t"

    return get_CR_from_monster(
        hit_points=monster_var["hp"],
        armor_class=monster_var["ac"],
        damage_per_round=monster_var["average_damage"],
        attack_bonus=monster_var["attack_bonus"],
        has_legendary_action=monster_var["has_legendary_action"],
        has_flight=monster_var["has_flight"],
        resistance_count=monster_var["resistance_count"],
        immunity_count=monster_var["immunity_count"],
        save_dc=monster_var["save_dc"],
        is_spellcaster=monster_var["is_spellcaster"],
        regeneration_per_round=monster_var["regeneration_per_round"],
        multiattack_count=monster_var["multiattack_count"],
        ability_count=monster_var["ability_count"],
        tab_amount=tab_amount
                        )