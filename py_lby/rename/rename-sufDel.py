#! python3
# _*_ coding: utf_8  _*_
import os
import re
import logging

logging.basicConfig(level = logging.ERROR, format = ' %(asctime)s - %(levelname)s - %(message)s' )                   
# logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )                   
logging.critical('--------Start----------')

dirName = input('please input the directory: ')
# dirName = 'd:\\_201503Lby\\jq2'
# dirName = 'd:\_PythonWorks\wordOperate\collectDoc' 
fileType = input('input the file type: ')
# fileType = 'jgs'
# fileType = 'doc' 
fReg = re.compile('\.' + fileType + '$')
# suffix = input('please input the suffix: ')
suffix = '_\d{1,5}\.'
suf = re.compile(suffix)

files = os.listdir(dirName)
count = 0
finishCount = 0
for file in files:
    if fReg.search(file):
        if suf.search(file):
            leng = suf.search(file).group()
            logging.debug(leng)
            dotPos = file.find('.')
            logging.debug('dotPos: %d' % dotPos)
            newName = file[:dotPos - len(leng)+1] + file[dotPos:]
            print('file:  ' + file + "\n" + 'newName:  ' + newName)
            count += 1
            if count < 3:
                input('Please input "c" for continue: %c')                
            try:
                os.rename(dirName + '\\' + file,dirName + '\\' + newName)
                finishCount += 1
            except FileExistsError:
                logging.error('file already exist. this file has not renamed.')
print('finish %d files in %d files.'% (finishCount,count))
logging.critical('--------End----------')
