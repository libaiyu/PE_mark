import PyPDF2
import os
os.chdir('d:\\_PythonWorks\\pdfOperate')
pdfFileObj = open('md-ch2.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
