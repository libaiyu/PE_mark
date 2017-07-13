import pypdf2
import PyPDF2
pdfFileObj = open('md-ch2.pdf','rb')
os.chdir('d:\\_PythonWorks\\pdfOperate')
import os
os.chdir('d:\\_PythonWorks\\pdfOperate')
pdfFileObj = open('md-ch2.pdf','rb')
pdfReader.numPages
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText().decode(__utf_8)
