# _*_ coding: utf_8  _*_
#! python3
import re
import logging

logging.basicConfig( level = logging.ERROR, format = ' %(asctime)s - %(levelname)s - %(message)s' )
# logging.basicConfig( level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )
logging.debug('--------Start of program---------')

class cmdLineToPy():
    """
    There is a file that simply copy command lines,
    Copy necessary context in this file , to compose a python file.  
    """

    def __init__(self,srcDoc,dstDoc):
        # the file that copy command lines
        self.srcDoc = srcDoc
        # the destination python file that is wanted to compose
        self.dstDoc = dstDoc
        # all string lines to be written
        self.lines = []
  
    def composePy(self):
        # read the file that copy command lines to get the string lines
        with open(self.srcDoc, 'r') as srcFile:
            for line in srcFile.readlines():
                logging.debug(line)
                # add the line if matches
                lineRegEx = re.compile( r'^>{3} (.*$)',re.DOTALL )
                lineNeed = re.findall(lineRegEx,str(line))
                logging.debug(lineNeed)
                if ( lineNeed ):
                    self.lines.append( lineNeed )                    
        # write lines to pyfile
        with open(self.dstDoc, 'w') as dstFile:
            for line in self.lines:
                dstFile.writelines(line)

        print ( 'File: %s is composed' % self.dstDoc )

def main():
    srcDoc = input('please input the source file name *.py: ' )
    dstDoc = input('please input the destination file name *.py:')  
    pyCom = cmdLineToPy(srcDoc, dstDoc)
    pyCom.composePy()

if __name__ == '__main__':
    main()

    
