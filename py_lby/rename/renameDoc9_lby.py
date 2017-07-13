#! python3
# _*_ coding: utf_8  _*_
import os
import re
import logging

logging.basicConfig(level = logging.ERROR, format = ' %(asctime)s - %(levelname)s - %(message)s' )                   
# logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )                   
logging.critical('--------Start----------')

dirName = input('please input the directory: ')
fileType = input('input the file type: ')
fReg = re.compile('.' + fileType + '$')
dels = re.compile(r'_\.')  # dels = re.compile(r'_\d{1,5}.')

files = os.listdir(dirName)
count = 0
for file in files:
    if fReg.search(file):
        if dels.search(file):
            leng = dels.search(file).group()
            logging.debug(leng)
            dotPos = file.find('.')
            logging.debug('dotPos: %d' % dotPos)
##            _Pos = file.find('_')
##            logging.debug('_Pos: %d' % _Pos)            
##            if(_Pos > 0):
##                newName = file[:_Pos] + file[dotPos-1] + file[_Pos:dotPos - 1] + file[dotPos:]
            newName = file[:dotPos - len(leng) + 1] + file[dotPos:]
            print('file:  ' + file + "\n" + 'newName:  ' + newName)

#            if count < 2:
            input('Please input "c" for continue: %c')
            try:
                os.rename(dirName + '\\' + file,dirName + '\\' + newName)
                count += 1
            except FileExistsError:
                print('file already exist. this file has not renamed.')
print('finish %d files.'% (count))
logging.critical('--------End----------')
