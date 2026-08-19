import keyboard
from sympy import true

from A_GUI_programs.universal_terminal_clear import universal_terminal_clear

initiative_rolls_dictionary = \
    {
        "Mikey": None,
        "Forest": None,
        "Thalis": None,
        "Micheal": None,
        "Evil": None,  # these are the monsters, AKA the bad guys.
        "Good": None  # these are DM controlled allies. They're not always there so this can be Null.
    }

def get_if_all_rolls_in_initiative_rolls_are_all_none(initative_rolls_dictionary=initiative_rolls_dictionary):
    for i in list(initative_rolls_dictionary.values()):
        if i != None:
            return False
    return True

def get_acceptable_initiative_roll_list():
    acceptable_user_input_list = []

    # "The absolute highest initiative roll you can mathematically achieve in D&D 5e is 111."
    # if you manage to get a number greater than 40 i'll eat my fingers
    largest_initiative_roll = 41

    for i in range(largest_initiative_roll):
        if i == 0:
            # do nothing lol
            pass
        else:
            acceptable_user_input_list.insert(0, str(i) + "--")
            acceptable_user_input_list.insert(0, str(i))
            acceptable_user_input_list.insert(0, str(i) + "++")

    """
    what is looks like:

    ['40++', '40', '40--', 
    '39++', '39', '39--', 
    '38++', '38', '38--', 
    '37++', '37', '37--', 
    '36++', '36', '36--',
    '35++', '35', '35--',
    '34++', '34', '34--',
    '33++', '33', '33--',
    '32++', '32', '32--',
    '31++', '31', '31--', 
    '30++', '30', '30--', 
    '29++', '29', '29--', 
    '28++', '28', '28--', '27++', '27', '27--', '26++', '26', '26--', '25++', '25', '25--', '24++', '24', '24--', '23++', '23', '23--', '22++', '22', '22--', '21++', '21', '21--', '20++', '20', '20--', '19++', '19', '19--', '18++', '18', '18--', '17++', '17', '17--', '16++', '16', '16--', '15++', '15', '15--', '14++', '14', '14--', '13++', '13', '13--', '12++', '12', '12--', '11++', '11', '11--', '10++', '10', '10--', '9++', '9', '9--', '8++', '8', '8--', '7++', '7', '7--', '6++', '6', '6--', '5++', '5', '5--', '4++', '4', '4--', '3++', '3', '3--', '2++', '2', '2--', '1++', '1', '1--']
    """

    return acceptable_user_input_list


def get_if_initiative_input_is_failed_input(user_input):
    """
    this is kinda fucky because we need to allow things like "10--" and "10++"
    so we can't just say if it's a integer let it pass.
    so the bastard thing i'm gonna do is make a list of acceptable answers.
    and if our user_input is not in the array, throw a hissy fit.

    :param user_input:
    :return:
    """
    acceptable_user_input_list = get_acceptable_initiative_roll_list()
    if user_input in acceptable_user_input_list:
        return False
    else:
        return True

def get_if_selected_roll_taker_index_is_beyond_limits(selected_roll_taker_index,modifier):
    least_limit = 0
    greatest_limit = len(initiative_rolls_dictionary)
    modified_selected_roll_taker_index = selected_roll_taker_index + modifier
    return least_limit <= modified_selected_roll_taker_index < greatest_limit

def update_initiative_roles_screen_and_return_user_input(
        selected_roll_taker_index=0,
        failed_input_bool=False,
        user_input=None,
):
    universal_terminal_clear(tab_amount="")

    take_initiative_roles_intro_text = """
take_initiative_roles
    we need to take initiative roles
    use the UP and DOWN arrow keys to swap from input to input
    press ENTER to register a integer in a initiative role
    press the RIGHT ARROW key to continue
        if a player is absent, or there's no good or bad NPCs
        controlled by the DM, leave that parameter blank
"""

    print(take_initiative_roles_intro_text)

    for key,value in initiative_rolls_dictionary.items():
        if key == list(initiative_rolls_dictionary.keys())[selected_roll_taker_index]:
            print("\t →", key, ": ",value)
        else:
            print("\t  ", key, ": ",value)

def take_initiative_roles():
    """
    # this takes in 4 integers.

    ## if players get the same integer
    in situations in which 2 players get the same integer,
    they roll again and whoever gets the bigger number gets higher integrative by a half.
    represented by a ++ or a -- penning on if you won or lost the roll off.

    for example.
        Mikey and Forest both get 10
        they roll off, Mikey gets 12, Forest gets 9
        Mikey is 10++, Forest is 10--

    ## GUI statement
    this is supposed to emulate google docs very minorly.
    * you cannot edit the text where it says the character's names
    * if you enter letters or poor integer syntax the system asks for initiative roles again.
    * "Good" can be None, but "Evil" and the other 4 inputs cannot be None.
    * you can swap from character input to character input freely using the arrow keys
    * press enter on the keyboard or the rightward arrow key to continue through the combat sim

    ## implementation
    * i tried asking claude how to do this and:
        * the library (curses) it initially used was pissy pant and didn't work on pycharm very well.
          how tf people use that library when it's such a pain in the ass when
            windows + pycharm
          idk. and i don't care.
        * it then tried to use somethign else and the code it made was shit
        * so clanking this bitch isn't worked so i have to make somethign more archaic.

    make it look like this:
    ```
    take_initiative_roles
        we need to take initiative roles
        use the UP and DOWN arrow keys to swap from input to input
        press ENTER to register a integer in a initiative role
        press the RIGHT ARROW button to continue
            if a player is absent, or there's no good or bad NPCs
            controlled by the DM, leave that parameter blank

        → Mikey:
          Forest:
          Thalis:
          Micheal:
          Evil:
          Good:
    ```
    :return: modified initiative_roles_dictionary variable that contains initiative roles
    """
    selected_roll_taker_index = 0
    update_initiative_roles_screen_and_return_user_input(
        selected_roll_taker_index=selected_roll_taker_index
    )
    keep_program_running_bool = True

    while keep_program_running_bool:
        #these 2 lines are so duplicate inputs aren't recorded / holding down the key does nothing
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:

            if keyboard.is_pressed("up"):
                modifier = -1
                if get_if_selected_roll_taker_index_is_beyond_limits(selected_roll_taker_index=selected_roll_taker_index,
                                                                     modifier=modifier):
                    selected_roll_taker_index += modifier
                    update_initiative_roles_screen_and_return_user_input(
                        selected_roll_taker_index=selected_roll_taker_index
                    )
                """
                else:
                    print("selected_roll_taker_index :",selected_roll_taker_index)
                    print("modifier :",modifier)
                """
            elif keyboard.is_pressed("down"):
                modifier = 1
                if get_if_selected_roll_taker_index_is_beyond_limits(selected_roll_taker_index=selected_roll_taker_index,
                                                                     modifier=modifier):
                    selected_roll_taker_index += modifier
                    update_initiative_roles_screen_and_return_user_input(
                        selected_roll_taker_index=selected_roll_taker_index
                    )
                """
                else:
                    print("selected_roll_taker_index :", selected_roll_taker_index)
                    print("modifier :", modifier)
                """
            elif keyboard.is_pressed("right"):
                keep_program_running_bool = False

    if get_if_all_rolls_in_initiative_rolls_are_all_none():
        print("all of the values in the intiative_rolls_dictionary is blank. That's bad.")
    return initiative_rolls_dictionary