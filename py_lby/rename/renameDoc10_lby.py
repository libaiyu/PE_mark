# _*_ coding: utf_8  _*_
# change the suffix from .xls to .xlsx
import os,openpyxl,pprint,logging


#logging.disable(logging.CRITICAL)

logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )                   

logging.debug('Start of program')

files = os.listdir('d:\_PythonWorks\execlOperate\PE_marks')
for filename in files:
    logging.debug(filename)
    _Pos = filename.find('-')
    logging.debug(_Pos)
    dotPos = filename.find('.')
    logging.debug(dotPos)
    if( filename[dotPos+1:] == 'xlsx' ):
        newName = 'PE_' + filename[_Pos+1:dotPos]+'.xlsx'
        logging.debug(newName)
        os.rename(filename,newName)
#    input('Please input "c" for continue: %c')
           
