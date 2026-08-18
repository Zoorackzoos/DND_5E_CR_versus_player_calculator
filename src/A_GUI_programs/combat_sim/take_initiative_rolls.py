import msvcrt
import os

FIELDS = ["Mikey", "Forest", "Thalis", "Micheal", "Evil", "Good"]
OPTIONAL_FIELDS = {"Good"}

# arrow keys arrive as two bytes on Windows: b'\xe0' or b'\x00', then a code
ARROW_PREFIXES = (b'\xe0', b'\x00')
ARROW_UP = b'H'
ARROW_DOWN = b'P'
ARROW_RIGHT = b'M'


def _clear():
    os.system("cls")


def _draw_form(values, cursor_row, error_msg=""):
    _clear()
    print("take_initiative_roles")
    print("    Use UP/DOWN to move between fields.")
    print("    Type digits, BACKSPACE to edit.")
    print("    Press ENTER or RIGHT ARROW to continue.\n")

    for i, name in enumerate(FIELDS):
        marker = ">" if i == cursor_row else " "
        print(f"    {marker} {name}: {values[name]}")

    if error_msg:
        print(f"\n    !! {error_msg}")


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


def _initiative_form():
    values = {name: "" for name in FIELDS}
    cursor_row = 0
    error_msg = ""

    while True:
        _draw_form(values, cursor_row, error_msg)
        key = msvcrt.getch()

        if key in ARROW_PREFIXES:
            key2 = msvcrt.getch()
            if key2 == ARROW_UP:
                cursor_row = (cursor_row - 1) % len(FIELDS)
                error_msg = ""
            elif key2 == ARROW_DOWN:
                cursor_row = (cursor_row + 1) % len(FIELDS)
                error_msg = ""
            elif key2 == ARROW_RIGHT:
                err = _validate(values)
                if err:
                    error_msg = err
                else:
                    return {
                        name: (int(values[name]) if values[name].strip() != "" else None)
                        for name in FIELDS
                    }
        elif key in (b'\r', b'\n'):
            err = _validate(values)
            if err:
                error_msg = err
            else:
                return {
                    name: (int(values[name]) if values[name].strip() != "" else None)
                    for name in FIELDS
                }
        elif key == b'\x08':  # backspace
            name = FIELDS[cursor_row]
            values[name] = values[name][:-1]
        elif key in b'0123456789' or (key == b'-' and values[FIELDS[cursor_row]] == ""):
            name = FIELDS[cursor_row]
            values[name] += key.decode("ascii")
        # anything else (letters etc.) is ignored


def _roll_off(tied_names):
    rolls = {}
    for name in tied_names:
        raw = input(f"Tie roll-off: enter {name}'s roll: ").strip()
        while not raw.lstrip("-").isdigit():
            raw = input("Invalid number, try again: ").strip()
        rolls[name] = int(raw)

    ordered = sorted(tied_names, key=lambda n: rolls[n], reverse=True)
    result = {name: "" for name in tied_names}
    top_val = rolls[ordered[0]]
    bottom_val = rolls[ordered[-1]]

    top_group = [n for n in tied_names if rolls[n] == top_val]
    bottom_group = [n for n in tied_names if rolls[n] == bottom_val]

    if len(top_group) > 1:
        result.update(_roll_off(top_group))
    else:
        result[top_group[0]] = "++"

    if top_val != bottom_val:
        if len(bottom_group) > 1:
            result.update(_roll_off(bottom_group))
        else:
            result[bottom_group[0]] = "--"

    return result


def take_initiative_roles():
    raw_values = _initiative_form()

    player_names = ["Mikey", "Forest", "Thalis", "Micheal"]
    by_value = {}
    for name in player_names:
        by_value.setdefault(raw_values[name], []).append(name)

    ties_to_resolve = [names for names in by_value.values() if len(names) > 1]

    final = dict(raw_values)
    for tied_group in ties_to_resolve:
        suffixes = _roll_off(tied_group)
        for name, suffix in suffixes.items():
            if suffix:
                final[name] = f"{final[name]}{suffix}"

    return final


if __name__ == "__main__":
    result = take_initiative_roles()
    print(result)