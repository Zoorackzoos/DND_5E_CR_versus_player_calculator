from copy import deepcopy


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

    #sorting the bloody thing
    sorted_initiative_rolls_list = deepcopy(unsorted_initiative_rolls_list)
    for i in range(len(sorted_initiative_rolls_list)):
        for j in range(len(sorted_initiative_rolls_list[i])):
            if sorted_initiative_rolls_list[i][1] > sorted_initiative_rolls_list[j][1]:
                #this is moving them. might want to re-do this later.
                temp_list_one = sorted_initiative_rolls_list[i]
                temp_list_two = sorted_initiative_rolls_list[j]
                sorted_initiative_rolls_list[i] = temp_list_two
                sorted_initiative_rolls_list[j] = temp_list_one

    print("sorted them. look at it!")
    print(sorted_initiative_rolls_list)