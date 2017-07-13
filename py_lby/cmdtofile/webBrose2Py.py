 import pyperclip
 import webbrowser
 webbrowser.open('http://www.ecit.cn/')
 webbrowser.open('https://cas.ecit.cn/index.jsp?service=http://portal.ecit.cn/Authentication')
 import requests
 res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
 type(res)
 res.status_code
 res.status_code == requests.codes.ok
 len(res.text)
 print(res.text[:250])
 print(res.text[:178981])
 res.raise_for_status()
 playfile = open('RomeoAndJuliet.txt','wb')
 for chunk in res.iter_content(10000):
 playfile.close()
 playfile = open('RomeoAndJuliet.txt','wb')
 for chunk in res.iter_content(100000):
 playfile.close()
