#! python3

import pyperclip
import webbrowser
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/page_that_not _exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))

