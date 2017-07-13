>>> import docRead
 2017-01-21 10:17:20,191 - CRITICAL - --------Start of program---------
>>> doc = doc.Document()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    doc = doc.Document()
NameError: name 'doc' is not defined
>>> doc = docx.Document()
>>> doc.add_paragraph('this is on the first page')
<docx.text.paragraph.Paragraph object at 0x0288AE50>
>>> doc.add_page_break()
<docx.text.paragraph.Paragraph object at 0x01CD9F90>
>>> doc.add_paragraph('this is on the first page')
<docx.text.paragraph.Paragraph object at 0x01CD94B0>
>>> doc.add_paragraph('this is on the second page')
<docx.text.paragraph.Paragraph object at 0x0288AE10>
>>> doc.save('testpagebreak')
>>> 
