###############################################################################

# Panja lada lada kar apna spacebar mat tod dena!
# Copyright (C) 2022  Siddh Raman Pant

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# The online repository may be found at <https://github.com/siddhpant/panja>.

###############################################################################


from sys import exit
from time import sleep

from pynput import keyboard


pressed = False
fight = []
fight_len = 0
hand = None  # Index
won = None  # True if win, False if lose


def set_hand(spaces: int):
    global fight, fight_len, hand
    fight = list("|" + (" " * spaces) + "💪" + (" " * spaces) + "|")
    fight_len = len(fight)
    hand = spaces + 1
# End of set_hand()


def print_fight():
    print("\t", end="")
    print(*fight, sep="", end="\r")
# End of print_fight()


def move_hand(direction: bool):  # True for right, False for left.
    global won, fight, hand
    
    if won is None:
        offset = 1 if direction else -1
        fight[hand], fight[hand + offset] = fight[hand + offset], fight[hand]
        hand += offset
        
        print_fight()
        
        if hand == (fight_len - 2):
            won = True
        elif hand == 1:
            won = False
        
    else:
        if won:
            print("\n\n\t\t !!! BHAI AAP JEET GAYE !!!\n")
        else:
            print("\n\n\t\t lmao you lost, what a wimp.")
        
        input("\nPress any key to exit.")
        exit(0)
# End of move_hand()


def on_press(key):
    global pressed, won
    if key == keyboard.Key.space:
        if not pressed and won is None:
            move_hand(True)
            pressed = True
# End of on_press()


def on_release(key):
    global pressed
    if key == keyboard.Key.space:
        pressed = False
# End of on_release()


listener = keyboard.Listener(on_press=on_press, on_release=on_release)

print("\t\t!!! PANJA ZONE !!!\n")

level = int(input("Enter level to play: "))
set_hand(40)  # In future this can depend on level
delay = 1/level  # In seconds

print("Keep pressing space to win! Go!\n\n")
print_fight()
listener.start()

while True:
    sleep(delay)
    move_hand(False)
# End of while loop.


# End of file.
