import time
from copy import deepcopy

import keyboard

from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from universal_functions.display.print_2d_list import print_2d_list
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_dict_from_csv_file import \
    get_dict_from_csv_file
from universal_functions.spreadsheet_stuff.dict_based_database_interpretors.get_rows_from_dict_on_param_type_and_string import \
    get_rows_from_dict_on_param_type_and_string
from universal_functions.vars.spreadsheet_enums import SpreadsheetKeysEnums


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

def detect_if_NPC_and_display_monster_if_yes(
        sub_list,
        list_that_contains_dictionaries_that_are_monsters
):
    """
    used to be called "detect_if_evil_and_display_monster_if_yes"
    but need refactor for friendly NPCs. so just NPC.

    :param sub_list:
        is a lost of 2 elements. name, and a int. the int is the initiative roll.
    :param list_that_contains_dictionaries_that_are_monsters:
        this is a list of dictionaries that are monsters. monster information
    :param monster_selection_index:
        if this is -1, then it's False, for no monster is selected.
         if it's any other integer, then a monster is selected.
    :return:
    """
    if (sub_list[0].lower() == "evil" or sub_list[0].lower() == "good"):
        print("\t\t", "name : hp : ac")
        for monster_dict in list_that_contains_dictionaries_that_are_monsters:
            print("\t\t", monster_dict["Name"], ":", monster_dict["HP"], ":", monster_dict["AC"])

