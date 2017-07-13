>>> import os
>>> import pyautogui

>>> pyautogui.scroll(200)
>>> pyautogui.scroll(200)
>>> pyautogui.scroll(200)
>>> pyautogui.scroll(200)
>>> import pyautogui
>>> pyautogui.scroll(200)
>>> time.sleep(5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    time.sleep(5)
NameError: name 'time' is not defined
>>> import time
>>> time.sleep(5)
>>> pyautogui.scroll(200)
>>> pyautogui.scroll(800)
>>> time.sleep(5)pyautogui.scroll(200)
SyntaxError: invalid syntax
>>> time.sleep(5);pyautogui.scroll(200)
>>> time.sleep(5);pyautogui.scroll(200)
>>> time.sleep(5);pyautogui.scroll(200)
>>> import pyautogui
>>> im = pyautogui.screenshot()
>>> im.getpixel((0,0))
(58, 110, 165)
>>> im.getpixel((50,200))
(255, 255, 255)
>>> pyautogui.pixelMatchesColor(50,200,(255, 255, 255))
True
>>> pyautogui.pixelMatchesColor(50,200,(255, 155, 255))
False
