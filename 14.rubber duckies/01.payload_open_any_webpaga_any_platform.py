#A simple script that opens a webpage. It's based on Hak5 2124, but it presses Command+Space 3 times, because on Windows it changes the keyboard layout, and it has 3 options. Make sure to change the firmware as in the original video on Macs to avoid the pop-up about the layout.

# Converted using ducky2python by CedArctic (https://github.com/CedArctic/ducky2python) 

import pyautogui
import time
time.sleep(0.6)

# Linux run dialog
pyautogui.hotkey("alt","f2")
time.sleep(0.2)
# Mac OS run dialog
pyautogui.hotkey("win","space")
time.sleep(0.2)
# On Windows this changes the input language, so press 3 times
pyautogui.hotkey("win","space")
time.sleep(0.2)
pyautogui.hotkey("win","space")
time.sleep(0.2)
pyautogui.hotkey("win","R")
time.sleep(0.2)

# On another OS, this could have typed "r". Backspace 4 times.
pyautogui.hotkey("delete")
pyautogui.hotkey("delete")
pyautogui.hotkey("delete")
pyautogui.hotkey("delete")
pyautogui.hotkey("delete")

# Type in URL and open page!
pyautogui.typewrite("# Converted using ducky2python by CedArctic (https://github.com/CedArctic/ducky2python", interval=0.02) 
import pyautogui
import time
time.sleep(0.6)
# Linux run dialog
pyautogui.hotkey("alt","f2")
time.sleep(0.2)
# Mac OS run dialog
pyautogui.hotkey("win","space")
time.sleep(0.2)
# On Windows this changes the input language, so press 3 times
pyautogui.hotkey("win","space")
time.sleep(0.2)
pyautogui.hotkey("win","space")
time.sleep(0.2)
pyautogui.hotkey("win","R")
time.sleep(0.2)


# On another OS, this could have typed "   r". Backspace 4 times.
pyautogui.hotkey("delete")
pyautogui.hotkey("delete")
pyautogui.hotkey("delete")
pyautogui.hotkey("delete")
pyautogui.hotkey("delete")


# Type in URL and open page!
pyautogui.typewrite("http://example.com/", interval=0.02)
pyautogui.hotkey("enter")

pyautogui.hotkey("enter")