def update_combat_sim_cycle_combat_interface(
        sorted_initiative_rolls_list,
        user_selected_initiative_roll,
        system_selected_initiative_roll,
        list_that_contains_dictionaries_that_are_monsters,
        selected_npc_bool,
):
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
        Use the "T" button to cycle through turns once the selected one has ended. (T for turn)

        !→ Evil: 5
            name : hp : ac
            goblin : 10 : 15
            skeleton : 15 : 13
            Dragon, Chromatic, Black, Young : 130 : 18
          Micheal: 4
          Thalis: 3
          Forest: 2
          Mikey: 1
    ```
    :return:
    """
    universal_terminal_clear()

    update_combat_sim_cycle_combat_interface_start = """update_combat_sim_cycle_combat_interface
    you are in combat now.
    the '→' character indicates which PC / NPC 's you've selected.
    the '!" character indicates which PC / NPC 's turn it is to play.
    Use the UP and DOWN arrow key to go between PCs or NPCs.
    Use the RIGHT arrow on a parent NPC label to choose which NPC to interact with.
    from there, use the RIGHT arrow on a NPC to go to a menu. 
    from there you can either:
        * make them do an attack. Either hit something or a make someone else do a saving throw.
        * make them take damage which an integer you input.
        * make them heal with an integer you input.
    Use the "T" button to cycle through turns once the selected one has ended. (T for turn)
"""
    print(update_combat_sim_cycle_combat_interface_start)

    #printing the NPCs and PCs
    for sub_list in sorted_initiative_rolls_list:
        #i'm comparing the names because list versus list can be fucky.
        # is both a system and user selected initiative roll
        #  sub_list[0] name    #sub_list[0] name
        if (sub_list[0] == user_selected_initiative_roll[0]
                and
            sub_list[0] == system_selected_initiative_roll[0]):
          print("\t!→",sub_list[0],":",sub_list[1])
          detect_if_NPC_and_display_monster_if_yes(
              sub_list=sub_list,
              list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters
          )
        # is a system selected initiative roll
        elif sub_list[0] == system_selected_initiative_roll[0]:
            print("\t! ", sub_list[0], ":", sub_list[1])
            detect_if_NPC_and_display_monster_if_yes(
                sub_list=sub_list,
                list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters
            )
        # is a user selected initiative roll
        elif sub_list[0] == user_selected_initiative_roll[0]:
            print("\t →", sub_list[0], ":", sub_list[1])
            detect_if_NPC_and_display_monster_if_yes(
                sub_list=sub_list,
                list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters
            )
        else:
            print("\t  ", sub_list[0], ":", sub_list[1])
            detect_if_NPC_and_display_monster_if_yes(
                sub_list=sub_list,
                list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters
            )

def combat_sim_cycle_combat(
        initiative_rolls_dictionary,
):
    if initiative_rolls_dictionary is None:
        exit("ERROR: combat_sim_cycle_combat: initative_roles_dict is None.")

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

    sorted_initiative_rolls_list = get_sorted_initiative_rolls_from_greatest_to_least(
        unsorted_initiative_rolls_list=unsorted_initiative_rolls_list
    )

    universal_terminal_clear()

    #fetching the large ahh dictionary
    combat_sim_cycle_combat_path_to_monsters_csv_file = \
        "../../../sheets/monsters_all_stats_homebrew/monsters_all_stats_homebrew.csv"
    monsters_all_stats_homebrew_dict = get_dict_from_csv_file(path_to_csv_file=combat_sim_cycle_combat_path_to_monsters_csv_file)

    """
    #TDOD: make these monsters dynamic 
    a goblin
    a skeleton
    a "Dragon, Chromatic, Black, Young"
    """
    goblin_list_that_contains_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="goblin",
        tab_amount=""
    )
    skeleton_list_that_contains_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="skeleton",
        tab_amount=""
    )
    chromatic_blank_young_dragon_list_that_contains_dict = get_rows_from_dict_on_param_type_and_string(
        dict_in_question=monsters_all_stats_homebrew_dict,
        param_type=SpreadsheetKeysEnums.NAME.value,
        string="Dragon, Chromatic, Black, Young",
        tab_amount=""
    )

    #you'd figure i would be taught how to name variables by now but no.
    #"fuck them kids" -every university on earth.
    list_that_contains_dictionaries_that_are_monsters = \
    [
        goblin_list_that_contains_dict[0],
        skeleton_list_that_contains_dict[0],
        chromatic_blank_young_dragon_list_that_contains_dict[0]
    ]

    """
    originally i had it as "sorted_initiative_rolls_list[0]" which stored those
    sub lists. 
       another situation where it makes more sense to have this be made in java. 
           oh well :-/ 
    """
    user_initiative_roll_index = 0
    system_initiative_roll_index = 0

    #if you selected a NPC. not a player. this includes it a evil or a godo NPC mind you.
    selected_npc_bool = False

    """
    there's probably a less shit way to do this in order to save lines but considering the 
    variables involved update so frequently within this scope. IDK. 
        if only chris born was here to mock me wand program a function 
    i completely fail to understand.
    """
    def default_input_update_combat_sim_cycle_combat_interface():
        update_combat_sim_cycle_combat_interface(
            sorted_initiative_rolls_list=sorted_initiative_rolls_list,
            user_selected_initiative_roll=sorted_initiative_rolls_list[user_initiative_roll_index],
            system_selected_initiative_roll=sorted_initiative_rolls_list[system_initiative_roll_index],
            list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters,
            selected_npc_bool=selected_npc_bool
        )

    # do this once with the starter indexes.
    default_input_update_combat_sim_cycle_combat_interface()

    combat_cycle_keep_program_running_bool = True

    while combat_cycle_keep_program_running_bool:
        #these 2 lines are so duplicate inputs aren't recorded / holding down the key does nothing
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if keyboard.is_pressed("up"):
                if user_initiative_roll_index > 0:
                    user_initiative_roll_index += -1
                    default_input_update_combat_sim_cycle_combat_interface()
                else:
                    #do nothing
                    pass
            elif keyboard.is_pressed("down"):
                if user_initiative_roll_index < len(sorted_initiative_rolls_list)-1:
                    user_initiative_roll_index += 1
                    default_input_update_combat_sim_cycle_combat_interface()
                else:
                    # do nothing
                    pass
            elif keyboard.is_pressed("right"):
                name_of_selected_npc_or_pc = sorted_initiative_rolls_list[user_initiative_roll_index][0].lower()
                if name_of_selected_npc_or_pc == "evil" or name_of_selected_npc_or_pc == "good":
                    selected_npc_bool = True
                else:
                    #TODO: make update GUI function say "no interactions with PCs implemented yet"
                    pass
                update_combat_sim_cycle_combat_interface(
                    sorted_initiative_rolls_list=sorted_initiative_rolls_list,
                    user_selected_initiative_roll=sorted_initiative_rolls_list[user_initiative_roll_index],
                    system_selected_initiative_roll=sorted_initiative_rolls_list[system_initiative_roll_index],
                    list_that_contains_dictionaries_that_are_monsters=list_that_contains_dictionaries_that_are_monsters,
                    selected_npc_bool=selected_npc_bool
                )