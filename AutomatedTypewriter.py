import pyautogui as pt
import time

i = 0
time.sleep(3)
while i < 100:
    pt.typewrite('Hello World')
    pt.press('enter')
    time.sleep(1)
    i+=1
