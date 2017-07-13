import os
import pyautogui
import time
time.sleep(1)
##pyautogui.scroll(200)
##pyautogui.scroll(800)
##time.sleep(5)pyautogui.scroll(200)
##time.sleep(5);pyautogui.scroll(200)
##time.sleep(5);pyautogui.scroll(200)
##time.sleep(5);pyautogui.scroll(200)

im = pyautogui.screenshot()
im.getpixel((0,0))
im.getpixel((50,200))
pyautogui.pixelMatchesColor(50,200,(255, 255, 255))
pyautogui.pixelMatchesColor(50,200,(255, 155, 255))
