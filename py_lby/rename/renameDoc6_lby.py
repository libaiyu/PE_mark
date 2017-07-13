# _*_ coding: utf_8  _*_
import os

files = os.listdir('d:\_PythonWorks')
for filename in files:
    if filename[:4] == '2015':
        newName = filename +'x'
        os.rename(filename,newName)
           
