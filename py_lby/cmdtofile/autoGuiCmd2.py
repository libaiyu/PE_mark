
>>> import os
>>> import pyautogui
>>> import time
>>> time.sleep(1)

>>> im = pyautogui.screenshot()

>>> im.save('submit.png')
>>> pyautogui.locateOnScreen('submit.png')
>>> print(pyautogui.locateOnScreen('submit.png'))
None
>>> pyautogui.locateOnScreen('submit.png')
>>> print(pyautogui.locateOnScreen('submit.png'))
None
>>> im = pyautogui.screenshot()
>>> im.save('submit.png')
>>> pyautogui.locateOnScreen('submit.png')
>>> print(pyautogui.locateOnScreen('submit.png'))
None
>>> from PIL import Image
>>> Image.open('submit.png')
<PIL.PngImagePlugin.PngImageFile image mode=RGB size=1366x768 at 0x1F77290>
>>> im1 = Image.open('submit.png')
>>> im1.size()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    im1.size()
TypeError: 'tuple' object is not callable
>>> im1.size
(1366, 768)
>>> im2 = im1.crop(200,200,200,200)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    im2 = im1.crop(200,200,200,200)
TypeError: crop() takes from 1 to 2 positional arguments but 5 were given
>>> im2 = im1.crop((200,200,200,200))
>>> im2.save('submit2.png')
Traceback (most recent call last):
  File "C:\Python34\lib\site-packages\PIL\ImageFile.py", line 461, in _save
    fh = fp.fileno()
AttributeError: '_idat' object has no attribute 'fileno'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    im2.save('submit2.png')
  File "C:\Python34\lib\site-packages\PIL\Image.py", line 1728, in save
    save_handler(self, fp, filename)
  File "C:\Python34\lib\site-packages\PIL\PngImagePlugin.py", line 787, in _save
    [("zip", (0, 0)+im.size, 0, rawmode)])
  File "C:\Python34\lib\site-packages\PIL\ImageFile.py", line 469, in _save
    e.setimage(im.im, b)
SystemError: tile cannot extend outside image
>>> im2 = im1.crop((200,200,400,400))
>>> im2.save('submit2.png')
>>> pyautogui.locateOnScreen('submit2.png')
>>> print(pyautogui.locateOnScreen('submit.png'))
None
>>> im = pyautogui.screenshot()
>>> im.save('screen.png')
>>> im2 = im1.crop((200,200,200,200))
>>> im2.save('submit.png')
Traceback (most recent call last):
  File "C:\Python34\lib\site-packages\PIL\ImageFile.py", line 461, in _save
    fh = fp.fileno()
AttributeError: '_idat' object has no attribute 'fileno'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    im2.save('submit.png')
  File "C:\Python34\lib\site-packages\PIL\Image.py", line 1728, in save
    save_handler(self, fp, filename)
  File "C:\Python34\lib\site-packages\PIL\PngImagePlugin.py", line 787, in _save
    [("zip", (0, 0)+im.size, 0, rawmode)])
  File "C:\Python34\lib\site-packages\PIL\ImageFile.py", line 469, in _save
    e.setimage(im.im, b)
SystemError: tile cannot extend outside image
>>> im2 = im1.crop((200,200,400,400))
>>> im2.save('submit.png')
>>> pyautogui.locateOnScreen('submit.png')
>>> print(pyautogui.locateOnScreen('submit.png'))
None
>>> im2 = im1.crop((200,200,400,400))
>>> im2.save('submit.png')
>>> im2 = im.crop((200,200,400,400))
>>> im2.save('submit.png')
>>> pyautogui.locateOnScreen('submit.png')
(200, 200, 200, 200)
>>> 
