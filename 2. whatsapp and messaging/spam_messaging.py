from cv2 import SparseMat_HASH_BIT
import pyautogui as auto
import time

time.sleep(10)
while True:
    auto.write("spam") #write here what you want to spam
    auto.press("enter")
    time.sleep(0)

