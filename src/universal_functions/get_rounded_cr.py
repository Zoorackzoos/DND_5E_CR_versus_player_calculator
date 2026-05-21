def get_rounded_cr(cr,tab_amount="\t"):
    print(tab_amount,"get_rounded_cr")
    tab_amount += "\t"

    if cr < 0:
        print("ERROR: get_rounded_cr: you have a negative cr. wtf bro")
        exit(1)
    elif cr == 0:
        return 0
    elif cr <= 0.125:
        return 0.125
    elif cr <= 0.25:
        return 0.25
    elif cr <= 0.5:
        return 0.5
    elif cr <= 1:
        return 1
    elif cr <= 2:
        return 2
    elif cr <= 3:
        return 3
    elif cr <= 4:
        return 4
    elif cr <= 5:
        return 5
    elif cr <= 6:
        return 6
    elif cr <= 7:
        return 7
    elif cr <= 8:
        return 8
    elif cr <= 9:
        return 9
    elif cr <= 10:
        return 10
    elif cr <= 11:
        return 11
    elif cr <= 12:
        return 12
    elif cr <= 13:
        return 13
    elif cr <= 14:
        return 14
    elif cr <= 15:
        return 15
    elif cr <= 16:
        return 16
    elif cr <= 17:
        return 17
    elif cr <= 18:
        return 18
    elif cr <= 19:
        return 19
    elif cr <= 20:
        return 20
    elif cr <= 21:
        return 21
    elif cr <= 22:
        return 22
    elif cr <= 23:
        return 23
    elif cr <= 24:
        return 24
    elif cr <= 25:
        return 25
    elif cr <= 26:
        return 26
    elif cr <= 27:
        return 27
    elif cr <= 28:
        return 28
    elif cr <= 29:
        return 29
    elif cr > 30:
        return 30
    else:
        print(tab_amount,"ERROR: really weird cr",cr)
        exit(1)
