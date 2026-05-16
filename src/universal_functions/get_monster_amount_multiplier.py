def get_monster_amount_multiplier(monster_count,tab_amount="\t"):
    print(tab_amount,"get_monster_amount_multiplier")
    tab_amount += "\t"
    print(tab_amount,"monster_count =",monster_count)

    if monster_count == 1:
        print(tab_amount+"\t","1 --> *= 1")
        return 1
    elif monster_count == 2:
        print(tab_amount+"\t","2 --> *= 1.5")
        return 1.5
    elif 3 <= monster_count <= 6:
        print(tab_amount+"\t",monster_count,"--> *= 2")
        return 2
    elif 7 <= monster_count <= 10:
        print(tab_amount+"\t",monster_count,"--> *= 2.5")
        return 2.5
    elif 11 <= monster_count <= 14:
        print(tab_amount+"\t",monster_count,"--> *= 3")
        return 3
    else:
        print(tab_amount+"\t",monster_count,"--> *= 4")
        return 4