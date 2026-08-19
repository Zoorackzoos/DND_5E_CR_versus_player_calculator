import time
from copy import deepcopy

from universal_functions.display.print_2d_list import print_2d_list


def get_sorted_initiative_rolls_from_greatest_to_least(unsorted_initiative_rolls_list):
    sorted_initiative_rolls_list = deepcopy(unsorted_initiative_rolls_list)

    sorted_initiative_rolls_length = len(sorted_initiative_rolls_list)

    for i in range(sorted_initiative_rolls_length):
        for j in range(sorted_initiative_rolls_length):

            # if a initiative roll is none, then just remove it because we can't use it.
            if sorted_initiative_rolls_list[i][1] is None:
                sorted_initiative_rolls_list.pop(i)
                sorted_initiative_rolls_length -= 1
                return get_sorted_initiative_rolls_from_greatest_to_least(sorted_initiative_rolls_list)
            if sorted_initiative_rolls_list[j][1] is None:
                sorted_initiative_rolls_list.pop(j)
                sorted_initiative_rolls_length -= 1
                return get_sorted_initiative_rolls_from_greatest_to_least(sorted_initiative_rolls_list)

            """
            print(sorted_initiative_rolls_list)
            print(sorted_initiative_rolls_length)
            print("\t", sorted_initiative_rolls_list[i][1])
            print("\t", sorted_initiative_rolls_list[j][1])
            """
            if sorted_initiative_rolls_list[i][1] > sorted_initiative_rolls_list[j][1]:
                # this is moving them. might want to re-do this later.
                temp_list_one = sorted_initiative_rolls_list[i]
                temp_list_two = sorted_initiative_rolls_list[j]
                sorted_initiative_rolls_list[i] = temp_list_two
                sorted_initiative_rolls_list[j] = temp_list_one

    print("get_sorted_initiative_rolls_from_greatest_to_least")
    print("\tsorted them. look at it!")
    print_2d_list(list_in_question=sorted_initiative_rolls_list,tab_amount="\t\t")
    time.sleep(1) #this "hey i did it :DDD" text will be pasted over by another function anyway.

    return sorted_initiative_rolls_list

def update_combat_sim_cycle_combat_interface():
    """

    ##GUI statement
    make it look like this
    ```
    update_combat_sim_cycle_combat_interface
        you are in combat now.
        the '→' character indicates which PC / NPC 's you've selected.
        the '!" character indicates which PC / NPC 's turn it is to play.
        Use the UP and DOWN arrow key to go between PCs or NPCs.
        Use the RIGHT arrow on a NPC to go to a menu
        from there you can either:
            * make them do an attack. Either hit something or a make someone else do a saving throw.
            * make them take damage which an integer you input.
            * make them heal with an integer you input.
        Use the 'T" button to cycle through turns once the selected one has ended. (T for turn)

        !→ Evil: 5
            name : hp
            goblin : 10
            skeleton : 15
            Dragon, Chromatic, Black, Young : 130
          Micheal: 4
          Thalis: 3
          Forest: 2
          Mikey: 1
    ```

    :return:
    """

def combat_sim_cycle_combat(initiative_rolls_dictionary):
    if initiative_rolls_dictionary == None:
        exit("ERR: combat_sim_cycle_combat: initative_roles_dict is None.")

    #sort initiative roles based from first to last. 20 means first 1 means last.
    #   to do this i'm going to have the structure that contains this to be a list
    #   that contains lists with the 1st value in teh sub-list be the PC / NPC's
    #   name and the 2nd will be their role
    #       think about making it a list that stories tiny dictionaries instead.
    unsorted_initiative_rolls_list = []

    #add the roles to the rolls list
    for name,initiative_roll in initiative_rolls_dictionary.items():
        name_and_roll_list = [name, initiative_roll]
        unsorted_initiative_rolls_list.append(name_and_roll_list)

    sorted_initiative_rolls = get_sorted_initiative_rolls_from_greatest_to_least(
        unsorted_initiative_rolls_list=unsorted_initiative_rolls_list
    )

    selected_initiative_roll = sorted_initiative_rolls[0]

