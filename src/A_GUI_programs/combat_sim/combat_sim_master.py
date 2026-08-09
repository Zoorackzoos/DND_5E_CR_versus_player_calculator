from get_damage_and_get_chance_to_hit import get_damage, get_chance_to_hit
from src.computer_minigames.DMV_door_minigame import universal_terminal_clear

if __name__ == "__main__":
    tab_amount=""
    universal_terminal_clear(tab_amount=tab_amount)
    print("You've ran \"combat_sim_master.py\" . Would you like to continue? (y/n)")
    userInput = input()
    while userInput != ["y", "n"]:
        if userInput == "y":
            print("running program...")
            exit(999)
        elif userInput == "n":
            print("exiting program.")
            exit(0)
        else:
            print("Invalid input. Must be 'y' or 'n'")