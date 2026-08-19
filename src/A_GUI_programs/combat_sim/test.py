import keyboard

while True:
    key = keyboard.read_key()

    if key == "up":
       print("Moving up!")

    elif key == "down":
       print("Moving down!")

    elif key == "left":
       print("Moving left!")

    elif key == "right":
       print("Moving right!")
