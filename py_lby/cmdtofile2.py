# _*_ coding: utf_8  _*_
#! python3
import re
import logging
# It can work correctly. 2017-2-26  6:10
# Add directory.         2017-3-2
# A command will not be copied If the command can not work correctly. 2017-3-2
# use relative path.                  2017-4-29

# when file has this content, the program can not work. 2017-2-26 6:40
'''
>>> pageObj.extractText()
'1—˚xG˘M™˛9NÈNÈ˚7˛9NÈGÿM”?òNÈNÈ+X1Ñ4ô˘@˘p/j,´˙n+eD˜+X!ﬁ.ž,´1V˛±>Ł1Ñ+e$À+e+e˚7˝>˛±1—˚x˙n+eD˜˘p/j7--O˙n,´!ﬁF9>Ÿ4ô˙€4ô4ô4ô4ô1—˚x˙n+eD˜˘p/j7--O˙n,´!ﬁ'

'''
# when file has this content, the program can not work. 2017-2-26 6:40


logging.basicConfig( level = logging.ERROR, format = ' %(asctime)s - %(levelname)s - %(message)s' )
# logging.basicConfig( level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )
logging.debug('--------Start of program---------')

class CmdToFile():
    """
    There is a file that simply copy command lines,
    Copy necessary context in this file , to compose a python file.  
    """

    def __init__(self,srcdoc,dstdoc):
        # the file that copy command lines
        self.srcdoc = srcdoc
        # the destination python file that is wanted to compose
        self.dstdoc = dstdoc
        # all string lines to be written
        self.lines = []
  
    def composepy(self, regex):
        # read the file that copy command lines to get the string lines
        with open(self.srcdoc, 'r') as srcfile:
            lines = srcfile.readlines()
            for n in range( 1, len( lines)):
                lineNeed = regex.search( lines[n-1])
                regex2 = re.compile( '^Traceback')
                delline = regex2.search( lines[n])
                if lineNeed and not delline:
                    logging.debug( lineNeed.group(1))
                    #input('stop for debug')
                    self.lines.append( lineNeed.group(1))                    
        # write lines to pyfile
        with open(self.dstdoc, 'w') as dstfile:
            for line in self.lines:
                dstfile.write(line)
            print ( 'File: %s is composed' % self.dstdoc )
        print('End.')

def main():
    SRCDOC = input('please input the source file name *.py(*.txt): ')
    DSTDOC = input('please input the destination file name *.py:')
    # RegEx = re.compile( r'>{3}\s(.*)')  # it will missing \n.
    regEx = re.compile( r'^>{3}\s(.*)', re.DOTALL)
    pycom = CmdToFile(SRCDOC, DSTDOC)
    pycom.composepy(regEx)

if __name__ == '__main__':
    main()

    
