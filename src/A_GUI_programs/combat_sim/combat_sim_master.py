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

from A_GUI_programs.combat_sim.take_initiative_rolls import take_initiative_roles
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



if __name__ == "__main__":
    tab_amount=""
    universal_terminal_clear(tab_amount=tab_amount)
    ask_to_run_combat_sim_master()