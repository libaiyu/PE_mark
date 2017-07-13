# _*_ coding: utf_8  _*_
import os
import re

for files in os.listdir('.'):
    print( files )
    newname = files+'del'
    print( files, newname )
    input( 'stop for safe')
    os.rename( files, newname)
 

