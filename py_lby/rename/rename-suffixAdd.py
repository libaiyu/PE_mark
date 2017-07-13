#! python3
# _*_ coding: utf_8  _*_
import os
import re

finishCount = 0
for fold,subfold,files in os.walk('.'):
    for e in files:
        if e[-2:] != 'py':
            dot_pos = e.find('.')
            newName = e[:dot_pos] + '-2' + e[dot_pos:]       # add prefix
            print(e,"\n",newName)
            yes_no = input('Please input "c" for continue: %c')
            if yes_no:
                os.rename(e,newName)
                finishCount += 1

print('finish adding suffix %d files.'% (finishCount))       
