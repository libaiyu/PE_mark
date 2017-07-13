import os
import pyautogui

os.chdir('d:\\_PythonWorks\\working')

pyautogui.PAUSE = 5
pyautogui.FAILSAFE = True
pyautogui.size()
width,height = pyautogui.size()
for i in range(2):
    pyautogui.moveTo(100,100,duration = 0.5)
    print(pyautogui.position())
    pyautogui.moveTo(200,100,duration = 0.5)
    print(pyautogui.position())
    pyautogui.moveTo(200,200,duration = 0.25)
    print(pyautogui.position())
    pyautogui.moveTo(100,200,duration = 0.25)
    print(pyautogui.position())
for i in range(2):
    pyautogui.moveRel(100,-100,duration = 0.25)
    print(pyautogui.position())
    pyautogui.moveRel(200,100,duration = 0.25)
    print(pyautogui.position())    
    pyautogui.moveRel(-200,200,duration = 0.5)
    print(pyautogui.position())
    pyautogui.moveRel(-100,-200,duration = 0.5)
    print(pyautogui.position())
