>>> import pypdf2
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import pypdf2
ImportError: No module named 'pypdf2'
>>> import PyPDF2
>>> pdfFileObj = open('md-ch2.pdf','rb')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pdfFileObj = open('md-ch2.pdf','rb')
FileNotFoundError: [Errno 2] No such file or directory: 'md-ch2.pdf'
>>> os.chdir('d:\\_PythonWorks\\pdfOperate')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    os.chdir('d:\\_PythonWorks\\pdfOperate')
NameError: name 'os' is not defined
>>> import os
>>> os.chdir('d:\\_PythonWorks\\pdfOperate')
>>> pdfFileObj = open('md-ch2.pdf','rb')
>>> pdfReader.numPages
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    pdfReader.numPages
NameError: name 'pdfReader' is not defined
>>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
>>> pdfReader.numPages
18
>>> pageObj = pdfReader.getPage(0)
>>> pageObj.extractText().decode(__utf_8)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    pageObj.extractText().decode(__utf_8)
AttributeError: 'str' object has no attribute 'decode'
