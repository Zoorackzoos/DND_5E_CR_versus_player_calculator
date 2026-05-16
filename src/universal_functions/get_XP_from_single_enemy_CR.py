def get_XP_from_single_enemy_CR(CR, tab_amount):
    print(tab_amount,"get_XP_from_single_enemy_CR")
    tab_amount += "\t"

    print(tab_amount,"CR =",CR)

    if CR < 0:
        print(tab_amount,CR,"--> 10")
        return 10
    if CR < 0.125:
        print(tab_amount, CR, "--> 25")
        return 25
    if CR < 0.25:
        print(tab_amount, CR, "--> 50")
        return 50
    if CR < 0.5:
        print(tab_amount, CR, "--> 100")
        return 100
    if CR < 1:
        print(tab_amount, CR, "--> 200")
        return 200
    if CR < 2:
        print(tab_amount, CR, "--> 450")
        return 450
    if CR < 3:
        print(tab_amount, CR, "--> 700")
        return 700
    if CR < 4:
        print(tab_amount, CR, "--> 1100")
        return 1100
    if CR < 5:
        print(tab_amount, CR, "--> 1800")
        return 1800
    if CR < 6:
        print(tab_amount, CR, "--> 2300")
        return 2300
    if CR < 10:
        print(tab_amount, CR, "--> 5900")
        return 5900
    if CR < 20:
        print(tab_amount, CR, "--> 25000")
        return 25000
    if CR < 30:
        print(tab_amount, CR, "--> 155000")
        return 155000
    else:
        return 0