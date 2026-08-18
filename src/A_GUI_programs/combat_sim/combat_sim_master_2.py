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
import curses

from A_GUI_programs.universal_terminal_clear import universal_terminal_clear
from get_damage_and_get_chance_to_hit import get_damage, get_chance_to_hit


def ask_to_run_combat_sim_master():
    print("You've ran \"combat_sim_master.py\" . Would you like to continue? (y/n)")
    userInput = input()
    while userInput not in ("y", "n"):
        print("Invalid input. Must be 'y' or 'n'")
        userInput = input()

    if userInput == "y":
        print("running program...")
        time.sleep(1)  # just give me some breathing thinking room
    else:
        print("exiting program.")
        exit(0)


# ---------------------------------------------------------------------------
# take_initiative_roles and its curses helpers
# ---------------------------------------------------------------------------

FIELDS = ["Mikey", "Forest", "Thalis", "Micheal", "Evil", "Good"]
OPTIONAL_FIELDS = {"Good"}  # allowed to be left blank -> None


def _draw_form(stdscr, values, cursor_row, error_msg=""):
    stdscr.clear()
    stdscr.addstr(0, 0, "take_initiative_roles")
    stdscr.addstr(1, 4, "Use UP/DOWN to move between fields.")
    stdscr.addstr(2, 4, "Type digits, BACKSPACE to edit.")
    stdscr.addstr(3, 4, "Press ENTER or RIGHT ARROW to continue.")

    for i, name in enumerate(FIELDS):
        row = 5 + i
        prefix = f"{name}: "
        stdscr.addstr(row, 4, prefix)
        val = values[name]
        if i == cursor_row:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(row, 4 + len(prefix), val if val else " ")
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(row, 4 + len(prefix), val)

    if error_msg:
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(5 + len(FIELDS) + 1, 4, error_msg)
        stdscr.attroff(curses.A_BOLD)

    stdscr.move(5 + cursor_row, 4 + len(FIELDS[cursor_row]) + 2 + len(values[FIELDS[cursor_row]]))
    stdscr.refresh()


def _validate(values):
    for name in FIELDS:
        raw = values[name].strip()
        if name in OPTIONAL_FIELDS and raw == "":
            continue
        if raw == "":
            return f"{name} cannot be blank."
        if not raw.lstrip("-").isdigit():
            return f"{name} must be a whole number, got '{raw}'."
    return None


def _initiative_form(stdscr):
    curses.curs_set(1)
    values = {name: "" for name in FIELDS}
    cursor_row = 0
    error_msg = ""

    while True:
        _draw_form(stdscr, values, cursor_row, error_msg)
        key = stdscr.getch()

        if key == curses.KEY_UP:
            cursor_row = (cursor_row - 1) % len(FIELDS)
            error_msg = ""
        elif key == curses.KEY_DOWN:
            cursor_row = (cursor_row + 1) % len(FIELDS)
            error_msg = ""
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            name = FIELDS[cursor_row]
            values[name] = values[name][:-1]
        elif key in (curses.KEY_RIGHT, curses.KEY_ENTER, 10, 13):
            err = _validate(values)
            if err:
                error_msg = err
                continue
            return {
                name: (int(values[name]) if values[name].strip() != "" else None)
                for name in FIELDS
            }
        elif 48 <= key <= 57 or (key == ord('-') and values[FIELDS[cursor_row]] == ""):
            name = FIELDS[cursor_row]
            values[name] += chr(key)


def _roll_off(stdscr, tied_names):
    rolls = {}
    for name in tied_names:
        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, f"Tie roll-off: enter {name}'s roll: ")
        stdscr.refresh()
        curses.curs_set(1)
        raw = stdscr.getstr(1, 0, 10).decode("utf-8").strip()
        curses.noecho()
        while not raw.lstrip("-").isdigit():
            stdscr.addstr(2, 0, "Invalid number, try again: ")
            raw = stdscr.getstr(3, 0, 10).decode("utf-8").strip()
        rolls[name] = int(raw)

    ordered = sorted(tied_names, key=lambda n: rolls[n], reverse=True)
    result = {name: "" for name in tied_names}
    top_val = rolls[ordered[0]]
    bottom_val = rolls[ordered[-1]]

    top_group = [n for n in tied_names if rolls[n] == top_val]
    bottom_group = [n for n in tied_names if rolls[n] == bottom_val]

    if len(top_group) > 1:
        result.update(_roll_off(stdscr, top_group))
    else:
        result[top_group[0]] = "++"

    if top_val != bottom_val:
        if len(bottom_group) > 1:
            result.update(_roll_off(stdscr, bottom_group))
        else:
            result[bottom_group[0]] = "--"

    return result


def take_initiative_roles():
    raw_values = curses.wrapper(_initiative_form)

    player_names = ["Mikey", "Forest", "Thalis", "Micheal"]
    by_value = {}
    for name in player_names:
        by_value.setdefault(raw_values[name], []).append(name)

    ties_to_resolve = [names for names in by_value.values() if len(names) > 1]

    final = dict(raw_values)
    if ties_to_resolve:
        def _run_roll_offs(stdscr):
            suffixes = {}
            for tied_group in ties_to_resolve:
                suffixes.update(_roll_off(stdscr, tied_group))
            return suffixes

        suffixes = curses.wrapper(_run_roll_offs)
        for name, suffix in suffixes.items():
            if suffix:
                final[name] = f"{final[name]}{suffix}"

    return final


if __name__ == "__main__":
    tab_amount = ""
    universal_terminal_clear(tab_amount=tab_amount)
    ask_to_run_combat_sim_master()
    result = take_initiative_roles()
    print(result)