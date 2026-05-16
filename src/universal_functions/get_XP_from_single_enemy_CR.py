def get_XP_from_single_enemy_CR(CR, tab_amount):
    print(tab_amount,"get_XP_from_single_enemy_CR")
    tab_amount += "\t"

    print(tab_amount,"CR = ",CR)

    match CR:
        case 0:
            print(tab_amount,CR,"--> 10")
            return 10
        case 0.125:
            print(tab_amount, CR, "--> 0.125")
            return 25
        case 0.25:
            print(tab_amount, CR, "--> 0.25")
            return 50
        case 0.5:
            print(tab_amount, CR, "--> 100")
            return 100
        case 1:
            print(tab_amount, CR, "--> 200")
            return 200
        case 2:
            print(tab_amount, CR, "--> 450")
            return 450
        case 3:
            print(tab_amount, CR, "--> 700")
            return 700
        case 4:
            print(tab_amount, CR, "--> 1100")
            return 1100
        case 5:
            print(tab_amount, CR, "--> 1800")
            return 1800
        case 6:
            print(tab_amount, CR, "--> 2300")
            return 2300
        case 10:
            print(tab_amount, CR, "--> 5900")
            return 5900
        case 20:
            print(tab_amount, CR, "--> 25000")
            return 25000
        case 30:
            print(tab_amount, CR, "--> 155000")
            return 155000
        case _:
            return 0