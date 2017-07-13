#! python3

>>> import requests
>>> import bs4
>>> res = requests.get('http://www.ecit.cn/')
>>> res.raise_for_status()
>>> noStarchSoup = bs4.BeautifulSoup(res.text)
>>> type(noStarchSoup)
<class 'bs4.BeautifulSoup'>
>>> 


>>> import os
>>> os.getcwd()
'C:\\Python34'
>>> os.chdir('d:\\_PythonWorks')


>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile)
>>> type(exampleSoup)
<class 'bs4.BeautifulSoup'>
>>> print(exampleSoup)

##<html><head><title>The Website Title</title></head>
##<body>
##<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>
##<p class="slogan">Learn Python the easy way!</p>
##<p>By <span id="author">Al Sweigart</span></p>
##</body></html>


>>> exampleSoup.select('span')
[<span id="author">Al Sweigart</span>]
>>> 


>>> import bs4
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read ())
>>> elems = BeautifulSoup.select('#author')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    elems = BeautifulSoup.select('#author')
NameError: name 'BeautifulSoup' is not defined
>>> elems = exampleSoup.select('#author')
>>> type(elems)
<class 'list'>
>>> len(elems)
1
>>> type(elems[0])
<class 'bs4.element.Tag'>
>>> elems[0].getText()
'Al Sweigart'
>>> str(elems[0])
'<span id="author">Al Sweigart</span>'
>>> elems[0].attrs
{'id': 'author'}
>>> 


>>> pElems = exampleSoup.select('p')
>>> str(pElems[0])
'<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>'
>>> pElems[0].getText()
'Download my Python book from my website.'
>>> str(pElems[1])
'<p class="slogan">Learn Python the easy way!</p>'
>>> pElems[1].getText()
'Learn Python the easy way!'
>>> str(pElems[2])
'<p>By <span id="author">Al Sweigart</span></p>'
>>> pElems[2].getText()
'By Al Sweigart'
>>> 
