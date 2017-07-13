#! python3
# _*_ coding: utf_8  _*_
import os
import re

rule = r'\+'

for root,dirs,files in os.walk("d:\_PythonWorks"):  
    if (  re.findall( rule,( "%s" % (files ) ) ) ):
        print( files )
for i in range( len(files) ):
    if (  re.findall( rule,files[i] ) ):
        name = files[i]
        print( '*'*5 )
        print( name )
        print( '*'*5 )
        leftHalf = []
        rightHalf = []
        newName = ''
        listName = list(name)
        for left in range(list.index(listName,'+')+1,len(name)-5):
            leftHalf += name[left]
            newName += str(name[left])
        for right in range(0,list.index(listName,'+') ):
            rightHalf += name[right]
            newName += str(name[right])
        print('rightHalf\n',rightHalf)        
        print('leftHalf\n',leftHalf)    
        leftHalf += rightHalf
        print( 'newName:', newName )
#        os.chdir( "d:\_PythonWorks\1510401Z")
        os.rename(name,newName+'.doc')
       # os.rename(name,newName)    #  FileNotFoundError: after copy the files to this dir. It works.
                
print('Done!')
           
