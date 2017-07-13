>>> import os
>>> import pyautogui
>>> import time
>>> time.sleep(1)

>>> im = pyautogui.screenshot()
>>> im.save('screen.png')


>>> im2 = im.crop((200,200,400,400))
>>> im2.save('submit.png')
>>> pyautogui.locateOnScreen('submit.png')
(200, 200, 200, 200)
>>> 
