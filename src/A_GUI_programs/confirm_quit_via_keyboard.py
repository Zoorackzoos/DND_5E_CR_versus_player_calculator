import keyboard


def confirm_quit_via_keyboard():
    """
    Blocks and listens for y/n using the keyboard module directly,
    instead of input() -- avoids the stdin-buffer collision that happens
    when input() is called from inside a keyboard.read_event() loop.

    claude made this.
    i probably could have as well but i asked it a question about why input
    doesn't work with the keyboard.read_event() thing we have.
    and it spat out this so i'm using it.
    """
    print("you're about to quit? are you sure? (y/n)")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "y":
                return True
            elif event.name == "n":
                return False
            # anything else: keep waiting, don't fall through