import unittest


def get_damage_per_round(dice_dict, tab_amount="\t"):
    """
    2d6
    7.0

    2d4 + 1d8
    9.5

    5d4 + 2
    29

    store like dictionary
    damage_dice_var = {
        6 : 2
        "constant" : 2
    }

    previous:
        total = 0
        matches = re.findall(r"(\\d+)d(\\d+)", dice_string)
        for dice_count, dice_sides in matches:
            dice_count = int(dice_count)
            dice_sides = int(dice_sides)
            average_die = (dice_sides + 1) / 2
            total += dice_count * average_die

    """
    print(tab_amount,"get_damage_per_round")
    tab_amount += "\t"

    total = 0

    for key,value in dice_dict.items():
        if key == "constant":
            total += value
        else:
            print(tab_amount+"\t",key,":",value)
            average_die = (key + 1) / 2
            print(tab_amount+"\t\t","average_die =",average_die)
            total += value * average_die
            print(tab_amount+"\t\t","total =",total)

    print(tab_amount+"\t","total =",total)
    return total

class Test_get_damage_per_round(unittest.TestCase):

    def test_two_six_dice(self):
        dice_dict = {6: 2}
        self.assertEqual(
            get_damage_per_round(dice_dict),
            7.0
        )

    def test_two_d4_one_d8(self):
        dice_dict = {
            4: 2,
            8: 1
        }

        self.assertEqual(
            get_damage_per_round(dice_dict),
            9.5
        )

    def test_constant_damage(self):
        dice_dict = {
            4: 5,
            "constant": 2
        }

        self.assertEqual(
            get_damage_per_round(dice_dict),
            14.5
        )


