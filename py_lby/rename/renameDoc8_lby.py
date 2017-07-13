# _*_ coding: utf_8  _*_
# change the suffix from .p to .py
import os,openpyxl,pprint,logging

logging.basicConfig(level = logging.ERROR, format = ' %(asctime)s - %(levelname)s - %(message)s' )                   

logging.debug('Start of program')

os.chdir('d:\\_PythonWorks\\LearningPython')

i=0
files = os.listdir('.')
for filename in files:
    logging.debug(filename)
    dotPos = filename.find('.')
    logging.debug(dotPos)
    logging.debug(filename[dotPos])
    if (filename[dotPos+1:] == 'p' ):
        newname = filename[:dotPos+1] + 'py'
        logging.debug(filename + ' ' + newname)
        os.rename(filename,newname)
    i+=1
    logging.debug( str(i) )
