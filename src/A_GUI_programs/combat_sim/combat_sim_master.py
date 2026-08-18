"""
the goal of this file is to:
1. calculate intative and use a step system to tell you who's intative it is
2. take in damage against monsters and tell if they're dead or not. hp stored as a variable
3. take in healing against monsters and tell they're new hp value. hp stored as a variable
4. have monster dictionaries stored in a array.
    a. instead of crafting markdown files that contain the stat block for every new monster
       so this program is normalized...
       instead i will put in values to the spreadsheet from the "update_homebrew_monster.py"
       keys.
    b. from there i can craft temp dictionaries and put the min the array. or something similar.
    c. the monster list will be modified in the source code, not via the GUI.
5. smooth GUi interface. interaction instructions top,
   get_damage_and_chance_to_hit.py stuff middle, verbose bullshit below that.
"""
import time
import keyboard
from asyncio.windows_events import NULL
from sympy.parsing.sympy_parser import null

from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from get_damage_and_get_chance_to_hit import get_damage, get_chance_to_hit

def ask_to_run_combat_sim_master():
    print("You've ran \"combat_sim_master.py\" . Would you like to continue? (y/n)")
    userInput = input()
    while userInput != ["y", "n"]:
        if userInput == "y":
            print("running program...")
            time.sleep(0.5) #just give me some breathing thinking room
            break
        elif userInput == "n":
            print("exiting program.")
            exit(0)
        else:
            print("Invalid input. Must be 'y' or 'n'")

initiative_roles_dictionary = \
{
    "Mikey" : None,
    "Forest" : None,
    "Thalis" : None,
    "Micheal" : None,
    "Evil" : None, #these are the monsters, AKA the bad guys.
    "Good" : None #these are DM controlled allies. They're not always there so this can be Null.
}

def update_initiative_roles_screen_and_return_user_input(
    selected_roll_taker_index=0,
    failed_input_bool=False,
    user_input = None,
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

    first_initiative_detector_bool = True
    for key in initiative_roles_dictionary:
        if first_initiative_detector_bool:
            print("\t→ ", key, ": ")
            first_initiative_detector_bool = False
        else:
            print("\t  ", key, ": ")

    print()
    if failed_input_bool:
        #if our good input detection system was better we could tell the user what they did wrong
        #however, i have a bastard good detection system. so i can't.
        print("\tyou entered: \""+user_input+"\" which is not in the \"acceptable_user_input_list\" list.")

    selected_roll_taker_indicator_text = str("\t→  " + str(list(initiative_roles_dictionary.keys())[selected_roll_taker_index]) + " : ")
    roll_for_selected_roll_taker = input(selected_roll_taker_indicator_text)

    return roll_for_selected_roll_taker

def get_acceptable_user_input_list():
    acceptable_user_input_list = []

    #"The absolute highest initiative roll you can mathematically achieve in D&D 5e is 111."
    #if you manage to get a number greater than 40 i'll eat my fingers
    largest_initiative_roll = 41

    for i in range(largest_initiative_roll):
        if i == 0:
            #do nothing lol
            pass
        else:
            acceptable_user_input_list.insert(0,str(i) + "--")
            acceptable_user_input_list.insert(0,str(i))
            acceptable_user_input_list.insert(0,str(i) + "++")

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

def get_if_user_input_is_failed_input(user_input):
    """
    this is kinda fucky because we need to allow things like "10--" and "10++"
    so we can't just say if it's a integer let it pass.
    so the bastard thing i'm gonna do is make a list of acceptable answers.
    and if our user_input is not in the array, throw a hissy fit.

    :param user_input:
    :return:
    """
    acceptable_user_input_list = get_acceptable_user_input_list()
    if user_input in acceptable_user_input_list:
        return False
    else:
        return True

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

        → Mikey: *cursor is here*
    ```
    :return:
    """
    selected_roll_taker_index = 0
    user_input = update_initiative_roles_screen_and_return_user_input(selected_roll_taker_index=selected_roll_taker_index)

    #if failed_input was wrong, it's true. because it was a failed input
    failed_input_bool = get_if_user_input_is_failed_input(user_input=user_input)

    while failed_input_bool:
        #this is just gonna keep going until failed_input_bool is false
        user_input = update_initiative_roles_screen_and_return_user_input(
                    selected_roll_taker_index=selected_roll_taker_index,
                    failed_input_bool=failed_input_bool,
                    user_input=user_input)
        failed_input_bool = get_if_user_input_is_failed_input(user_input=user_input)


if __name__ == "__main__":
    tab_amount=""
    universal_terminal_clear(tab_amount=tab_amount)
    ask_to_run_combat_sim_master()
    take_initiative_roles()