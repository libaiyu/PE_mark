import os
from PIL import Image

os.chdir('d:\\_PythonWorks\\working')
testIm = Image.open('RCoscillate.png')
croppedIm = testIm.crop((200,100,300,150))
testImWidth,testImHeight = testIm.size
croppedImWidth,croppedImHeight = croppedIm.size
testCopyIm = testIm.copy()
row = 1
for left in range(0,testImWidth,croppedImWidth):
    for top in range(0,testImHeight,croppedImHeight):
        print(left,top)
        testCopyIm.paste(croppedIm,(left,top))
    testCopyIm.save('%dmultirow.png'%(row))
    row += 1
testCopyIm.save('tiled.png')
