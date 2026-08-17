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
            time.sleep(1) #just give me some breathing thinking room
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
    :return:
    """
    universal_terminal_clear(tab_amount=tab_amount)
    print("take_initiative_roles")
    print("\tWe need to take intative roles")
    print("\tuse the up and down arrow keys to swap from input to input")
    print("\tpress enter or the right arrow key on the keyboard to continue through the combat sim")
    input("\t\tMikey: ")
    print("\t\tForest: ")
    print("\t\tThalis: ")
    print("\t\tMicheal: ")
    print("\t\tEvil: ")
    print("\t\tGood: ") #this is allowed to be None


if __name__ == "__main__":
    tab_amount=""
    universal_terminal_clear(tab_amount=tab_amount)
    ask_to_run_combat_sim_master()
    take_initiative_roles()