import random

staff_of_the_spire_lvl_0_cr_options = \
[
    0,
    0.125,
    0.25,
    0.5,
    1
]

staff_of_the_spire_lvl_1_cr_options = \
[
    1,
    2,
    3,
    4
]

staff_of_the_spire_options_master = \
[
    staff_of_the_spire_lvl_0_cr_options,
    staff_of_the_spire_lvl_1_cr_options,
]

def get_random_cr_from_list(lvl_integer=0, tab_amount="\t"):
    print(tab_amount,"get_random_cr_from_list")
    tab_amount += "\t"
    chosen_cr = random.choice(staff_of_the_spire_options_master[lvl_integer])
    print(tab_amount,"chosen_cr = ",chosen_cr)
    return chosen_cr

if __name__ == "__main__":
    tab_amount = "\t"
    lvl_integer = 0
    get_random_cr_from_list(lvl_integer=lvl_integer, tab_amount=tab_amount)