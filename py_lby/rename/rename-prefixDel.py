#! python3
# _*_ coding: utf_8  _*_
import os
import re

dirName = input('please input the directory: ')
fileType = input('input the file type: ')
fReg = re.compile('.' + fileType + '$')
prefix = input('please input the prefix: ')
pre = re.compile('^' + prefix)

files = os.listdir(dirName)
count = 0
finishCount = 0
for file in files:
    #    print(file)
    if fReg.search(file):       
        if pre.search(file):
            newName = file[len(prefix):]        # del prefix 
            print(file,"\n",newName)
            count += 1
            if count < 3:
                input('Please input "c" for continue: %c')                
            try:
                os.rename(dirName + '\\' + file,dirName + '\\' + newName)
                finishCount += 1
            except FileExistsError:
                print('file already exist. this file has not renamed.')
print('finish deleting prefix %d files in %d files .'% (finishCount,count)) 
