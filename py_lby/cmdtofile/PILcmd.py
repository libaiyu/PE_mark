import os
from PIL import Image
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from PIL import Image
ImportError: No module named 'PIL'
>>> from PIL import Image
os.chdir('d:\\_PythonWorks\\working')
>>> testIm = Image.open('RCoscillate.png')
>>> testIm.size
(435, 255)
>>> width,height = testIm.size
>>> width
435
>>> height
255
>>> testIm.filename
'RCoscillate.png'
>>> testIm.format
'PNG'
>>> testIm.format_description
'Portable network graphics'
>>> testIm.save('test.jpg')

>>> im = Image.new('RGBA',(100,200),'purple') # red blue black white green gray yellow 
>>> im.save('purpleImage.png')
>>> im2 = Image.new('RGBA',(10,20))   # chocolate cornflowerblue
>>> im2.save('transparentImage.png')

>>> im2 = Image.new('RGBA',(10,20),'chocolate')
>>> im2.save('chocolateImage.png')
>>> im2 = Image.new('RGBA',(10,20),'cornflowerblue')
>>> im2.save('cornflowerblueImage.png')
>>> testIm = Image.open('RCoscillate.png')
>>> testIm.crop((200,100))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    testIm.crop((200,100))
  File "C:\Python34\lib\site-packages\PIL\Image.py", line 1032, in crop
    x0, y0, x1, y1 = map(int, map(round, box))
ValueError: need more than 2 values to unpack
>>> testIm.crop((200,100,300,150))
<PIL.Image.Image image mode=RGBA size=100x50 at 0x2630150>
>>> croppedIm = testIm.crop((200,100,300,150))
>>> croppedIm.save('cropped.png')
