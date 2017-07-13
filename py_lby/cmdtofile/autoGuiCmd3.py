
>>> import os
>>> import pyautogui
>>> import time
>>> time.sleep(1)

>>> pyautogui.click(100,100);pyautogui.typewrite('Hello world!')
>>> pyautogui.click(100,100);pyautogui.typewrite('Hello world!',0.25)
>>> pyautogui.click(200,100);pyautogui.typewrite('如果含 有受控源!',0.25)
>>> pyautogui.click(200,100);pyautogui.typewrite('Hello worl如果含 有受控源!',0.25)
>>> pyautogui.typewrite(['a','b','left','left','X','Y'])
XYab

pyautogui.KEYBOARD_KEYS  # 查看此列表，可知pyautogui接受的所有可能的键字符串.

>>> pyautogui.keyDown('shift');pyautogui.press('4');pyautogui.keyUp('shift')
$
>>> pyautogui.keyDown('ctrl');pyautogui.keyDown('c');pyautogui.keyUp('c');pyautogui.keyUp('ctrl')

>>> pyautogui.hotkey('ctrl','c')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    pyautogui.hotkey('ctrl','c')
  File "C:\Python34\lib\site-packages\pyautogui\__init__.py", line 1000, in hotkey
    _autoPause(kwargs.get('pause', None), kwargs.get('_pause', True))
  File "C:\Python34\lib\site-packages\pyautogui\__init__.py", line 163, in _autoPause
    time.sleep(PAUSE)
KeyboardInterrupt
>>> def commentAfterDelay():
	pyautogui.click(100,100)
	pyautogui.typewrite('In IDLE,Alt-3 comments out a line.')
	time.sleep(2)
	pyautogui.hotkey('alt','3')

	
>>> commentAfterDelay()
