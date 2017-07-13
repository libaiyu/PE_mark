import os
import pyautogui

os.chdir('d:\\_PythonWorks\\learnPy\\cmdtofile')

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width,height = pyautogui.size()

print('Press Ctrl-c to quit.')
try:
    while True:
        x,y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr,end = '')
        print('\b' * len(positionStr),end = '',flush = True)
except KeyboardInterrupt:
    print('\ndone.')
pyautogui.click(10,5)
pyautogui.mouseDown(20,50)
pyautogui.mouseUp(20,50)
pyautogui.doubleClick(200,150)
pyautogui.rightClick(120,220)
pyautogui.middleClick(160,80)
