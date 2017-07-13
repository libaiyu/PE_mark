#! python3

>>> import pyperclip
>>> import webbrowser

>>> webbrowser.open('http://www.ecit.cn/')
True

>>> webbrowser.open('https://cas.ecit.cn/index.jsp?service=http://portal.ecit.cn/Authentication')
True

>>> import requests




>>> res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
>>> type(res)
<class 'requests.models.Response'>
>>> res.status_code
200
>>> res.status_code == requests.codes.ok
True
>>> len(res.text)
178981
>>> print(res.text[:250])
﻿The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare



This eBook is for the use of anyone anywhere at no cost and with

almost no restrictions whatsoever.  You may copy it, give it away or

re-use it under the terms of the Proje
>>> print(res.text[:178981])
﻿The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare



This eBook is for the use of anyone anywhere at no cost and with

......

