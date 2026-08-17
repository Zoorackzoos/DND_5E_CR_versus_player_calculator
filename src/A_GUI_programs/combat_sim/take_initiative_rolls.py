import curses

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
        # character's name label is never editable - just draw it fresh every time
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
        # reject "poor integer syntax": allow optional leading -, digits only after that
        if not (raw.lstrip("-").isdigit()):
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
            # digits, and a leading '-' for negative rolls if you ever need it
            name = FIELDS[cursor_row]
            values[name] += chr(key)
        # any other key (letters etc.) is silently ignored -> "asks again" is
        # enforced at validation time instead of blocking keystrokes


def _roll_off(stdscr, tied_names):
    """
    Given a list of >=2 names tied on the same initiative value, prompt a
    single-number roll-off input for each, then recursively resolve.
    Returns dict name -> "++" or "--" (or "" if not part of a decisive pair).
    """
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

    # highest roll gets "++", lowest gets "--"; if the roll-off itself ties,
    # recurse on just that subgroup until it breaks
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
    """
    Runs a curses-based form for entering DnD 5e initiative rolls, resolves
    ties among the named player characters with a roll-off, and returns
    the finished initiative_roles_dictionary.
    """
    raw_values = curses.wrapper(_initiative_form)

    # tie resolution only applies to the four named players, not Evil/Good
    player_names = ["Mikey", "Forest", "Thalis", "Micheal"]
    by_value = {}
    for name in player_names:
        by_value.setdefault(raw_values[name], []).append(name)

    ties_to_resolve = [names for names in by_value.values() if len(names) > 1]

    final = dict(raw_values)  # start with ints/None
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
    result = take_initiative_roles()
    print(result)