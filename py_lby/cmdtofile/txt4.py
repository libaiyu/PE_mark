# how to del the \n

# _*_ coding: utf_8  _*_
import os
import re

srctext = 'd:\\_PythonWorks\\testDoc.txt'
dsttext = 'd:\\_PythonWorks\\resultDoc4.txt'
f = open (srctext,'r+')
f2 = open (dsttext,'w')

res = r'.\n$'

for lineContent in f.readlines():

    
    re.findall(res,lineContent)
    print lineContent
    
    lineContent.replace('\n','')
    print lineContent

    f2.seek(2,2)
    f2.write(lineContent)

f.close()

f2.close()
f2 = open (dsttext,'r')


# f2.replace('\n','')   #  can not finish

print f2.readlines()
f2.close()
