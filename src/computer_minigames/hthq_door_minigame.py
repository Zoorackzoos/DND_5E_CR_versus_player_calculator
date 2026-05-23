import math
import os
import random
import time

from src.universal_functions.display.print_2d_list import print_2d_list
from src.universal_functions.display.print_2d_list_that_contains_dictionaries import print_2d_list_that_contains_dictionaries

BUFFER_TIME_MAX = 2
BUFFER_TIME_MIN = 0.001

"""
================================================
                    display
================================================
"""

def print_2d_list_with_decreasing_buffer\
            (list_in_question,
            buffer_time_max=BUFFER_TIME_MAX,
            buffer_time_min=BUFFER_TIME_MIN,
            tab_amount=""):
    buffer_time_max_editable = buffer_time_max
    buffer_time_min_editable = buffer_time_min

    buffers_are_the_same_or_max = (buffer_time_max_editable == buffer_time_min_editable
                                   or
                                   buffer_time_max_editable < 0)

    i = 1

    for row in list_in_question:
        for element in row:
            if not buffers_are_the_same_or_max:
                i *= i
                buffer_time_max_editable -= buffer_time_min_editable * i
            wait_random_buffer(max=buffer_time_max_editable,min=buffer_time_min_editable,tab_amount=tab_amount)
            print(element, end=" ")
        wait_random_buffer(max=buffer_time_max_editable,min=buffer_time_min_editable,tab_amount=tab_amount)
        print()

def print_2d_list_with_buffer(list_in_question,
                              buffer_time_max=BUFFER_TIME_MAX,
                              buffer_time_min=BUFFER_TIME_MIN,
                              tab_amount=""):
    for row in list_in_question:
        for element in row:
            wait_random_buffer(max=buffer_time_max,min=buffer_time_min,tab_amount=tab_amount)
            print(element, end=" ")
        wait_random_buffer(max=buffer_time_max,min=buffer_time_min,tab_amount=tab_amount)
        print()

"""
=============================================
          random number shananagins
=============================================
"""

def get_random_numbers_array(tab_amount=""):
    """
    1. make a array that semi depends on the terminal
    2. put random numbers in that array
    3. return

    :param tab_amount:
    :return:
    """
    #creating the fucking thing
    terminal_size = 1

    try:
        terminal_size = os.get_terminal_size()
    except OSError:
        # Fallback to a default size if the handle is invalid
        # or if you're in pycharms run lol
        from collections import namedtuple
        TerminalSize = namedtuple('TerminalSize', ['columns', 'lines'])
        terminal_size = TerminalSize(80, 24)

    #terminal_size_rows = terminal_size.lines
    terminal_size_rows = 50 #i want it to go off the page :-/
    terminal_size_columns = terminal_size.columns
    random_numbers_array = \
    [
        [0 for col in range(terminal_size_columns)]
        for row in range(terminal_size_rows)
    ]

    print()

    #not really :-3. just the dimensions
    print("number of top secrets =",terminal_size_rows)
    print("number of enemies to slay =",terminal_size_rows)
    print()

    #fill the array with random integers
    for row in range(terminal_size_rows):
        for col in range(terminal_size_columns):
            random_int = random.randint(0,9)
            random_numbers_array[row][col] = random_int

    print_2d_list_with_decreasing_buffer(list_in_question=random_numbers_array)
    return random_numbers_array

def wait_random_buffer(min=BUFFER_TIME_MIN,
                       max=BUFFER_TIME_MAX,
                       tab_amount=""):
    """
    make the computer wait.
    this makes it seem like it's important

    :param min:
    :param max:
    :param tab_amount:
    :return:
    """
    #this is a random decimal between the min & max values
    random_buffer = random.uniform(min,max)
    print(tab_amount,"random_buffer =", random_buffer)
    time.sleep(random_buffer)

"""
====================================================
            dungeon specific functions
====================================================
"""

def print_starting_noise(tab_amount=""):
    """
    it's going to start off as a bunch of random numbers that change every half second or so
    then eventually a random number will turn into either a 1 or a 0

    :param tab_amount:
    :return:
    """
    random_numbers_array = get_random_numbers_array()

def hthq_door_minigame(tab_amount=""):
    wait_random_buffer()
    print("initializing Evil Ninja OS...")
    wait_random_buffer()

    #detec the os so we can clear the terminal
    if os.name == 'nt':
        #print("Windows-based system")
        os.system("cls")
    elif os.name == 'posix':
        #print("Unix-based system (Linux, macOS, etc.)")
        os.system("clear")

    #TODO: get rid of the goofy ahh '\0'
    print_starting_noise()

if __name__ == "__main__":
    hthq_door_minigame()
