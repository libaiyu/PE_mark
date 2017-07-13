# _*_ coding: utf_8  _*_
import os
import re

fileName = []

rule = r'\+'

for root,dirs,files in os.walk("d:\_PythonWorks"):
    # export.append( "\n %s;%s;%s" % (root,dirs,files ))    
    fileName.append("%s" % (files ))
    print( fileName )
    print("*"*66)
    if (  re.findall( rule,( "%s" % (files ) ) ) ):
        print( ( "%s" % (files ) ) )
print('Done!')
           
