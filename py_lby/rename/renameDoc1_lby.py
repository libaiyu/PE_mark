# _*_ coding: utf_8  _*_
import os
import re

export = []

for root,dirs,files in os.walk("d:\_PythonWorks"):
    export.append( "\n %s;%s;%s" % (root,dirs,files ))
    print( export )
open('filename.txt','w').write(''.join(export) ) 

