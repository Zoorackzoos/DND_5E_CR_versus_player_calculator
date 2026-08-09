import os
import subprocess


def universal_terminal_clear(tab_amount=""):
    """
    detect the OS so we can clear the terminal.
    subprocess is a bastard and requires shell.
    """
    if os.name == 'nt':
        #print("Windows-based system")
        #os.system("cls")
        subprocess.run("cls", shell=True)
    else: #elif os.name == 'posix' :
        #print("Unix-based system (Linux, macOS, etc.)")
        #os.system("clear")
        subprocess.run("clear", shell=True)