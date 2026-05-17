def get_xp_from_single_enemy_cr(cr, tab_amount):
    print(tab_amount,"get_xp_from_single_enemy_cr")
    tab_amount += "\t"

    print(tab_amount,"CR =", cr)

    if cr < 0.125:
        print(tab_amount, cr, "--> 0 --> 10")
        return 10
    if cr < 0.25:
        print(tab_amount, cr, "--> 0.125 --> 25")
        return 25
    if cr < 0.5:
        print(tab_amount, cr, "--> 0.25 --> 50")
        return 50
    if cr < 1:
        print(tab_amount, cr, "--> 0.5 --> 100")
        return 100
    if cr < 2:
        print(tab_amount, cr, "--> 1 --> 200")
        return 200
    if cr < 3:
        print(tab_amount, cr, "--> 2 --> 450")
        return 450
    if cr < 4:
        print(tab_amount, cr, "--> 3 --> 700")
        return 700
    if cr < 5:
        print(tab_amount, cr, "--> 4 --> 1100")
        return 1100
    if cr < 6:
        print(tab_amount, cr, "--> 5 --> 1800")
        return 1800
    if cr < 7:
        print(tab_amount, cr, "--> 6 --> 2300")
        return 2300
    if cr < 8:
        print(tab_amount, cr, "--> 7 --> 2900")
        return 2900
    if cr < 9:
        print(tab_amount, cr, "--> 8 --> 3900")
        return 3900
    if cr < 10:
        print(tab_amount, cr, "---> 9 --> 5000")
        return 5000
    if cr < 11:
        print(tab_amount, cr, "---> 10 --> 5900")
        return 5900
    if cr < 12:
        print(tab_amount, cr, "---> 11 --> 7200")
        return 7200
    if cr < 13:
        print(tab_amount, cr, "---> 12 --> 8400")
        return 8400
    if cr < 14:
        print(tab_amount, cr, "---> 13 --> 10000")
        return 10000
    if cr < 15:
        print(tab_amount, cr, "---> 14 --> 11500")
        return 11500
    if cr < 16:
        print(tab_amount, cr, "---> 15 --> 13000")
        return 13000
    if cr < 17:
        print(tab_amount, cr, "---> 16 --> 15000")
        return 15000
    if cr < 18:
        print(tab_amount, cr, "---> 17 --> 18000")
        return 18000
    if cr < 19:
        print(tab_amount, cr, "---> 18 --> 20000")
        return 20000
    if cr < 20:
        print(tab_amount, cr, "--> 19 --> 22000")
        return 22000
    if cr < 21:
        print(tab_amount, cr, "---> 20 --> 25000")
        return 25000
    if cr >= 30:
        print(tab_amount, cr, "--> 30 --> 155000")
        return 155000
    else:
        return 0