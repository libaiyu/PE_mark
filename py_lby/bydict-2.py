#! python3
# _*_ coding: utf_8  _*_
''' Try to help me to remember the words that I have already checked up.
every time I look up the words in dictionary, then copy it and its meaning
to the entry, then return.
this program will write the words and its meaning to the bydict.txt.  2017-4-23
'''

import datetime
import os

def word_backup():

    # get the word and meaning
    st = input("请输入单词和解释：")
    # write the time, word and meaning into the word_backup.txt. 
    word_backfile = 'word_backup.txt'
    t = datetime.datetime.now()
    memory_file = open( word_backfile,'a')
    memory_file.write( str( t.year)+'-'+str( t.month)+'-'+str( t.day)+','+str( t.hour)+':'+str( t.minute)+':'+str( t.second)+','+'\n')
    memory_file.write( st+'\n\n')
    memory_file.close()
    print(st+'\n')


if __name__ == '__main__':
    '''
'''
    while True:
        word_backup()
        con = input('yes or no? n for quit:')
        if con == 'n':
            break
    print('End')

