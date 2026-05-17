def get_xp_from_single_enemy_cr(CR, tab_amount):
    print(tab_amount,"get_xp_from_single_enemy_cr")
    tab_amount += "\t"

    print(tab_amount,"CR =",CR)

    if CR < 0.125:
        print(tab_amount,CR,"--> 0 --> 10")
        return 10
    if CR < 0.25:
        print(tab_amount, CR, "--> 0.125 --> 25")
        return 25
    if CR < 0.5:
        print(tab_amount, CR, "--> 0.25 --> 50")
        return 50
    if CR < 1:
        print(tab_amount, CR, "--> 0.5 --> 100")
        return 100
    if CR < 2:
        print(tab_amount, CR, "--> 1 --> 200")
        return 200
    if CR < 3:
        print(tab_amount, CR, "--> 2 --> 450")
        return 450
    if CR < 4:
        print(tab_amount, CR, "--> 3 --> 700")
        return 700
    if CR < 5:
        print(tab_amount, CR, "--> 4 --> 1100")
        return 1100
    if CR < 6:
        print(tab_amount, CR, "--> 5 --> 1800")
        return 1800
    if CR < 7:
        print(tab_amount, CR, "--> 6 --> 2300")
        return 2300
    if CR < 8:
        print(tab_amount, CR, "--> 7 --> 2900")
        return 2900
    if CR < 9:
        print(tab_amount, CR, "--> 8 --> 3900")
        return 3900
    if CR < 10:
        print(tab_amount, CR, "---> 9 --> 5000")
        return 5000
    if CR < 11:
        print(tab_amount, CR, "---> 10 --> 5900")
        return 5900
    if CR < 12:
        print(tab_amount, CR, "---> 11 --> 7200")
        return 7200
    if CR < 13:
        print(tab_amount, CR, "---> 12 --> 8400")
        return 8400
    if CR < 14:
        print(tab_amount, CR, "---> 13 --> 10000")
        return 10000
    if CR < 15:
        print(tab_amount, CR, "---> 14 --> 11500")
        return 11500
    if CR < 16:
        print(tab_amount, CR, "---> 15 --> 13000")
        return 13000
    if CR < 17:
        print(tab_amount, CR, "---> 16 --> 15000")
        return 15000
    if CR < 18:
        print(tab_amount, CR, "---> 17 --> 18000")
        return 18000
    if CR < 19:
        print(tab_amount, CR, "---> 18 --> 20000")
        return 20000
    if CR < 20:
        print(tab_amount, CR, "--> 19 --> 22000")
        return 22000
    if CR < 21:
        print(tab_amount, CR, "---> 20 --> 25000")
        return 25000
    if CR >= 30:
        print(tab_amount, CR, "--> 30 --> 155000")
        return 155000
    else:
        return 0