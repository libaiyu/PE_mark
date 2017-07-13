# _*_ coding: utf_8  _*_
import os
import re
import logging

# logging.basicConfig(level = logging.ERROR, format = ' %(asctime)s - %(levelname)s - %(message)s' )                   
logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )                   
logging.debug('--------Start----------')

reg = r'.doc$' # reg = r'.docx$'
fnRegex = re.compile(reg)

n = 1
files = os.listdir('D:\\_PythonWorks\\wordOperate\\collectDoc')
for file in files:
    logging.debug(file)
    docFile = fnRegex.search(file)
    if(docFile):    
        dotPos = file.find('.')
        logging.debug('dotPos: ' + str(dotPos))
        
        _Pos = file.find('_')
        logging.debug('_Pos: ' + str(_Pos))
        
        if( n < 5 ):
            n +=1
            newName = file[:_Pos]+file[dotPos-1:]
            print('file:  '+file+"\n"+'newName:  '+newName)
            os.rename(file,newName)
        
logging.debug('--------End----------')
           
