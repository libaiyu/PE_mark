import os
import pyautogui

os.chdir('d:\\_PythonWorks\\working')

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
