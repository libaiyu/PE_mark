import os
from PIL import Image

os.chdir('d:\\_PythonWorks\\working')
testIm = Image.open('RCoscillate.png')
width,height = testIm.size
testResizeIm = testIm.resize((int(width * 2),int(height * 2)))
testResizeIm.save('testresize.png')
testResize2Im = testIm.resize((int(width * 1.2),height + 600 ))
testResize2Im.save('testresize2.png')
