from PIL import Image
testIm = Image.open('RCoscillate.png')
testIm.size
width,height = testIm.size
width
height
testIm.filename
testIm.format
testIm.format_description
testIm.save('test.jpg')
im = Image.new('RGBA',(100,200),'purple') # red blue black white green gray yellow 
im.save('purpleImage.png')
im2 = Image.new('RGBA',(10,20))   # chocolate cornflowerblue
im2.save('transparentImage.png')
im2 = Image.new('RGBA',(10,20),'chocolate')
im2.save('chocolateImage.png')
im2 = Image.new('RGBA',(10,20),'cornflowerblue')
im2.save('cornflowerblueImage.png')
testIm = Image.open('RCoscillate.png')
testIm.crop((200,100))
testIm.crop((200,100,300,150))
croppedIm = testIm.crop((200,100,300,150))
croppedIm.save('cropped.png')
