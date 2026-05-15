def get_monster_amount_multiplier(monster_count,tab_amount="\t"):
    print(tab_amount,"get_monster_amount_multiplier")
    tab_amount += "\t"

    if monster_count == 1:
        return 1
    elif monster_count == 2:
        return 1.5
    elif 3 <= monster_count <= 6:
        return 2
    elif 7 <= monster_count <= 10:
        return 2.5
    elif 11 <= monster_count <= 14:
        return 3
    else:
        return 4