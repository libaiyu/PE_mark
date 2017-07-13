# _*_ coding: utf_8  _*_
#! python3
import re
import logging


logging.basicConfig( level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s' )

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
        #  a list of regex to used when match
        self.regExList = []
        # all string lines to be written
        self.lines = []

    def set_regular(self,reList):
        for st in reList:
            self.regExList.append( re.compile( st ) )

    def reg_match(self,line):
        for regEx in self.regExList:
            if ( re.match(regEx,line) ):
                return True
            return False
        
    def composePy(self):
        # read the file that copy command lines to get the string lines
        with open(srcDoc, 'r') as srcFile:
            for line in srcFile.readlines():
                # add the line if matches
                if ( self.reg_match(line) ):
                    self.lines.append(line)                    
        # write lines to pyfile
        with open(dstDoc, 'w') as dstFile:
            for line in self.lines:
                dstFile.writelines(line)

        print ( 'File: %s is composed' % self.dstDoc )

if __name__ == '__main__':
    srcDoc = 'docPageBreakTest.py'
    dstDoc = 'docPageBreak1.py'
    ReList = [r'^>{3}(.*$)']
    pyCom = cmdLineToPy(srcDoc, dstDoc)
    pyCom.set_regular(ReList)
    pyCom.composePy()

