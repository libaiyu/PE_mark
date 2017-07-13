# _*_ coding: utf_8  _*_
import os
import re

fileName = []
# selectFileName = []

rule = r'\+'

for root,dirs,files in os.walk("d:\_PythonWorks"):  
    fileName.append("%s" % (files ))
    if (  re.findall( rule,( "%s" % (files ) ) ) ):
        print( files )
for i in range( len(files) ):
    if (  re.findall( rule,files[i] ) ):
        name = files[i]
        print( '*'*20 )
        print( name )
print('Done!')
           
